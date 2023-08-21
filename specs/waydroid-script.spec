
%define ADD_DESCRIPTION_FROM_SUMMARY no
%global flavor @BUILD_FLAVOR@%{nil}
%define pypi_name waydroid_script
%define pypi_version main

%ifarch %{arm} 
%define wayarch armeabi-v7a 
%endif

%ifarch %{arm64} aarch64 
%define wayarch arm64-v8a 
%endif   Script to add gapps and other stuff to waydroid!

%ifarch %{x86_64} x86_64 amd64
%define wayarch x86_64
%endif

%ifarch %{ix86} 
%define wayarch x86
%endif

%define descr %{expand:
Python Script to add OpenGapps, Magisk, libhoudini translation library and
libndk translation library to waydroid !
}

%description
%{descr}

%define build_waydroid_extra_from_file(-) %{lua: 
larg = {}
lopt = {}

len = #arg
ind = 0

while ind < len do
  ind = ind + 1
  tk = arg[ind]
  if tk:sub(1, 2) == '--' then
    ind = ind + 1
    lopt[tk:sub(3)] = arg[ind]
  else 
    larg[#larg+1] = tk
  end
end

arg = larg

name = lopt['name'] or rpm.expand('%{?NAME:%NAME}')
if name == '' then 
  error('name is not defined')
end
source = lopt['source'] or rpm.expand('%{?SOURCE0:%SOURCE0}')
if source == '' then
  error('source is not defined')
end

license = lopt['license'] or rpm.expand('%{?LICENSE:%LICENSE}%{!?LICENSE:LGPL}')
summary = lopt['summary'] or rpm.expand('%{?SUMMARY:%SUMMARY}%{!?SUMMARY:Waydroid extra files}')
version = lopt['version'] or rpm.expand('%{?VERSION:%VERSION}%{!?VERSION:1}')
release = lopt['release'] or rpm.expand('%{?RELEASE:%RELEASE}%{!?RELEASE:1}')

main = lopt['dscr'] or rpm.expand('%{ADD_DESCRIPTION_FROM_SUMMARY}')
main = main:lower()
createdescription = (main == 'ok') or (main == 'yes') or (main == 'y') or (main == '1')

--main = opt.main
--main = main:lower()
--main = (main == 'ok') or (main == 'yes') or (main == 'y') or (main == '1')

a,b=rpm.isdefined('_waydroidextradir')
if (not a) or b then
  rpm.define('_waydroidextradir %{_datadir}/waydroid-extra')
end

a,b=rpm.isdefined('_waydroid_unit')
if (not a) or (not b) then
  rpm.define('_waydroid_unit() waydroid(%1)')
end

a,b=rpm.isdefined('_waydroid_provide')
if (not a) or (not b) then
  rpm.define('_waydroid_provide() Provides: %{_waydroid_unit %{1}}')
end

len=#arg

ind=0
dirs={}

while ind < len do
  ind = ind + 1
  dir = arg[ind]
  while dir do
    dir=dir:match("(.*)/")
    if dir then
        dirs['/' .. dir ] = 1
    else 
        dirs[''] = 1
    end
  end
end
nw = string.char(10) .. string.char(13)

--if main then
--    print('Name: ' .. name .. nw)
--else
--    print('%package -n ', name, nw)
--end

--print('License: ' .. license .. nw
--   .. 'Summary: ' .. summary .. nw
--   .. 'Version: ' .. version .. nw
--   .. 'Release: ' .. release .. nw)

ind = 0
while ind < len do
  ind = ind + 1
  print(rpm.expand('%_waydroid_provide ' .. arg[ind]) .. nw)
end

filename = source:match("^.*/(.*)$") or source
path = rpm.expand('%_datadir/') .. name .. '/' .. filename
waydroidextradir = rpm.expand('%_waydroidextradir')

if createdescription then
    print([[

%description 
]])
    --if main then
    --print('-n ', name)
    --end
    print(summary .. '.' .. nw)
end

if len > 0 then
print([[

%post ]])
--if main then 
--    print('-n ', name)
--end
print([[

#!/bin/sh
echo post install "$1"
if [ "$1" == 1 ]; then
]])

ind = 0

alternatives = rpm.expand('%{_sbindir}/update-alternatives')

if len == 1 then
  ind = ind + 1
  token = arg[ind]
  print(
  alternatives .. " --install '" .. waydroidextradir .. '/' 
  ..token..rpm.expand("' '%{_waydroid_unit "..token.."}' '" ) 
  ..path.."' 25" .. nw) 
else 
print('for i in ')
while ind < len do
  ind = ind + 1
  token = arg[ind]
  print("'" .. token .. "' ")
end
print('; do '..nw..alternatives.." --install '"..
    waydroidextradir.."'"..rpm.expand('/"$i" "%{_waydroid_unit $1}" ')
    .."'"..path .."' 25" .. nw .. "done" .. nw )
end


print([[
fi

%postun ]])
--if main then 
--    print('-n ', name)
--end
print([[

#!/bin/sh
echo post remove "$1"
if [ "$1" == 0 ]; then
]])

ind = 0

if len == 1 then
  ind = ind + 1
  token = arg[ind]
  print(alternatives .. rpm.expand(" --remove '%{_waydroid_unit "
  ..token.."}' '")..path.."' " .. nw) 
else 
print('for i in ')
while ind < len do
  ind = ind + 1
  token = arg[ind]
  print("'" .. token .. "' ")
end
print('; do '..nw..alternatives.. rpm.expand(
  ' --remove "%{_waydroid_unit $1}" ')
  .."'"..path .."' 25" .. nw .. "done" .. nw )
end

print('fi')
end

print(
[[


%files ]])
--if main then 
--    print('-n ', name)
--end
print(nw)
print(path, nw)
for key, v in pairs(dirs) do
  print('%dir '.. waydroidextradir ..  key .. nw)
end


print([[

%install 
]])

for key, v in pairs(dirs) do
  print('mkdir -p ' .. waydroidextradir .. key .. nw)
end
print("cp '"..rpm.expand('%{_sourcedir}/')..filename.."' " )

}


%if "%{flavor}" == "11-libndk-zip" 
%define mainsource https://github.com/supremegamers/vendor_google_proprietary_ndk_translation-prebuilt/archive/9324a8914b649b885dad6f2bfd14a67e5d1520bf.zip 
%define nameprovides libndktranslation.zip 11/libndktranslation.zip
%elif "%{flavor}" == "13-libndk-zip" 
%define mainsource https://github.com/supremegamers/vendor_google_proprietary_ndk_translation-prebuilt/archive/a090003c60df53a9eadb2df09bd4fd2fa86ea629.zip 
%define nameprovides libndktranslation.zip 13/libndktranslation.zip
%elif "%{flavor}" == "11-nodataperm-zip" 
%define mainsource https://github.com/ayasa520/hack_full_data_permission/archive/refs/heads/main.zip 
%define nameprovides nodataperm.zip 11/nodataperm.zip
%elif "%{flavor}" == "11-libhoudini-zip" 
%define mainsource https://github.com/supremegamers/vendor_intel_proprietary_houdini/archive/81f2a51ef539a35aead396ab7fce2adf89f46e88.zip 
%define nameprovides libhoudini.zip 11/libhoudini.zip
%elif "%{flavor}" == "11-hide-status-bar-apk" 
%define mainsource https://github.com/ayasa520/hide-status-bar/releases/download/v0.0.1/app-release.apk 
%define nameprovides hidestatusbar.apk 11/hidestatusbar.apk
%elif "%{flavor}" == "smartdock-apk" 
%define mainsource https://f-droid.org/repo/cu.axel.smartdock_198.apk 
%define nameprovides smartdock.apk
%elif "%{flavor}" == "x86_64-11-widevine-zip" 
%define mainsource https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/48d1076a570837be6cdce8252d5d143363e37cc1.zip 
%define nameprovides widevine.zip 11/widevine.zip x86_64/11/widevine.zip
%elif "%{flavor}" == "x86_64-13-widevine-zip" 
%define mainsource https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/a8524d608431573ef1c9313822d271f78728f9a6.zip 
%define nameprovides widevine.zip 13/widevine.zip x86_64/13/widevine.zip
%elif "%{flavor}" == "arm64-v8a-11-widevine-zip" 
%define mainsource https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/a1a19361d36311bee042da8cf4ced798d2c76d98.zip 
%define nameprovides widevine.zip 11/widevine.zip arm64-v8a/11/widevine.zip
%elif "%{flavor}" == "x86_64-11-OpenGapps-zip" 
%define mainsource https://sourceforge.net/projects/opengapps/files/x86_64/20220503/open_gapps-x86_64-11.0-pico-20220503.zip 
%define nameprovides gapps.zip 11/gapps.zip x86_64/11/gapps.zip
%elif "%{flavor}" == "x86-11-OpenGapps-zip" 
%define mainsource https://sourceforge.net/projects/opengapps/files/x86/20220503/open_gapps-x86-11.0-pico-20220503.zip 
%define nameprovides gapps.zip 11/gapps.zip x86/11/gapps.zip
%elif "%{flavor}" == "arm64-v8a-11-OpenGapps-zip" 
%define mainsource https://sourceforge.net/projects/opengapps/files/arm64/20220503/open_gapps-arm64-11.0-pico-20220503.zip 
%define nameprovides gapps.zip 11/gapps.zip arm64-v8a/11/gapps.zip
%elif "%{flavor}" == "armeabi-v7a-11-OpenGapps-zip" 
%define mainsource https://sourceforge.net/projects/opengapps/files/arm/20220215/open_gapps-arm-11.0-pico-20220215.zip 
%define nameprovides gapps.zip 11/gapps.zip armeabi-v7a/11/gapps.zip
%elif "%{flavor}" == "x86_64-13-MindTheGapps-zip" 
%define mainsource https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-x86_64-20230323.zip 
%define nameprovides gapps.zip 13/gapps.zip x86_64/13/gapps.zip
%elif "%{flavor}" == "x86-13-MindTheGapps-zip" 
%define mainsource https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-x86-20230323.zip 
%define nameprovides gapps.zip 13/gapps.zip x86/13/gapps.zip
%elif "%{flavor}" == "arm64-v8a-13-MindTheGapps-zip" 
%define mainsource https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-arm64-20230323.zip 
%define nameprovides gapps.zip 13/gapps.zip arm64-v8a/13/gapps.zip
%elif "%{flavor}" == "armeabi-v7a-13-MindTheGapps-zip" 
%define mainsource https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-arm-20230323.zip 
%define nameprovides gapps.zip 13/gapps.zip armeabi-v7a/13/gapps.zip
%elif "%{flavor}" == "MicroG-Standard-zip" 
%define mainsource https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-Standard-2.11.1-20230429100529.zip 
%define nameprovides MicroG.zip MicroG_Standard.zip
%elif "%{flavor}" == "MicroG-NoGoolag-zip" 
%define mainsource https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-NoGoolag-2.11.1-20230429100545.zip 
%define nameprovides MicroG.zip MicroG_NoGoolag.zip
%elif "%{flavor}" == "MicroG-UNLP-zip" 
%define mainsource https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-UNLP-2.11.1-20230429100555.zip 
%define nameprovides MicroG.zip MicroG_UNLP.zip
%elif "%{flavor}" == "MicroG-Minimal-zip" 
%define mainsource https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-Minimal-2.11.1-20230429100521.zip 
%define nameprovides MicroG.zip MicroG_Minimal.zip
%elif "%{flavor}" == "MicroG-MinimalIAP-zip" 
%define mainsource https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-MinimalIAP-2.11.1-20230429100556.zip 
%define nameprovides MicroG.zip MicroG_MinimalIAP.zip
%else
%global flavor script%{nil}', file=j)
%endif

%if "%flavor" == "script"
  %define main_name %{pypi_name}
%else
  %define main_name waydroid-%{flavor}
%endif


Name:           %{main_name}
Version:        0
Release:        1%{?dist}
Summary:        Script to add gapps and other stuff to waydroid!
License:        MIT
URL:            http://github.com/casualsnek/waydroid-script

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)


%if "%flavor" == "script"
Source0:        %{pypi_name}-%{pypi_version}.tar.gz

Requires: python3dist(tqdm)
Requires: python3dist(requests)
Requires: python3dist(InquirerPy)
Requires: python3dist(requests_file)

%package -n     waydroid-script-binary-%{wayarch}
Summary: Binaries for waydroid-script package

%description -n waydroid-script-binary-%{wayarch}
Binaries for waydroid-script package.

%package -n    waydroid-script
Summary:         Script to add gapps and other stuff to waydroid!
BuildArch: noarch
Requires:     python3-%{pypi_name}

%package -n     python3-%{pypi_name}
Summary:          Script to add gapps and other stuff to waydroid!
BuildArch: noarch
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires: lzip
Requires: waydroid-script-binary-%{wayarch}

%description -n waydroid-script
Python Script to add OpenGapps, Magisk, libhoudini translation library and
libndk translation library to waydroid !

%description -n python3-%{pypi_name}
Python Script to add OpenGapps, Magisk, libhoudini translation library and
libndk translation library to waydroid !

%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%build
%py3_build
%define  pypi_libdir    %{_usr}/lib/%{pypi_name}
%define  pypi_bindir  %{pypi_libdir}/bin
%define  pypi_oldbindir  %{python3_sitelib}/%{pypi_name}/bin

%install
%py3_install
mkdir -p %{buildroot}%{pypi_bindir}/%{wayarch}/
mv   %{buildroot}%{pypi_oldbindir}/%{wayarch}/resetprop    %{buildroot}%{pypi_bindir}/%{wayarch}/resetprop
rm -R %{buildroot}%{pypi_oldbindir}
ln -s %{pypi_bindir}   %{buildroot}%{pypi_oldbindir}


%files -n waydroid-script-binary-%{wayarch}
%{pypi_bindir}/%{wayarch}/resetprop 
%dir %{pypi_bindir}/%{wayarch}/
%dir %{pypi_bindir}/
%dir %{pypi_libdir}/

%files -n waydroid-script
%{_bindir}/waydroid-script

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/**/*
%dir %{python3_sitelib}/*



%else
Source0:        %mainsource
%{build_waydroid_extra_from_file  --name waydroid-%{flavor}  --source  %{mainsource}  }
%endif


