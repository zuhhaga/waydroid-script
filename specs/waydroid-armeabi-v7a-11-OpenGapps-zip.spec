BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)

%_waydroid_name armeabi-v7a-11-OpenGapps-zip
Source0: https://sourceforge.net/projects/opengapps/files/arm/20220215/open_gapps-arm-11.0-pico-20220215.zip
%build_waydroid_extra_from_file gapps.zip 11/gapps.zip armeabi-v7a/11/gapps.zip
