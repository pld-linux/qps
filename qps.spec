Summary:	A visual process manager
Name:		qps
Version:	1.9.7
Release:	1
License:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Vendor:		Mattias Engdegard <f91-men@nada.kth.se>
Source0:	ftp://ptah.lnf.kth.se/pub/qps/%{name}-%{version}.tar.gz
URL:		http://www.student.nada.kth.se/~f91-men/qps/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Qps is a visual process manager, an X11 version of "top" or "ps" that
displays processes in a window and lets you sort and manipulate them.

%prep
%setup -q

%build
make

%install
rm -r $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s qps $RPM_BUILD_ROOT%{_bindir}

install qps.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf CHANGES README \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/qps
%{_mandir}/man1/*
