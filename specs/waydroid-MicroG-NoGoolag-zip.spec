BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)

%_waydroid_name MicroG-NoGoolag-zip
Source0: https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-NoGoolag-2.11.1-20230429100545.zip
%build_waydroid_extra_from_file MicroG.zip MicroG_NoGoolag.zip
