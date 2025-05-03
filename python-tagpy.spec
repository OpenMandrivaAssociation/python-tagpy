%define module tagpy
%bcond_without test

Name:			python-tagpy
License:	MIT
Version:	2025.1
Release:	1
Summary:	Python bindings for TagLib to read and write music files tags
Group:		Development/Python
URL:			https://pypi.org/project/tagpy/
# https://github.com/palfrey/tagpy
Source0:	https://github.com/palfrey/tagpy/archive/v%{version}/%{module}-%{version}.tar.gz

BuildRequires:	boost-devel
BuildRequires:	boost-python-devel >= 1.74
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(taglib) >= 1.9
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	utf8cpp-devel
%if %{with test}
BuildRequires:	python%{pyver}dist(build)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pre-commit)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(twine)
%endif

%description
TagPy is a Python crust (or a set of Python bindings) for TagLib, which allows
to read and write ID3 tags of version 1 and 2, access Xiph Comments in Ogg
Vorbis Files and Ogg Flac Files and access APE tags in Musepack and MP3 files.

%prep
%autosetup -n %{module}-%{version} -p1
rm -rf tagpy.egg-info
chmod -x test/tagrename

# remove remote git badges and pip/remote install guide from readme,
# we dont need those for system packages.
sed -i '3,4d;22,39d;' README.md
# remove pytest-cov as we are not doing code coverage checks.
sed -i '/pytest-cov/d' requirements-dev.in

%build
export CFLAGS="%{optflags} `pkg-config --cflags taglib`"
%py3_build

%install
%py3_install

%if %{with test}
%check
pip install -e .[test]
%{__python} -m pytest
%endif

%files
%{python_sitearch}/%{module}/
%{python_sitearch}/%{module}-%{version}.dist-info
%{python_sitearch}/_%{module}.cpython-%{python_version_nodots}-*-linux-gnu.so
%doc test/*.py test/tagrename
%doc README.md
%license LICENSE
