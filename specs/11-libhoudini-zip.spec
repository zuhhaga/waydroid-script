Name:  waydroid-11-libhoudini-zip 
 Source0:  https://github.com/supremegamers/vendor_intel_proprietary_houdini/archive/81f2a51ef539a35aead396ab7fce2adf89f46e88.zip 
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
 %build_waydroid_extra_from_file --dscr yes  libhoudini.zip 11/libhoudini.zip
