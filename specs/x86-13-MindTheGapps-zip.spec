Name:  waydroid-x86-13-MindTheGapps-zip 
Source0:  https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-x86-20230323.zip 
BuildArch: noarch
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  gapps.zip gapps.13.zip gapps.13.x86.zip
