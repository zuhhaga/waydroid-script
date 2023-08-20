BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)

%_waydroid_name 11-libndk-zip
Source0: https://github.com/supremegamers/vendor_google_proprietary_ndk_translation-prebuilt/archive/9324a8914b649b885dad6f2bfd14a67e5d1520bf.zip
%build_waydroid_extra_from_file libndktranslation.zip 11/libndktranslation.zip
