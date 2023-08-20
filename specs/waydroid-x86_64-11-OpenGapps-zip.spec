BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)

%_waydroid_name x86_64-11-OpenGapps-zip
Source0: https://sourceforge.net/projects/opengapps/files/x86_64/20220503/open_gapps-x86_64-11.0-pico-20220503.zip
%build_waydroid_extra_from_file gapps.zip 11/gapps.zip x86_64/11/gapps.zip
