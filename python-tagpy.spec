%define shortname tagpy

Summary:	Python bindings for TagLib to read and write music files tags
Name:		python-tagpy
Version:	2018.1.1
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.python.org/pypi/tagpy
Source0:	http://pypi.python.org/packages/source/t/tagpy/tagpy-%{version}.tar.gz

# from Debian
Patch0:		taglib-1.8.patch

# from AUR
Patch1:   compile_fix.patch

BuildRequires:  pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	boost-devel
BuildRequires:  boost-python-devel

%description
TagPy is a Python crust (or a set of Python bindings) for TagLib, which allows
to read and write ID3 tags of version 1 and 2, access Xiph Comments in Ogg
Vorbis Files and Ogg Flac Files and access APE tags in Musepack and MP3 files.

%prep
%setup -q -n %{shortname}-%{version}
%autopatch -p1
rm -rf tagpy.egg-info
chmod -x test/tagrename

%build
CFLAGS="%{optflags} `pkg-config --cflags taglib`" \
CFLAGS="%{optflags} `pkg-config --cflags taglib`" \
%py_build

%install
%py_install

%files
%doc test/*.py test/tagrename
%{python_sitearch}/%{shortname}/
%{python_sitearch}/*.so
%{python_sitearch}/*.egg-info


%changelog
* Thu Mar 17 2011 Funda Wang <fwang@mandriva.org> 0.94.8-2mdv2011.0
+ Revision: 645717
- rebuild for new boost

  + Matthew Dawkins <mattydaw@mandriva.org>
    - removed poorly commented out patch

* Fri Nov 05 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.94.8-1mdv2011.0
+ Revision: 593704
- Updated to 0.94.8.
- Rebuild for new python.

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 0.94.7-1mdv2011.0
+ Revision: 572592
- New version 0.94.7

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 0.94.5-6mdv2011.0
+ Revision: 572550
- rebuild for new boost

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 0.94.5-5mdv2011.0
+ Revision: 501882
- rebuild for new boost

* Fri Aug 21 2009 Götz Waschk <waschk@mandriva.org> 0.94.5-4mdv2010.0
+ Revision: 418917
- rebuild

* Wed Dec 31 2008 Adam Williamson <awilliamson@mandriva.org> 0.94.5-3mdv2009.1
+ Revision: 321615
- fix python requires
- rebuild for python 2.6
- fix file list for differing python versions

* Mon Dec 22 2008 Funda Wang <fwang@mandriva.org> 0.94.5-2mdv2009.1
+ Revision: 317403
- rebuild for new boost

* Sun Dec 14 2008 Adam Williamson <awilliamson@mandriva.org> 0.94.5-1mdv2009.1
+ Revision: 314071
- rebuild for new(ish) boost
- jump through a couple of hoops with the new configure script and taglib's
  header location
- rediff baz.patch (file was moved)
- new release 0.94.5

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Erwan Velu <erwan@mandriva.org>
    - Rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Nov 23 2007 Jérôme Soyer <saispo@mandriva.org> 0.91-1mdv2008.1
+ Revision: 111580
- import python-tagpy


