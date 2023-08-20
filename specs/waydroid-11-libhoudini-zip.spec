Name: waydroid-11-libhoudini-zip
Version: 1
Release: 1
License: LGPL
Summary: Waydroid extra files
Source0: https://github.com/supremegamers/vendor_intel_proprietary_houdini/archive/81f2a51ef539a35aead396ab7fce2adf89f46e88.zip

%if %{undefined _waydroidextradir}
%define _waydroidextradir %{_datadir}/waydroid-extra
%endif

%if %{undefined _waydroid_unit}
%define _waydroid_unit() waydroid(%1)
%endif

%if %{undefined _waydroid_provide}
%define _waydroid_provide() Provides: %{_waydroid_unit %{1}}
%endif
    
%_waydroid_provide libhoudini.zip
%_waydroid_provide 11/libhoudini.zip

%description
%{summary}. 

%post
#!/bin/sh
echo post install "$1"
if [ "$1" == 1 ]; then
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/libhoudini.zip' '%{_waydroid_unit libhoudini.zip}' '%{_datadir}/%{name}/81f2a51ef539a35aead396ab7fce2adf89f46e88.zip' 25
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/11/libhoudini.zip' '%{_waydroid_unit 11/libhoudini.zip}' '%{_datadir}/%{name}/81f2a51ef539a35aead396ab7fce2adf89f46e88.zip' 25
fi
   
%postun
#!/bin/sh
echo post remove "$1"
if [ "$1" == 0 ]; then
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit libhoudini.zip}' '%{_datadir}/%{name}/81f2a51ef539a35aead396ab7fce2adf89f46e88.zip' 25
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit 11/libhoudini.zip}' '%{_datadir}/%{name}/81f2a51ef539a35aead396ab7fce2adf89f46e88.zip' 25
fi

%files
%{_datadir}/%{name}/81f2a51ef539a35aead396ab7fce2adf89f46e88.zip
%dir %{_waydroidextradir}/
%dir %{_waydroidextradir}/11

%install
mkdir -p '%{buildroot}%{_datadir}/%{name}'
cp '%{_sourcedir}/81f2a51ef539a35aead396ab7fce2adf89f46e88.zip' '%{buildroot}%{_datadir}/%{name}/81f2a51ef539a35aead396ab7fce2adf89f46e88.zip'
mkdir -p '%{buildroot}%{_waydroidextradir}/'
mkdir -p '%{buildroot}%{_waydroidextradir}/11'
