%define ADD_DESCRIPTION_FROM_SUMMARY yes
%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "11-libndk-zip" 
%build_waydroid_extra_from_file --name waydroid-11-libndk-zip --source https://github.com/supremegamers/vendor_google_proprietary_ndk_translation-prebuilt/archive/9324a8914b649b885dad6f2bfd14a67e5d1520bf.zip libndktranslation.zip 11/libndktranslation.zip
%elif "%{flavor}" == "13-libndk-zip" 
%build_waydroid_extra_from_file --name waydroid-13-libndk-zip --source https://github.com/supremegamers/vendor_google_proprietary_ndk_translation-prebuilt/archive/a090003c60df53a9eadb2df09bd4fd2fa86ea629.zip libndktranslation.zip 13/libndktranslation.zip
%elif "%{flavor}" == "11-nodataperm-zip" 
%build_waydroid_extra_from_file --name waydroid-11-nodataperm-zip --source https://github.com/ayasa520/hack_full_data_permission/archive/refs/heads/main.zip nodataperm.zip 11/nodataperm.zip
%elif "%{flavor}" == "11-libhoudini-zip" 
%build_waydroid_extra_from_file --name waydroid-11-libhoudini-zip --source https://github.com/supremegamers/vendor_intel_proprietary_houdini/archive/81f2a51ef539a35aead396ab7fce2adf89f46e88.zip libhoudini.zip 11/libhoudini.zip
%elif "%{flavor}" == "11-hide-status-bar-apk" 
%build_waydroid_extra_from_file --name waydroid-11-hide-status-bar-apk --source https://github.com/ayasa520/hide-status-bar/releases/download/v0.0.1/app-release.apk hidestatusbar.apk 11/hidestatusbar.apk
%elif "%{flavor}" == "smartdock-apk" 
%build_waydroid_extra_from_file --name waydroid-smartdock-apk --source https://f-droid.org/repo/cu.axel.smartdock_198.apk smartdock.apk
%elif "%{flavor}" == "x86_64-11-widevine-zip" 
%build_waydroid_extra_from_file --name waydroid-x86_64-11-widevine-zip --source https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/48d1076a570837be6cdce8252d5d143363e37cc1.zip widevine.zip 11/widevine.zip x86_64/11/widevine.zip
%elif "%{flavor}" == "x86_64-13-widevine-zip" 
%build_waydroid_extra_from_file --name waydroid-x86_64-13-widevine-zip --source https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/a8524d608431573ef1c9313822d271f78728f9a6.zip widevine.zip 13/widevine.zip x86_64/13/widevine.zip
%elif "%{flavor}" == "arm64-v8a-11-widevine-zip" 
%build_waydroid_extra_from_file --name waydroid-arm64-v8a-11-widevine-zip --source https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/a1a19361d36311bee042da8cf4ced798d2c76d98.zip widevine.zip 11/widevine.zip arm64-v8a/11/widevine.zip
%elif "%{flavor}" == "x86_64-11-OpenGapps-zip" 
%build_waydroid_extra_from_file --name waydroid-x86_64-11-OpenGapps-zip --source https://sourceforge.net/projects/opengapps/files/x86_64/20220503/open_gapps-x86_64-11.0-pico-20220503.zip gapps.zip 11/gapps.zip x86_64/11/gapps.zip
%elif "%{flavor}" == "x86-11-OpenGapps-zip" 
%build_waydroid_extra_from_file --name waydroid-x86-11-OpenGapps-zip --source https://sourceforge.net/projects/opengapps/files/x86/20220503/open_gapps-x86-11.0-pico-20220503.zip gapps.zip 11/gapps.zip x86/11/gapps.zip
%elif "%{flavor}" == "arm64-v8a-11-OpenGapps-zip" 
%build_waydroid_extra_from_file --name waydroid-arm64-v8a-11-OpenGapps-zip --source https://sourceforge.net/projects/opengapps/files/arm64/20220503/open_gapps-arm64-11.0-pico-20220503.zip gapps.zip 11/gapps.zip arm64-v8a/11/gapps.zip
%elif "%{flavor}" == "armeabi-v7a-11-OpenGapps-zip" 
%build_waydroid_extra_from_file --name waydroid-armeabi-v7a-11-OpenGapps-zip --source https://sourceforge.net/projects/opengapps/files/arm/20220215/open_gapps-arm-11.0-pico-20220215.zip gapps.zip 11/gapps.zip armeabi-v7a/11/gapps.zip
%elif "%{flavor}" == "x86_64-13-MindTheGapps-zip" 
%build_waydroid_extra_from_file --name waydroid-x86_64-13-MindTheGapps-zip --source https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-x86_64-20230323.zip gapps.zip 13/gapps.zip x86_64/13/gapps.zip
%elif "%{flavor}" == "x86-13-MindTheGapps-zip" 
%build_waydroid_extra_from_file --name waydroid-x86-13-MindTheGapps-zip --source https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-x86-20230323.zip gapps.zip 13/gapps.zip x86/13/gapps.zip
%elif "%{flavor}" == "arm64-v8a-13-MindTheGapps-zip" 
%build_waydroid_extra_from_file --name waydroid-arm64-v8a-13-MindTheGapps-zip --source https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-arm64-20230323.zip gapps.zip 13/gapps.zip arm64-v8a/13/gapps.zip
%elif "%{flavor}" == "armeabi-v7a-13-MindTheGapps-zip" 
%build_waydroid_extra_from_file --name waydroid-armeabi-v7a-13-MindTheGapps-zip --source https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-arm-20230323.zip gapps.zip 13/gapps.zip armeabi-v7a/13/gapps.zip
%elif "%{flavor}" == "MicroG-Standard-zip" 
%build_waydroid_extra_from_file --name waydroid-MicroG-Standard-zip --source https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-Standard-2.11.1-20230429100529.zip MicroG.zip MicroG_Standard.zip
%elif "%{flavor}" == "MicroG-NoGoolag-zip" 
%build_waydroid_extra_from_file --name waydroid-MicroG-NoGoolag-zip --source https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-NoGoolag-2.11.1-20230429100545.zip MicroG.zip MicroG_NoGoolag.zip
%elif "%{flavor}" == "MicroG-UNLP-zip" 
%build_waydroid_extra_from_file --name waydroid-MicroG-UNLP-zip --source https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-UNLP-2.11.1-20230429100555.zip MicroG.zip MicroG_UNLP.zip
%elif "%{flavor}" == "MicroG-Minimal-zip" 
%build_waydroid_extra_from_file --name waydroid-MicroG-Minimal-zip --source https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-Minimal-2.11.1-20230429100521.zip MicroG.zip MicroG_Minimal.zip
%elif "%{flavor}" == "MicroG-MinimalIAP-zip" 
%build_waydroid_extra_from_file --name waydroid-MicroG-MinimalIAP-zip --source https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-MinimalIAP-2.11.1-20230429100556.zip MicroG.zip MicroG_MinimalIAP.zip
%else
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

Name:           %{pypi_name}
Version:        0
Release:        1%{?dist}
Summary:        Script to add gapps and other stuff to waydroid!
License:        MIT
URL:            http://github.com/casualsnek/waydroid-script
Source0:        %{pypi_name}-%{pypi_version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Python Script to add OpenGapps, Magisk, libhoudini translation library and
libndk translation library to waydroid !

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

Requires: python3dist(tqdm)
Requires: python3dist(requests)
Requires: python3dist(InquirerPy)
Requires: python3dist(requests_file)


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

%endif
