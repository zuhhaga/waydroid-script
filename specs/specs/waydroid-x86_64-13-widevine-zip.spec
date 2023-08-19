%define NAME name
%define VERSION 12

%lang_package

%_waydroid_name x86_64-13-widevine-zip
Source0: https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/a8524d608431573ef1c9313822d271f78728f9a6.zip
%build_waydroid_extra_from_file widevine.zip 13/widevine.zip x86_64/13/widevine.zip
