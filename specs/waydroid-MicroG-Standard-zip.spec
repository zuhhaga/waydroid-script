BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
Version:    1
Release:    1
License:    LGPL

Name: waydroid-MicroG-Standard-zip
Source0: https://github.com/ayasa520/MinMicroG/releases/download/latest/MinMicroG-Standard-2.11.1-20230429100529.zip
%build_waydroid_extra_from_file MicroG.zip MicroG_Standard.zip
