BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
Version:    1
Release:    1
License:    LGPL

Name: waydroid-MicroG-Minimal-zip
Source0: https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-Minimal-2.11.1-20230429100521.zip
%build_waydroid_extra_from_file MicroG.zip MicroG_Minimal.zip
