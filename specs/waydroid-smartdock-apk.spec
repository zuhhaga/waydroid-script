%define NAME name
%define VERSION 12

%lang_package

%_waydroid_name smartdock-apk
Source0: https://f-droid.org/repo/cu.axel.smartdock_198.apk
%build_waydroid_extra_from_file smartdock.apk
