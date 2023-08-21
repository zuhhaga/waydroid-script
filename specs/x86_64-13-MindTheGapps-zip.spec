Name:  waydroid-x86_64-13-MindTheGapps-zip 
Source0:  https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-x86_64-20230323.zip 
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  gapps.zip 13/gapps.zip x86_64/13/gapps.zip
