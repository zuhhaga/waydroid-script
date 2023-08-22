Name:  waydroid-x86_64-11-widevine-zip 
Source0:  https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/48d1076a570837be6cdce8252d5d143363e37cc1.zip 
BuildArch: noarch
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  widevine.zip widevine.11.zip widevine.11.x86_64.zip
