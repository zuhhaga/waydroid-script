Name:  waydroid-x86-11-OpenGapps-zip 
Source0:  https://sourceforge.net/projects/opengapps/files/x86/20220503/open_gapps-x86-11.0-pico-20220503.zip 
BuildArch: noarch
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  gapps.zip gapps.11.zip gapps.11.x86.zip
