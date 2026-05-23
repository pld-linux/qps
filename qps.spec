#
# Conditional build:
#
%define         qtver           6.6.0

Summary:	A visual process manager
Summary(pl.UTF-8):	Wizualny zarządca procesów
Name:		qps
Version:	2.13.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://github.com/lxqt/qps/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	554ada593b7d19f6d3a81cc493682a14
URL:		https://lxqt-project.org
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	liblxqt-devel >= 2.4.0
BuildRequires:	liblxqt-devel >= 2.4.0
BuildRequires:	lxqt-build-tools >= 2.4.0
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qps is a visual process manager, an X11 version of "top" or "ps" that
displays processes in a window and lets you sort and manipulate them.

%description -l pl.UTF-8
Qps to graficzny program do zarządzania procesami, czyli wersja X11
programów "top" lub "ps", wyświetlający procesy w okienku i
pozwalający je sortować oraz nimi manipulować.

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG README.md
%attr(755,root,root) %{_bindir}/qps
%{_mandir}/man1/*
%{_desktopdir}/qps.desktop
%{_iconsdir}/hicolor/scalable/apps/qps.svg
%{_datadir}/metainfo/org.lxqt.Qps.appdata.xml
%dir %{_datadir}/qps
# required for the lang files
%dir %{_datadir}/qps/translations
