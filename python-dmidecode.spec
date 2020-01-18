%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python_ver: %global python_ver %(%{__python} -c "import sys ; print sys.version[:3]")}

Summary: Python module to access DMI data
Name: python-dmidecode
Version: 3.10.13
Release: 12%{?dist}
License: GPLv2
Group: System Environment/Libraries
URL: http://projects.autonomy.net.au/python-dmidecode/
Source0: %{name}-%{version}.tar.xz
Source1: generate-tarball.sh
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libxml2-python
BuildRequires: libxml2-python
BuildRequires: libxml2-devel
BuildRequires: python-devel

# already in restored upstream git
Patch1: SIGILL-catcher.patch
# email: upstream why not in git, planed for release
Patch2: dmispec-remove.patch
# email: git postponed but planned for release
Patch3: installed-invalid.patch
Patch4: 0001-Harden-dmi_string-calls-with-better-NULL-checks.patch

%description
python-dmidecode is a python extension module that uses the
code-base of the 'dmidecode' utility, and presents the data
as python data structures or as XML data using libxml2.

%prep
%setup -q
%patch1 -p1 -b .SIGILL-catcher
%patch2 -p1 -b .dmispec-remove
%patch3 -p1 -b .install-invalid
%patch4 -p1

%build
make build
cd unit-tests
make
cd ..

%install
rm -rf $RPM_BUILD_ROOT
python src/setup.py install --root $RPM_BUILD_ROOT --prefix=%{_prefix}

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
* Mon May 22 2017 Petr Oros <poros@redhat.com> - 3.10.13-12
- Fix segfaults when reading invalid dmidecode data
- Resolves: #1431702

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.10.13-11
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.10.13-10
- Mass rebuild 2013-12-27

* Mon Jun 20 2013 Ales Ledvinka <aledvink@redhat.com> - 3.10.13-9
- Attribute installed may appear as duplicate and cause invalid XML.

* Mon Jun 17 2013 Ales Ledvinka <aledvink@redhat.com> - 3.10.13-8
- Attribute dmispec may cause invalid XML on some hardware.
- Signal handler for SIGILL.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 19 2012 Ales Ledvinka <aledvink@redhat.com> 3.10.14-5
- Upstream relocated. Document source tag and tarball generation.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.10.13-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 15 2010 Roman Rakus <rrakus@redhat.com> - 3.10.13-1
- Update to new release

* Fri Mar 12 2010 Nima Talebi <nima@it.net.au> - 3.10.12-1
- Update to new release

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

