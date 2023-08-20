BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
Version:    1
Release:    1
License:    LGPL

Name: waydroid-smartdock-apk
Source0: https://f-droid.org/repo/cu.axel.smartdock_198.apk
%build_waydroid_extra_from_file smartdock.apk
