%_waydroid_require() Requires: waydroid(%{1})
%_waydroid_provide() Provides: waydroid(%{1})
%_waydroidextradir %{_datadir}/waydroid-extra

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
    
    
    if not rpm.isdefined('SUMMARY') then
       summary="Waydroid extra files"
       print([[Summary: ]] .. summary .. [[

%description
]] .. summary .. [[.
]])
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



Name: waydroid-MicroG-Standard-zip
Source0: https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-Standard-2.11.1-20230429100529.zip
%build_waydroid_extra_from_file MicroG.zip MicroG_Standard.zip
