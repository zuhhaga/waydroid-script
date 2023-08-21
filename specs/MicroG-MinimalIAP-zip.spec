Name:  waydroid-MicroG-MinimalIAP-zip 
Source0:  https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-MinimalIAP-2.11.1-20230429100556.zip 
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  MicroG.zip MicroG_MinimalIAP.zip
