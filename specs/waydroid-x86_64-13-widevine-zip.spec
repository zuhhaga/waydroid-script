Name: waydroid-x86_64-13-widevine-zip
Version: 1
Release: 1
License: LGPL
Summary: Waydroid extra files
Source0: https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/a8524d608431573ef1c9313822d271f78728f9a6.zip

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
%_waydroid_provide 13/widevine.zip
%_waydroid_provide x86_64/13/widevine.zip

%description
%{summary}. 

%post
#!/bin/sh
echo post install "$1"
if [ "$1" == 1 ]; then
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/widevine.zip' '%{_waydroid_unit widevine.zip}' '%{_datadir}/%{name}/a8524d608431573ef1c9313822d271f78728f9a6.zip' 25
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/13/widevine.zip' '%{_waydroid_unit 13/widevine.zip}' '%{_datadir}/%{name}/a8524d608431573ef1c9313822d271f78728f9a6.zip' 25
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/x86_64/13/widevine.zip' '%{_waydroid_unit x86_64/13/widevine.zip}' '%{_datadir}/%{name}/a8524d608431573ef1c9313822d271f78728f9a6.zip' 25
fi
   
%postun
#!/bin/sh
echo post remove "$1"
if [ "$1" == 0 ]; then
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit widevine.zip}' '%{_datadir}/%{name}/a8524d608431573ef1c9313822d271f78728f9a6.zip' 25
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit 13/widevine.zip}' '%{_datadir}/%{name}/a8524d608431573ef1c9313822d271f78728f9a6.zip' 25
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit x86_64/13/widevine.zip}' '%{_datadir}/%{name}/a8524d608431573ef1c9313822d271f78728f9a6.zip' 25
fi

%files
%{_datadir}/%{name}/a8524d608431573ef1c9313822d271f78728f9a6.zip
%dir %{_waydroidextradir}/
%dir %{_waydroidextradir}/x86_64
%dir %{_waydroidextradir}/x86_64/13
%dir %{_waydroidextradir}/13

%install
mkdir -p '%{buildroot}%{_datadir}/%{name}'
cp '%{_sourcedir}/a8524d608431573ef1c9313822d271f78728f9a6.zip' '%{buildroot}%{_datadir}/%{name}/a8524d608431573ef1c9313822d271f78728f9a6.zip'
mkdir -p '%{buildroot}%{_waydroidextradir}/'
mkdir -p '%{buildroot}%{_waydroidextradir}/x86_64'
mkdir -p '%{buildroot}%{_waydroidextradir}/x86_64/13'
mkdir -p '%{buildroot}%{_waydroidextradir}/13'
