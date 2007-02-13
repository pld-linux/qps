Summary:	A visual process manager
Summary(pl.UTF-8):	Wizualny zarządca procesów
Name:		qps
Version:	1.9.18.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://kldp.net/frs/download.php/3550/%{name}-%{version}.tar.gz
# Source0-md5:	a55fabf362991fd13d43e930209927ea
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
sed -i -e 's/-lqt/-lqt-mt/' Makefile
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
