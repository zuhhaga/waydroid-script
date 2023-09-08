Name:  waydroid-x86_64-11-nodataperm-zip 
Source0:  https://github.com/ayasa520/hack_full_data_permission/archive/d4beab7780eb792059d33e77d865579c9ee41546.zip 
BuildArch: noarch
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  nodataperm.zip nodataperm.11.zip nodataperm.11.x86_64.zip
