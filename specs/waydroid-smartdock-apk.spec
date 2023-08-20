Name: waydroid-smartdock-apk
Version: 1
Release: 1
License: LGPL
Summary: Waydroid extra files
Source0: https://f-droid.org/repo/cu.axel.smartdock_198.apk

%if %{undefined _waydroidextradir}
%define _waydroidextradir %{_datadir}/waydroid-extra
%endif

%if %{undefined _waydroid_unit}
%define _waydroid_unit() waydroid(%1)
%endif

%if %{undefined _waydroid_provide}
%define _waydroid_provide() Provides: %{_waydroid_unit %{1}}
%endif
    
%_waydroid_provide smartdock.apk

%description
%{summary}. 

%post
#!/bin/sh
echo post install "$1"
if [ "$1" == 1 ]; then
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/smartdock.apk' '%{_waydroid_unit smartdock.apk}' '%{_datadir}/%{name}/cu.axel.smartdock_198.apk' 25
fi
   
%postun
#!/bin/sh
echo post remove "$1"
if [ "$1" == 0 ]; then
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit smartdock.apk}' '%{_datadir}/%{name}/cu.axel.smartdock_198.apk' 25
fi

%files
%{_datadir}/%{name}/cu.axel.smartdock_198.apk
%dir %{_waydroidextradir}/

%install
mkdir -p '%{buildroot}%{_datadir}/%{name}'
cp '%{_sourcedir}/cu.axel.smartdock_198.apk' '%{buildroot}%{_datadir}/%{name}/cu.axel.smartdock_198.apk'
mkdir -p '%{buildroot}%{_waydroidextradir}/'
