%define NAME name
%define VERSION 12

%lang_package

%_waydroid_name MicroG-Standard-zip
Source0: https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-Standard-2.11.1-20230429100529.zip
%build_waydroid_extra_from_file MicroG.zip MicroG_Standard.zip