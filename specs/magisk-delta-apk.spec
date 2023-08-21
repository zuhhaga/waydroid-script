Name:  waydroid-magisk-delta-apk 
Source0:  https://huskydg.github.io/magisk-files/app-debug.apk 
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  magisk.apk
