BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)

%_waydroid_name armeabi-v7a-13-MindTheGapps-zip
Source0: https://github.com/Howard20181/MindTheGappsBuilder/releases/download/20230323/MindTheGapps-13.0.0-arm-20230323.zip
%build_waydroid_extra_from_file gapps.zip 13/gapps.zip armeabi-v7a/13/gapps.zip
