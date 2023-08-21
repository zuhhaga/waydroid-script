Name:  waydroid-MicroG-UNLP-zip 
Source0:  https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-UNLP-2.11.1-20230429100555.zip 
BuildArch: noarch
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  MicroG.zip MicroG_UNLP.zip
