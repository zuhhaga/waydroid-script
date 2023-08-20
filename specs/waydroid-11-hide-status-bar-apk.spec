Name: waydroid-11-hide-status-bar-apk
Version: 1
Release: 1
License: LGPL
Summary: Waydroid extra files
Source0: https://github.com/ayasa520/hide-status-bar/releases/download/v0.0.1/app-release.apk

%if %{undefined _waydroidextradir}
%define _waydroidextradir %{_datadir}/waydroid-extra
%endif

%if %{undefined _waydroid_unit}
%define _waydroid_unit() waydroid(%1)
%endif

%if %{undefined _waydroid_provide}
%define _waydroid_provide() Provides: %{_waydroid_unit %{1}}
%endif
    
%_waydroid_provide hidestatusbar.apk
%_waydroid_provide 11/hidestatusbar.apk

%description
%{summary}. 

%post
#!/bin/sh
echo post install "$1"
if [ "$1" == 1 ]; then
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/hidestatusbar.apk' '%{_waydroid_unit hidestatusbar.apk}' '%{_datadir}/%{name}/app-release.apk' 25
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/11/hidestatusbar.apk' '%{_waydroid_unit 11/hidestatusbar.apk}' '%{_datadir}/%{name}/app-release.apk' 25
fi
   
%postun
#!/bin/sh
echo post remove "$1"
if [ "$1" == 0 ]; then
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit hidestatusbar.apk}' '%{_datadir}/%{name}/app-release.apk' 25
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit 11/hidestatusbar.apk}' '%{_datadir}/%{name}/app-release.apk' 25
fi

%files
%{_datadir}/%{name}/app-release.apk
%dir %{_waydroidextradir}/
%dir %{_waydroidextradir}/11

%install
mkdir -p '%{buildroot}%{_datadir}/%{name}'
cp '%{_sourcedir}/app-release.apk' '%{buildroot}%{_datadir}/%{name}/app-release.apk'
mkdir -p '%{buildroot}%{_waydroidextradir}/'
mkdir -p '%{buildroot}%{_waydroidextradir}/11'
