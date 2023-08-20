BuildRequires: rpm_macro(_waydroid_name)
BuildRequires: rpm_macro(build_waydroid_extra_from_file)

%_waydroid_name 11-hide-status-bar-apk
Source0: https://github.com/ayasa520/hide-status-bar/releases/download/v0.0.1/app-release.apk
%build_waydroid_extra_from_file hidestatusbar.apk 11/hidestatusbar.apk
