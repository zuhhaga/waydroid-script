Name:  waydroid-11-hide-status-bar-apk 
Source0:  https://github.com/ayasa520/hide-status-bar/releases/download/v0.0.2/app-release.apk 
BuildArch: noarch
BuildRequires: rpm_macro(build_waydroid_extra_from_file)
%build_waydroid_extra_from_file --dscr yes  hidestatusbar.apk hidestatusbar.11.apk
