%define shortname tagpy

Summary:	Python bindings for TagLib to read and write music files tags
Name:		python-tagpy
Version:	0.94.5
Release:	%{mkrel 2}
License:	BSD
Group:		Development/Python
URL:		http://news.tiker.net/software/tagpy
Source0:	http://news.tiker.net/news.tiker.net/download/software/tagpy/tagpy-%{version}.tar.gz
Source1:	tagpy-LICENSE
Patch0:		tagpy-0.94.5-baz.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	python-devel
BuildRequires:	taglib-devel
BuildRequires:	boost-devel

%description
TagPy is a Python crust (or a set of Python bindings) for TagLib, which allows
to read and write ID3 tags of version 1 and 2, access Xiph Comments in Ogg
Vorbis Files and Ogg Flac Files and access APE tags in Musepack and MP3 files.

%prep
%setup -q -n %{shortname}-%{version}
%patch0 -p1 -b .baz
%{__install} -p -m 0644 %{SOURCE1} LICENSE

%build
./configure --boost-python-libname=boost_python-mt
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
%{py_platsitedir}/%{shortname}-%{version}-py2.5.egg-info
