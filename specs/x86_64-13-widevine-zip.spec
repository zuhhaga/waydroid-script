Name:  waydroid-x86_64-13-widevine-zip 
Source0:  https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/a8524d608431573ef1c9313822d271f78728f9a6.zip 
BuildArch: noarch
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  widevine.zip widevine.13.zip widevine.13.x86_64.zip
