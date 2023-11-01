%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

# Tests are not included in PyPI tarball
%bcond_with tests

%global srcname setuptools_scm

Name:           python-%{srcname}
Version:        1.15.7
Release:        4%{?dist}
Summary:        Blessed package to manage your versions by scm tags

# https://github.com/pypa/setuptools_scm/issues/211
License:        MIT
URL:            https://pypi.python.org/pypi/setuptools_scm
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{srcname}; echo ${n:0:1})/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%if %{with tests}
BuildRequires:  git-core
BuildRequires:  mercurial
%endif

%description
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with tests}
BuildRequires:  python2-pytest
%endif
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.
%endif # with python2

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
%endif
%{?python_provide:%python_provide python3-%{srcname}}
Obsoletes:      platform-python-%{srcname} < %{version}-%{release}

%description -n python3-%{srcname}
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.

%prep
%autosetup -n %{srcname}-%{version}

%build
%if %{with python2}
%py2_build
%endif # with python2
%py3_build

%install
%if %{with python2}
%py2_install
%endif # with python2
%py3_install

%if %{with tests}
%check
%if %{with python2}
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -vv
%endif # with python2
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -vv
%endif

%if %{with python2}
%files -n python2-%{srcname}
#license LICENSE
%doc README.rst
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}-*.egg-info/
%endif # with python2

%files -n python3-%{srcname}
#license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info

%changelog
* Tue Jul 17 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.15.7-4
- Conditionalize the python2 subpackage

* Mon Jun 25 2018 Petr Viktorin <pviktori@redhat.com> - 1.15.7-3
- Allow Python 2 for build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.15.7-1
- Update to 1.15.7

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.15.6-7
- Use better Obsoletes for platform-python

* Fri Nov 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.15.6-6
- Remove platform-python subpackage

* Thu Aug 24 2017 Miro Hrončok <mhroncok@redhat.com> - 1.15.6-5
- Rebuilt for rhbz#1484607

* Sun Aug 20 2017 Tomas Orsava <torsava@redhat.com> - 1.15.6-4
- Re-enable tests to finish bootstrapping the platform-python stack
  (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Thu Aug 10 2017 Lumír Balhar <lbalhar@redhat.com> - 1.15.6-3
- Add subpackage for platform-python
- Disable tests so platform-python stack can be bootstrapped
  (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Orion Poplawski <orion@cora.nwra.com> - 1.15.6-1
- Update to 1.15.6

* Mon Apr 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.15.5-1
- Update to 1.15.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Kevin Fenzi <kevin@scrye.com> - 1.15.0-1
- Update to 1.15.0

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.13.0-2
- Rebuild for Python 3.6

* Mon Oct 10 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.13.0-1
- Update to 1.13.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 4 2016 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-2
- No python2 package on EPEL (setuptools too old)

* Thu Dec 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-1
- Update to 1.10.1

* Wed Dec 2 2015 Orion Poplawski <orion@cora.nwra.com> - 1.9.0-1
- Update to 1.9.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-2
- Cleanup stray .pyc files from tests

* Sat Sep 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-1
- Update to 1.8.0
- Fix license tag

* Mon Sep 14 2015 Orion Poplawski <orion@cora.nwra.com> - 1.7.0-1
- Initial package
