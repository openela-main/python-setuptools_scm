%bcond_without python3

%global srcname setuptools_scm

Name:           python-%{srcname}
Version:        1.15.7
Release:        6%{?dist}
Summary:        Blessed package to manage your versions by scm tags

# https://github.com/pypa/setuptools_scm/issues/211
License:        MIT
URL:            https://pypi.python.org/pypi/setuptools_scm
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{srcname}; echo ${n:0:1})/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.

%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.

%if %{with python3}
%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}
Obsoletes:      platform-python-%{srcname} < %{version}-%{release}

%description -n python3-%{srcname}
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.

%endif

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%if %{with python3}
%py3_build
%endif

%install
%py2_install
%if %{with python3}
%py3_install
%endif

#%%check
# Tests are not shipped in PyPI tarball and requires git and mercurial
# which means that we'd have to depends on mercurial module which is
# too heavy dependency for tests of one package not included in module API

%files -n python2-%{srcname}
#license LICENSE
%doc README.rst
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}-*.egg-info/

%if %{with python3}
%files -n python3-%{srcname}
#license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info
%endif

%changelog
* Thu Apr 25 2019 Tomas Orsava <torsava@redhat.com> - 1.15.7-6
- Bumping due to problems with modular RPM upgrade path
- Resolves: rhbz#1695587

* Tue Jul 31 2018 Lumír Balhar <lbalhar@redhat.com> - 1.15.7-5
- Make possible to disable python3 subpackage

* Wed Jul 18 2018 Lumír Balhar <lbalhar@redhat.com> - 1.15.7-5
- First version for python27 module
