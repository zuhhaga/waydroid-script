BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
Version:    1
Release:    1
License:    LGPL

Name: waydroid-x86_64-11-widevine-zip
Source0: https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/48d1076a570837be6cdce8252d5d143363e37cc1.zip
%build_waydroid_extra_from_file widevine.zip 11/widevine.zip x86_64/11/widevine.zip
