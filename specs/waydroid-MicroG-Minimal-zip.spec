Name: waydroid-MicroG-Minimal-zip
Version: 1
Release: 1
License: LGPL
Summary: Waydroid extra files
Source0: https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-Minimal-2.11.1-20230429100521.zip

%if %{undefined _waydroidextradir}
%define _waydroidextradir %{_datadir}/waydroid-extra
%endif

%if %{undefined _waydroid_unit}
%define _waydroid_unit() waydroid(%1)
%endif

%if %{undefined _waydroid_provide}
%define _waydroid_provide() Provides: %{_waydroid_unit %{1}}
%endif
    
%_waydroid_provide MicroG.zip
%_waydroid_provide MicroG_Minimal.zip

%description
%{summary}. 

%post
#!/bin/sh
echo post install "$1"
if [ "$1" == 1 ]; then
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/MicroG.zip' '%{_waydroid_unit MicroG.zip}' '%{_datadir}/%{name}/MinMicroG-Minimal-2.11.1-20230429100521.zip' 25
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/MicroG_Minimal.zip' '%{_waydroid_unit MicroG_Minimal.zip}' '%{_datadir}/%{name}/MinMicroG-Minimal-2.11.1-20230429100521.zip' 25
fi
   
%postun
#!/bin/sh
echo post remove "$1"
if [ "$1" == 0 ]; then
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit MicroG.zip}' '%{_datadir}/%{name}/MinMicroG-Minimal-2.11.1-20230429100521.zip' 25
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit MicroG_Minimal.zip}' '%{_datadir}/%{name}/MinMicroG-Minimal-2.11.1-20230429100521.zip' 25
fi

%files
%{_datadir}/%{name}/MinMicroG-Minimal-2.11.1-20230429100521.zip
%dir %{_waydroidextradir}/

%install
mkdir -p '%{buildroot}%{_datadir}/%{name}'
cp '%{_sourcedir}/MinMicroG-Minimal-2.11.1-20230429100521.zip' '%{buildroot}%{_datadir}/%{name}/MinMicroG-Minimal-2.11.1-20230429100521.zip'
mkdir -p '%{buildroot}%{_waydroidextradir}/'
