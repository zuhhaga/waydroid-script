Name:  waydroid-arm64-v8a-13-MindTheGapps-zip 
Source0:  https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-arm64-20230323.zip 
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  gapps.zip 13/gapps.zip arm64-v8a/13/gapps.zip
