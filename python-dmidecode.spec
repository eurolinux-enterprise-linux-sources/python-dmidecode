%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python_ver: %global python_ver %(%{__python} -c "import sys ; print sys.version[:3]")}

Summary: Python module to access DMI data
Name: python-dmidecode
Version: 3.10.15
Release: 2%{?dist}
License: GPLv2+
Group: System Environment/Libraries
URL: https://fedorahosted.org/python-dmidecode/
Source0: https://git.fedorahosted.org/cgit/python-dmidecode.git/snapshot/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libxml2-python
BuildRequires: libxml2-python
BuildRequires: libxml2-devel
BuildRequires: python-devel

Patch0001: 0001-python-dmidecode-doesn-t-trim-whitespace-from-some-f.patch

%description
python-dmidecode is a python extension module that uses the
code-base of the 'dmidecode' utility, and presents the data
as python data structures or as XML data using libxml2.

%prep
%setup -q
%patch0001 -p1

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
* Wed Feb 28 2018 Lianbo Jiang <lijiang@redhat.com> - 3.10.15-2
- Trim whitespace from some fields
- Resolves: #1445791

* Mon Oct 17 2016 Petr Oros <poros@redhat.com> - 3.10.15-1
- New upstream version v3.10.15
- Resolves: #728319

* Mon Oct 17 2016 Petr Oros <poros@redhat.com> - 3.10.13-4
- Fix upstream source url
- Resolves: #1354287

* Thu Jun 20 2013 Ales Ledvinka <aledvink@redhat.com> - 3.10.13-3
- Attribute installed may appear as duplicate and cause invalid XML.
  Resolves: #949036

* Mon Jun 17 2013 Ales Ledvinka <aledvink@redhat.com> - 3.10.13-2
- Attribute dmispec may cause invalid XML on some hardware.
  Resolves: #949036


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

