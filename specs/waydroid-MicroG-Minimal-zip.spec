%define NAME name
%define VERSION 12

%lang_package

%_waydroid_name MicroG-Minimal-zip
Source0: https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-Minimal-2.11.1-20230429100521.zip
%build_waydroid_extra_from_file MicroG.zip MicroG_Minimal.zip
