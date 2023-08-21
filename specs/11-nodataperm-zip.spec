Name:  waydroid-11-nodataperm-zip 
Source0:  https://github.com/ayasa520/hack_full_data_permission/archive/refs/heads/main.zip 
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  nodataperm.zip 11/nodataperm.zip
