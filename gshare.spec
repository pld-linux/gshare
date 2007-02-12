Summary:	Share files using Zeroconf technology
Summary(pl.UTF-8):	Współdzielenie plików przy użyciu technologii Zeroconf
Name:		gshare
Version:	0.92
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://yimports.com/~cpinto/downloads/gshare/%{name}-%{version}.tar.gz
# Source0-md5:	e3aa2f070aa2fff29b3f1916c1f61788
URL:		http://www.yimports.com/~cpinto/projects/gnome/gshare/
BuildRequires:	dotnet-avahi-devel
BuildRequires:	dotnet-dbus-sharp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GShare creates a special folder at the user's home directory (~/Shared
Files) and uses that as an FTP root for the built-in FTP server. These
are shared using Zeroconf technology.

%description -l pl.UTF-8
GShare tworzy specjalny folder w katalogu domowym użytkownika
(~/Shared Files) i wykorzystuje go jako główny katalog FTP dla
wbudowanego serwera FTP. Zawartość jest współdzielona przy użyciu
technologii Zeroconf.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.dll
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_datadir}/dbus-1/services/*.service
