#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Diff JSON and JSON-like structures in Python
Summary(pl.UTF-8):	Porównywanie JSON-a i struktur w stylu JSON-a w Pythonie
Name:		python-jsondiff
Version:	1.2.0
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jsondiff/
Source0:	https://files.pythonhosted.org/packages/source/j/jsondiff/jsondiff-%{version}.tar.gz
# Source0-md5:	d48297d9253356b7f71e38268e7e0d10
URL:		https://pypi.org/project/jsondiff/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose_random
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose_random
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diff JSON and JSON-like structures in Python.

%description -l pl.UTF-8
Porównywanie JSON-a i struktur w stylu JSON-a w Pythonie.

%package -n python3-jsondiff
Summary:	Diff JSON and JSON-like structures in Python
Summary(pl.UTF-8):	Porównywanie JSON-a i struktur w stylu JSON-a w Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-jsondiff
Diff JSON and JSON-like structures in Python.

%description -n python3-jsondiff -l pl.UTF-8
Porównywanie JSON-a i struktur w stylu JSON-a w Pythonie.

%prep
%setup -q -n jsondiff-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

for bin in jdiff jsondiff ; do
	%{__mv} $RPM_BUILD_ROOT%{_bindir}/${bin} $RPM_BUILD_ROOT%{_bindir}/${bin}-2
done

%py_postclean
%endif

%if %{with python3}
%py3_install

for bin in jdiff jsondiff ; do
	%{__mv} $RPM_BUILD_ROOT%{_bindir}/${bin} $RPM_BUILD_ROOT%{_bindir}/${bin}-3
	ln -sf ${bin}-3 $RPM_BUILD_ROOT%{_bindir}/${bin}
done
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/jdiff-2
%attr(755,root,root) %{_bindir}/jsondiff-2
%{py_sitescriptdir}/jsondiff
%{py_sitescriptdir}/jsondiff-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-jsondiff
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/jdiff
%attr(755,root,root) %{_bindir}/jdiff-3
%attr(755,root,root) %{_bindir}/jsondiff
%attr(755,root,root) %{_bindir}/jsondiff-3
%{py3_sitescriptdir}/jsondiff
%{py3_sitescriptdir}/jsondiff-%{version}-py*.egg-info
%endif
