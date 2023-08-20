Name: waydroid-11-nodataperm-zip
Version: 1
Release: 1
License: LGPL
Summary: Waydroid extra files
Source0: https://github.com/ayasa520/hack_full_data_permission/archive/refs/heads/main.zip

%if %{undefined _waydroidextradir}
%define _waydroidextradir %{_datadir}/waydroid-extra
%endif

%if %{undefined _waydroid_unit}
%define _waydroid_unit() waydroid(%1)
%endif

%if %{undefined _waydroid_provide}
%define _waydroid_provide() Provides: %{_waydroid_unit %{1}}
%endif
    
%_waydroid_provide nodataperm.zip
%_waydroid_provide 11/nodataperm.zip

%description
%{summary}. 

%post
#!/bin/sh
echo post install "$1"
if [ "$1" == 1 ]; then
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/nodataperm.zip' '%{_waydroid_unit nodataperm.zip}' '%{_datadir}/%{name}/main.zip' 25
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/11/nodataperm.zip' '%{_waydroid_unit 11/nodataperm.zip}' '%{_datadir}/%{name}/main.zip' 25
fi
   
%postun
#!/bin/sh
echo post remove "$1"
if [ "$1" == 0 ]; then
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit nodataperm.zip}' '%{_datadir}/%{name}/main.zip' 25
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit 11/nodataperm.zip}' '%{_datadir}/%{name}/main.zip' 25
fi

%files
%{_datadir}/%{name}/main.zip
%dir %{_waydroidextradir}/
%dir %{_waydroidextradir}/11

%install
mkdir -p '%{buildroot}%{_datadir}/%{name}'
cp '%{_sourcedir}/main.zip' '%{buildroot}%{_datadir}/%{name}/main.zip'
mkdir -p '%{buildroot}%{_waydroidextradir}/'
mkdir -p '%{buildroot}%{_waydroidextradir}/11'
