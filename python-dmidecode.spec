%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python_ver: %global python_ver %(%{__python} -c "import sys ; print sys.version[:3]")}

Summary: Python module to access DMI data
Name: python-dmidecode
Version: 3.10.13
Release: 3%{?dist}
License: GPLv2+
Group: System Environment/Libraries
URL: http://projects.autonomy.net.au/python-dmidecode/
Source0: http://src.autonomy.net.au/python-dmidecode/%{name}-%{version}.tar.gz
# Upstream source gone. Repository restored from developer tree or source packages.
# Source1: generate-tarball.sh
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libxml2-python
BuildRequires: libxml2-python
BuildRequires: libxml2-devel
BuildRequires: python-devel

Patch1: SIGILL-catcher.patch
Patch2: dmispec-remove.patch
Patch3: installed-invalid.patch

%description
python-dmidecode is a python extension module that uses the
code-base of the 'dmidecode' utility, and presents the data
as python data structures or as XML data using libxml2.

%prep
%setup -q
%patch1 -p1 -b .SIGILL-catcher
%patch2 -p1 -b .dmispec-remove
%patch3 -p1 -b .install-invalid

%build
make build
cd unit-tests
make
cd ..

%install
rm -rf $RPM_BUILD_ROOT
python src/setup.py install --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README doc/README.upstream doc/LICENSE doc/AUTHORS doc/AUTHORS.upstream
%{python_sitearch}/dmidecodemod.so
%{python_sitearch}/dmidecode.py
%{python_sitearch}/dmidecode.py[co]
%if "%{python_ver}" >= "2.5"
%{python_sitearch}/*.egg-info
%endif
%{_datadir}/python-dmidecode/

%changelog

* Thu Jun 20 2013 Ales Ledvinka <aledvink@redhat.com> - 3.10.13-3
- Attribute installed may appear as duplicate and cause invalid XML.
  Resolves: #975059

* Mon Jun 17 2013 Ales Ledvinka <aledvink@redhat.com> - 3.10.13-2
- Attribute dmispec may cause invalid XML on some hardware.
  Resolves: #975059


* Wed Jun 29 2011 Roman Rakus <rrakus@redhat.com> - 3.10.13-1
- Update to 3.10.13 release
  Resolves: #621567, #627901, #667363
- Signal handler for SIGILL
  Resolves #646429

* Wed May 19 2010 Roman Rakus <rrakus@redhat.com> - 3.10.12-1
- Update to 3.10.12 release
  Resolves: #588387

* Fri Feb 26 2010 Roman Rakus <rrakus@redhat.com> - 3.10.11-2
- Upstream license patch (now GPLv2+)

* Tue Feb 16 2010 Nima Talebi <nima@it.net.au> - 3.10.11-1
- Update to new release

* Tue Jan 12 2010 Nima Talebi <nima@it.net.au> - 3.10.10-1
- Update to new release

* Thu Jan 07 2010 Nima Talebi <nima@it.net.au> - 3.10.9-1
- Update to new release


* Thu Dec 15 2009 Nima Talebi <nima@it.net.au> - 3.10.8-1
- New Upstream release.
- Big-endian and little-endian approved.
- Packaged unit-test to tarball.
- Rewritten unit-test to be able to run as non-root user, where it will not
  try to read /dev/mem.
- Added two dmidump data files to the unit-test.

* Thu Nov 26 2009 David Sommerseth <davids@redhat.com> - 3.10.7-3
- Fixed even more .spec file issues and removed explicit mentioning
  of /usr/share/python-dmidecode/pymap.xml

* Wed Nov 25 2009 David Sommerseth <davids@redhat.com> - 3.10.7-2
- Fixed some .spec file issues (proper Requires, use _datadir macro)

* Wed Sep 23 2009 Nima Talebi <nima@it.net.au> - 3.10.7-1
- Updated source0 to new 3.10.7 tar ball

* Wed Jul 13 2009 David Sommerseth <davids@redhat.com> - 3.10.6-6
- Only build the python-dmidecode module, not everything

* Wed Jul 13 2009 David Sommerseth <davids@redhat.com> - 3.10.6-5
- Added missing BuildRequres for libxml2-python

* Wed Jul 13 2009 David Sommerseth <davids@redhat.com> - 3.10.6-4
- Added missing BuildRequres for python-devel

* Wed Jul 13 2009 David Sommerseth <davids@redhat.com> - 3.10.6-3
- Added missing BuildRequres for libxml2-devel

* Wed Jul 13 2009 David Sommerseth <davids@redhat.com> - 3.10.6-2
- Updated release, to avoid build conflict

* Wed Jun 10 2009 David Sommerseth <davids@redhat.com> - 3.10.6-1
- Updated to work with the new XML based python-dmidecode

* Sat Mar  7 2009 Clark Williams <williams@redhat.com> - 2.10.3-1
- Initial build.

