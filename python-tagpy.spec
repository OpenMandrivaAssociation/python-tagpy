%define shortname tagpy

Summary:	Python bindings for TagLib to read and write music files tags
Name:		python-tagpy
Version:	0.94.7
Release:	%{mkrel 1}
License:	MIT
Group:		Development/Python
URL:		http://pypi.python.org/pypi/tagpy
Source0:	http://pypi.python.org/packages/source/t/tagpy/tagpy-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
%{py_requires -d}
BuildRequires:	python-setuptools
BuildRequires:	taglib-devel
BuildRequires:	boost-devel

%description
TagPy is a Python crust (or a set of Python bindings) for TagLib, which allows
to read and write ID3 tags of version 1 and 2, access Xiph Comments in Ogg
Vorbis Files and Ogg Flac Files and access APE tags in Musepack and MP3 files.

%prep
%setup -q -n %{shortname}-%{version}
#%patch0 -p1 -b .baz
#%{__install} -p -m 0644 %{SOURCE1} LICENSE

%build
./configure.py --boost-python-libname=boost_python-mt
CFLAGS="%{optflags} -I%{_includedir}/taglib" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README test/*.py test/tagrename
%{py_platsitedir}/%{shortname}/
%{py_platsitedir}/_%{shortname}.so
%{py_platsitedir}/%{shortname}-%{version}-py%{pyver}.egg-info
