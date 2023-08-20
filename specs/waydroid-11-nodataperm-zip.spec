BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
Version:    1
Release:    1
License:    LGPL

Name: waydroid-11-nodataperm-zip
Source0: https://github.com/ayasa520/hack_full_data_permission/archive/refs/heads/main.zip
%build_waydroid_extra_from_file nodataperm.zip 11/nodataperm.zip
