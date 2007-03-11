Summary:	A visual process manager
Summary(pl.UTF-8):	Wizualny zarządca procesów
Name:		qps
Version:	1.9.19a
Release:	1
License:	GPL
Group:		X11/Applications
#Source0Download:	http://kldp.net/frs/?group_id=592
Source0:	http://kldp.net/frs/download.php/3800/%{name}-%{version}.tar.bz2
# Source0-md5:	bac0fea0ace4681eb85f31c02b6b0562
URL:		http://qps.kldp.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qps is a visual process manager, an X11 version of "top" or "ps" that
displays processes in a window and lets you sort and manipulate them.

%description -l pl.UTF-8
Qps to graficzny program do zarządzania procesami, czyli wersja X11
programów "top" lub "ps", wyświetlający procesy w okienku i
pozwalający je sortować oraz nimi manipulować.

%prep
%setup -q

%build
qmake
%{__make}\
	QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install qps $RPM_BUILD_ROOT%{_bindir}
install qps.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README_INSTALL
%attr(755,root,root) %{_bindir}/qps
%{_mandir}/man1/*
