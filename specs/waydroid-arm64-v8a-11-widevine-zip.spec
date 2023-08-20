Name: waydroid-arm64-v8a-11-widevine-zip
Version: 1
Release: 1
License: LGPL
Summary: Waydroid extra files
Source0: https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/a1a19361d36311bee042da8cf4ced798d2c76d98.zip

%if %{undefined _waydroidextradir}
%define _waydroidextradir %{_datadir}/waydroid-extra
%endif

%if %{undefined _waydroid_unit}
%define _waydroid_unit() waydroid(%1)
%endif

%if %{undefined _waydroid_provide}
%define _waydroid_provide() Provides: %{_waydroid_unit %{1}}
%endif
    
%_waydroid_provide widevine.zip
%_waydroid_provide 11/widevine.zip
%_waydroid_provide arm64-v8a/11/widevine.zip

%description
%{summary}. 

%post
#!/bin/sh
echo post install "$1"
if [ "$1" == 1 ]; then
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/widevine.zip' '%{_waydroid_unit widevine.zip}' '%{_datadir}/%{name}/a1a19361d36311bee042da8cf4ced798d2c76d98.zip' 25
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/11/widevine.zip' '%{_waydroid_unit 11/widevine.zip}' '%{_datadir}/%{name}/a1a19361d36311bee042da8cf4ced798d2c76d98.zip' 25
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/arm64-v8a/11/widevine.zip' '%{_waydroid_unit arm64-v8a/11/widevine.zip}' '%{_datadir}/%{name}/a1a19361d36311bee042da8cf4ced798d2c76d98.zip' 25
fi
   
%postun
#!/bin/sh
echo post remove "$1"
if [ "$1" == 0 ]; then
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit widevine.zip}' '%{_datadir}/%{name}/a1a19361d36311bee042da8cf4ced798d2c76d98.zip' 25
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit 11/widevine.zip}' '%{_datadir}/%{name}/a1a19361d36311bee042da8cf4ced798d2c76d98.zip' 25
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit arm64-v8a/11/widevine.zip}' '%{_datadir}/%{name}/a1a19361d36311bee042da8cf4ced798d2c76d98.zip' 25
fi

%files
%{_datadir}/%{name}/a1a19361d36311bee042da8cf4ced798d2c76d98.zip
%dir %{_waydroidextradir}/
%dir %{_waydroidextradir}/arm64-v8a/11
%dir %{_waydroidextradir}/arm64-v8a
%dir %{_waydroidextradir}/11

%install
mkdir -p '%{buildroot}%{_datadir}/%{name}'
cp '%{_sourcedir}/a1a19361d36311bee042da8cf4ced798d2c76d98.zip' '%{buildroot}%{_datadir}/%{name}/a1a19361d36311bee042da8cf4ced798d2c76d98.zip'
mkdir -p '%{buildroot}%{_waydroidextradir}/'
mkdir -p '%{buildroot}%{_waydroidextradir}/arm64-v8a/11'
mkdir -p '%{buildroot}%{_waydroidextradir}/arm64-v8a'
mkdir -p '%{buildroot}%{_waydroidextradir}/11'
