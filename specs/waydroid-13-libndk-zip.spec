%define NAME name
%define VERSION 12

%lang_package

%_waydroid_name 13-libndk-zip
Source0: https://github.com/supremegamers/vendor_google_proprietary_ndk_translation-prebuilt/archive/a090003c60df53a9eadb2df09bd4fd2fa86ea629.zip
%build_waydroid_extra_from_file libndktranslation.zip 13/libndktranslation.zip
