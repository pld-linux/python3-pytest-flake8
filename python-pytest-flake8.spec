#
# Conditional build:
%bcond_without	tests	# py.test tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	py.test plugin to check FLAKE8 requirements
Summary(pl.UTF-8):	Wtyczka py.test do sprawdzania wymagań FLAKE8
Name:		python-pytest-flake8
Version:	1.0.4
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-flake8/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-flake8/pytest-flake8-%{version}.tar.gz
# Source0-md5:	a6fcb6ceb01a2bc06c005f6cc7f70fe5
URL:		https://github.com/tholo/pytest-flake8
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-flake8 >= 3.5
BuildRequires:	python-pytest >= 3.5
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-flake8 >= 3.5
BuildRequires:	python3-pytest >= 3.5
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
py.test plugin for efficiently checking PEP8 compliance.

%description -l pl.UTF-8
Wtyczka py.test do efektywnego sprawdzania zgodności z PEP8.

%package -n python3-pytest-flake8
Summary:	py.test plugin to check FLAKE8 requirements
Summary(pl.UTF-8):	Wtyczka py.test do sprawdzania wymagań FLAKE8
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pytest-flake8
py.test plugin for efficiently checking PEP8 compliance.

%description -n python3-pytest-flake8 -l pl.UTF-8
Wtyczka py.test do efektywnego sprawdzania zgodności z PEP8.

%prep
%setup -q -n pytest-flake8-%{version}

%build
%if %{with python2}
%py_build

%{?with_tests:PYTHONPATH=$(pwd) %{__python} -m pytest}
%endif

%if %{with python3}
%py3_build

%{?with_tests:PYTHONPATH=$(pwd) %{__python3} -m pytest}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.rst
%{py_sitescriptdir}/pytest_flake8.py[co]
%{py_sitescriptdir}/pytest_flake8-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-flake8
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.rst
%{py3_sitescriptdir}/pytest_flake8.py
%{py3_sitescriptdir}/__pycache__/pytest_flake8.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_flake8-%{version}-py*.egg-info
%endif
