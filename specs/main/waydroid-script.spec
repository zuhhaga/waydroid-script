%define pypi_name waydroid_script
%define pypi_version main

%ifarch %{arm} 
%define wayarch armeabi-v7a 
%endif

%ifarch %{arm64} aarch64 
%define wayarch arm64-v8a 
%endif

%ifarch %{x86_64} x86_64 amd64
%define wayarch x86_64
%endif

%ifarch %{ix86} 
%define wayarch x86
%endif

Name:           %{pypi_name}
Version:        0
Release:        1%{?dist}
Summary:        Script to add gapps and other stuff to waydroid!
License:        MIT
URL:            http://github.com/casualsnek/waydroid-script
Source0:        %{pypi_name}-%{pypi_version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Python Script to add OpenGapps, Magisk, libhoudini translation library and
libndk translation library to waydroid !

%package -n     waydroid-script-binary-%{wayarch}
Summary: Binaries for waydroid-script package

%description -n waydroid-script-binary-%{wayarch}
Binaries for waydroid-script package.

%package -n    waydroid-script
Summary:        %{summary}
BuildArch: noarch
Requires:     python3-%{pypi_name}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildArch: noarch
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires: lzip
Requires: waydroid-script-binary-%{wayarch}

Requires:       python3dist(tqdm)
Requires:       python3dist(requests)
Requires:       python3dist(InquirerPy)
Requires:       python3dist(requests_file)


%description -n waydroid-script
Python Script to add OpenGapps, Magisk, libhoudini translation library and
libndk translation library to waydroid !

%description -n python3-%{pypi_name}
Python Script to add OpenGapps, Magisk, libhoudini translation library and
libndk translation library to waydroid !

%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%build
%py3_build
%define  pypi_libdir    %{_usr}/lib/%{pypi_name}
%define  pypi_bindir  %{pypi_libdir}/bin
%define  pypi_oldbindir  %{python3_sitelib}/%{pypi_name}/bin

%install
%py3_install
mkdir -p %{buildroot}%{pypi_bindir}/%{wayarch}/
mv   %{buildroot}%{pypi_oldbindir}/%{wayarch}/resetprop    %{buildroot}%{pypi_bindir}/%{wayarch}/resetprop
rm -R %{buildroot}%{pypi_oldbindir}
ln -s %{pypi_bindir}   %{buildroot}%{pypi_oldbindir}


%files -n waydroid-script-binary-%{wayarch}
%{pypi_bindir}/%{wayarch}/resetprop 
%dir %{pypi_bindir}/%{wayarch}/
%dir %{pypi_bindir}/
%dir %{pypi_libdir}/

%files -n waydroid-script
%{_bindir}/waydroid-script

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/**/*
%dir %{python3_sitelib}/*

%changelog
* Sat Aug 19 2023 lenovo - 0.~~dev0-1
- Initial package.
