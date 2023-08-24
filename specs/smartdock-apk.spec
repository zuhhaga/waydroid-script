Name:  waydroid-smartdock-apk 
Source0:  https://f-droid.org/repo/cu.axel.smartdock_1100.apk 
BuildArch: noarch
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  smartdock.apk
