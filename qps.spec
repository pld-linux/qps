Summary:	A visual process manager
Summary(pl):	Wizualny zarz±dca procesów
Name:		qps
Version:	1.9.7
Release:	2
License:	GPL
Group:		X11/Applications
Vendor:		Mattias Engdegard <f91-men@nada.kth.se>
Source0:	ftp://ptah.lnf.kth.se/pub/qps/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-time.patch
URL:		http://www.student.nada.kth.se/~f91-men/qps/
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Qps is a visual process manager, an X11 version of "top" or "ps" that
displays processes in a window and lets you sort and manipulate them.

%description -l pl
Qps to graficzny program do zarz±dzania procesami, czyli wersja X11
programów "top" lub "ps", wy¶wietlaj±cy procesy w okienku i
pozwalaj±cy je sortowaæ oraz nimi manipulowaæ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install qps $RPM_BUILD_ROOT%{_bindir}
install qps.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/qps
%{_mandir}/man1/*
