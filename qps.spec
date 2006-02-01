Summary:	A visual process manager
Summary(pl):	Wizualny zarz±dca procesów
Name:		qps
Version:	1.9.11
Release:	1
License:	GPL
Group:		X11/Applications
Vendor:		Mattias Engdegard <f91-men@nada.kth.se>
Source0:	http://kldp.net/frs/download.php/2930/%{name}-%{version}.tar.gz
# Source0-md5:	c094cd755ebe5f1c923f5ede5e96affc
URL:		http://qps.kldp.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Qps is a visual process manager, an X11 version of "top" or "ps" that
displays processes in a window and lets you sort and manipulate them.

%description -l pl
Qps to graficzny program do zarz±dzania procesami, czyli wersja X11
programów "top" lub "ps", wy¶wietlaj±cy procesy w okienku i
pozwalaj±cy je sortowaæ oraz nimi manipulowaæ.

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
