%define pypi_name waydroid_script
%define pypi_version main

Name:           python-%{pypi_name}
Version:        0
Release:        1%{?dist}
Summary:        Script to add gapps and other stuff to waydroid!

License:        MIT
URL:            http://github.com/casualsnek/waydroid-script
Source0:        %{pypi_name}-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Python Script to add OpenGapps, Magisk, libhoudini translation library and
libndk translation library to waydroid !

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides: waydroid-script
Requires: lzip

Requires:       python3dist(tqdm)
Requires:       python3dist(requests)
Requires:       python3dist(InquirerPy)
Requires:       python3dist(requests_file)

%description -n python3-%{pypi_name}
Python Script to add OpenGapps, Magisk, libhoudini translation library and
libndk translation library to waydroid !


%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/waydroid-script
%{python3_sitelib}/**/*
%dir %{python3_sitelib}/*

%changelog
* Sat Aug 19 2023 lenovo - 0.~~dev0-1
- Initial package.
