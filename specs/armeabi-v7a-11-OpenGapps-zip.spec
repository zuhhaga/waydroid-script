Name:  waydroid-armeabi-v7a-11-OpenGapps-zip 
Source0:  https://sourceforge.net/projects/opengapps/files/arm/20220215/open_gapps-arm-11.0-pico-20220215.zip 
BuildArch: noarch
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  gapps.zip gapps.11.zip gapps.11.armeabi-v7a.zip
