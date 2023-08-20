Name: waydroid-x86-13-MindTheGapps-zip
Version: 1
Release: 1
License: LGPL
Summary: Waydroid extra files
Source0: https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-x86-20230323.zip

%if %{undefined _waydroidextradir}
%define _waydroidextradir %{_datadir}/waydroid-extra
%endif

%if %{undefined _waydroid_unit}
%define _waydroid_unit() waydroid(%1)
%endif

%if %{undefined _waydroid_provide}
%define _waydroid_provide() Provides: %{_waydroid_unit %{1}}
%endif
    
%_waydroid_provide gapps.zip
%_waydroid_provide 13/gapps.zip
%_waydroid_provide x86/13/gapps.zip

%description
%{summary}. 

%post
#!/bin/sh
echo post install "$1"
if [ "$1" == 1 ]; then
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/gapps.zip' '%{_waydroid_unit gapps.zip}' '%{_datadir}/%{name}/MindTheGapps-13.0.0-x86-20230323.zip' 25
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/13/gapps.zip' '%{_waydroid_unit 13/gapps.zip}' '%{_datadir}/%{name}/MindTheGapps-13.0.0-x86-20230323.zip' 25
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/x86/13/gapps.zip' '%{_waydroid_unit x86/13/gapps.zip}' '%{_datadir}/%{name}/MindTheGapps-13.0.0-x86-20230323.zip' 25
fi
   
%postun
#!/bin/sh
echo post remove "$1"
if [ "$1" == 0 ]; then
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit gapps.zip}' '%{_datadir}/%{name}/MindTheGapps-13.0.0-x86-20230323.zip' 25
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit 13/gapps.zip}' '%{_datadir}/%{name}/MindTheGapps-13.0.0-x86-20230323.zip' 25
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit x86/13/gapps.zip}' '%{_datadir}/%{name}/MindTheGapps-13.0.0-x86-20230323.zip' 25
fi

%files
%{_datadir}/%{name}/MindTheGapps-13.0.0-x86-20230323.zip
%dir %{_waydroidextradir}/
%dir %{_waydroidextradir}/x86
%dir %{_waydroidextradir}/13
%dir %{_waydroidextradir}/x86/13

%install
mkdir -p '%{buildroot}%{_datadir}/%{name}'
cp '%{_sourcedir}/MindTheGapps-13.0.0-x86-20230323.zip' '%{buildroot}%{_datadir}/%{name}/MindTheGapps-13.0.0-x86-20230323.zip'
mkdir -p '%{buildroot}%{_waydroidextradir}/'
mkdir -p '%{buildroot}%{_waydroidextradir}/x86'
mkdir -p '%{buildroot}%{_waydroidextradir}/13'
mkdir -p '%{buildroot}%{_waydroidextradir}/x86/13'
