%define NAME name
%define VERSION 12

%lang_package

%_waydroid_name MicroG-MinimalIAP-zip
Source0: https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-MinimalIAP-2.11.1-20230429100556.zipcc071f4f776cbc16c4c1f707aff1f7fa
%build_waydroid_extra_from_file MicroG.zip MicroG_MinimalIAP.zip
