%define name	qps
%define ver	1.6
%define rel	1

Summary: A visual process manager
Name: %name
Version: %ver
Release: %rel
Copyright: GPL
Group: X11/Utilities
Source: ftp://ptah.lnf.kth.se/pub/qps/qps-%{ver}.tar.gz
Patch: qps-Makefile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL: http://www.student.nada.kth.se/~f91-men/qps/
Docdir: /usr/doc
Packager: Jochem Wichers Hoeth <wiho@chem.uva.nl>

%description
Qps is a visual process manager, an X11 version of "top" or "ps"
that displays processes in a window and lets you sort and manipulate
them. 

%prep
%setup
%patch -p1

%build
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man1
install -s -m 755 -o 0 -g 0 qps $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 444 -o 0 -g 0 qps.1 $RPM_BUILD_ROOT/usr/X11R6/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/X11R6/bin/qps
/usr/X11R6/man/man1/qps.1
%doc CHANGES COPYING README
