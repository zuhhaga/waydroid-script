BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
Version:    1
Release:    1
License:    LGPL

Name: waydroid-x86-11-OpenGapps-zip
Source0: https://sourceforge.net/projects/opengapps/files/x86/20220503/open_gapps-x86-11.0-pico-20220503.zip
%build_waydroid_extra_from_file gapps.zip 11/gapps.zip x86/11/gapps.zip
