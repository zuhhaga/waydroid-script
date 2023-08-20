# required macros: NAME, SOURCE0, provisions
%define build_waydroid_extra_from_file() %{lua:
    
    if not rpm.isdefined('SOURCE0') then
       error('SOURCE0 is not defined')
    end
    
    if not rpm.isdefined('NAME') then
       error('NAME is not defined')
    end
    
    if not rpm.isdefined('LICENSE') then
       print([[License: LGPL
]]) 
    end
    
    if not rpm.isdefined('VERSION') then
       print([[Version: 1
]])
       rpm.define('VERSION 1')
    end
    
    if not rpm.isdefined('RELEASE') then
       print([[Release: 1
]])
       rpm.define('RELEASE 1')
    end
 
    if not rpm.isdefined('SUMMARY') then
       summary="Waydroid extra files"
       print([[Summary: ]] .. summary .. [[

%description
]] .. summary .. [[.
]])
    end
 
    _source_url=rpm.expand('%{SOURCE0}')
    _file=_source_url:match("^.*/(.*)$")
    
    nw=string.char(10)
    name = rpm.expand('%{NAME}')
    
    file=rpm.expand('%{_datadir}/%{NAME}/') .. _file
    
    dirstr=rpm.expand('%{_waydroidextradir}/')
    
    post=''
    postun=''
    dirs={}
    
    tokens_len=#arg
    
    i = 0
    
    while i < tokens_len do
       i = i + 1
       token=arg[i]
       dir=token:match("(.*/)") or ''
       dirs[dir] = 1
       print(rpm.expand('%_waydroid_provide ' .. token .. nw))
    end
    
    print(nw)
    
    print([[%post
#!/bin/sh
echo post install "$1"
if [ "$1" == 1 ]; then
]])
    i = 0
    
    while i < tokens_len do
      i = i + 1
      token = arg[i]
      print(rpm.expand("%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/"..token.."' 'waydroid("..token..")' '"..file.."' 25"..nw))
    end
    
    print('fi')
    print(nw)
    print(nw)
    
    print([[%postun
#!/bin/sh
echo post remove "$1"
if [ "$1" == 0 ]; then
]])
    i = 0

    while i < tokens_len do
      i = i + 1
      token = arg[i]
      print(rpm.expand("%{_sbindir}/update-alternatives --remove 'waydroid("..token..")' '"..file.."' 25"..nw))
    end
    
    print('fi')
    
    print(nw)
    print(nw)
    print('%files')
    print(nw)
    print(file)
    for key, value in pairs(dirs) do
      print(nw)
      print('%dir ')
      print(dirstr)
      print(key)
    end
    print(nw)
    print(rpm.expand([[
    
%%install 
mkdir -p '%{buildroot}%{_datadir}/%{NAME}'
cp '%{_sourcedir}/]] .. _file .. [[' '%{buildroot}]] .. file .. [['
    ]]))
    buildroot=rpm.expand('%{buildroot}')
    
    for key, value in pairs(dirs) do
      print(nw)
      print("mkdir -p '")
      print(buildroot)
      print(dirstr)
      print(key)
      print("'")
    end
    
}


BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
Version:    1
Release:    1
License:    LGPL

Name: waydroid-11-libndk-zip
Source0: https://github.com/supremegamers/vendor_google_proprietary_ndk_translation-prebuilt/archive/9324a8914b649b885dad6f2bfd14a67e5d1520bf.zip
%build_waydroid_extra_from_file libndktranslation.zip 11/libndktranslation.zip
