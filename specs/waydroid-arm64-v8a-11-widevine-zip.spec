BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
Version:    1
Release:    1
License:    LGPL

Name: waydroid-arm64-v8a-11-widevine-zip
Source0: https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/a1a19361d36311bee042da8cf4ced798d2c76d98.zip
%build_waydroid_extra_from_file widevine.zip 11/widevine.zip arm64-v8a/11/widevine.zip
