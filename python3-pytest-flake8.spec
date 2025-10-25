#
# Conditional build:
%bcond_without	tests	# py.test tests

Summary:	py.test plugin to check FLAKE8 requirements
Summary(pl.UTF-8):	Wtyczka py.test do sprawdzania wymagań FLAKE8
Name:		python3-pytest-flake8
Version:	1.3.0
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-flake8/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-flake8/pytest_flake8-%{version}.tar.gz
# Source0-md5:	0f8b276a4ff9955c23f77997652cb0db
URL:		https://github.com/tholo/pytest-flake8
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-flake8 >= 3.5
BuildRequires:	python3-pytest >= 3.5
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
py.test plugin for efficiently checking PEP8 compliance.

%description -l pl.UTF-8
Wtyczka py.test do efektywnego sprawdzania zgodności z PEP8.

%prep
%setup -q -n pytest_flake8-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTHONPATH=$(pwd) \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_flake8" \
%{__python3} -m pytest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst
%{py3_sitescriptdir}/pytest_flake8.py
%{py3_sitescriptdir}/__pycache__/pytest_flake8.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_flake8-%{version}.dist-info
