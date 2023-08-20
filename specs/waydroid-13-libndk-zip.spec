Name: waydroid-13-libndk-zip
Version: 1
Release: 1
License: LGPL
Summary: Waydroid extra files
Source0: https://github.com/supremegamers/vendor_google_proprietary_ndk_translation-prebuilt/archive/a090003c60df53a9eadb2df09bd4fd2fa86ea629.zip

%if %{undefined _waydroidextradir}
%define _waydroidextradir %{_datadir}/waydroid-extra
%endif

%if %{undefined _waydroid_unit}
%define _waydroid_unit() waydroid(%1)
%endif

%if %{undefined _waydroid_provide}
%define _waydroid_provide() Provides: %{_waydroid_unit %{1}}
%endif
    
%_waydroid_provide libndktranslation.zip
%_waydroid_provide 13/libndktranslation.zip

%description
%{summary}. 

%post
#!/bin/sh
echo post install "$1"
if [ "$1" == 1 ]; then
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/libndktranslation.zip' '%{_waydroid_unit libndktranslation.zip}' '%{_datadir}/%{name}/a090003c60df53a9eadb2df09bd4fd2fa86ea629.zip' 25
%{_sbindir}/update-alternatives --install '%{_waydroidextradir}/13/libndktranslation.zip' '%{_waydroid_unit 13/libndktranslation.zip}' '%{_datadir}/%{name}/a090003c60df53a9eadb2df09bd4fd2fa86ea629.zip' 25
fi
   
%postun
#!/bin/sh
echo post remove "$1"
if [ "$1" == 0 ]; then
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit libndktranslation.zip}' '%{_datadir}/%{name}/a090003c60df53a9eadb2df09bd4fd2fa86ea629.zip' 25
%{_sbindir}/update-alternatives --remove '%{_waydroid_unit 13/libndktranslation.zip}' '%{_datadir}/%{name}/a090003c60df53a9eadb2df09bd4fd2fa86ea629.zip' 25
fi

%files
%{_datadir}/%{name}/a090003c60df53a9eadb2df09bd4fd2fa86ea629.zip
%dir %{_waydroidextradir}/
%dir %{_waydroidextradir}/13

%install
mkdir -p '%{buildroot}%{_datadir}/%{name}'
cp '%{_sourcedir}/a090003c60df53a9eadb2df09bd4fd2fa86ea629.zip' '%{buildroot}%{_datadir}/%{name}/a090003c60df53a9eadb2df09bd4fd2fa86ea629.zip'
mkdir -p '%{buildroot}%{_waydroidextradir}/'
mkdir -p '%{buildroot}%{_waydroidextradir}/13'
