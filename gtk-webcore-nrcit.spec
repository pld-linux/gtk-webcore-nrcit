%define snap	125
Summary:	Port of WebKit embeddable web component to GTK+
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+
Name:		gtk-webcore-nrcit
Version:	0.5.3
Release:	0.%{snap}.1
License:	BSD-like
Group:		X11/Libraries
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	7dfd80800a0b92d57832af9337ae2232
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.11.0
BuildRequires:	fontconfig-devel >= 1.0.0
BuildRequires:	gtk-webcore-nrcore-libs-devel >= 0.5.3
BuildRequires:	librsvg-devel >= 2.2.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXft-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-webcore-nrcit is a port of the WebKit embeddable web component to
GTK+.

%description -l pl.UTF-8
gtk-webcore-nrcit to port osadzalnego komponentu WWW WebKit do GTK+.

%package libs
Summary:	Shared library for gtk-webcore-nrcit
Summary(pl.UTF-8):	Współdzielona biblioteka gtk-webcore-nrcit
Group:		X11/Libraries
Requires:	curl-libs >= 7.11.0
Requires:	fontconfig-libs >= 1.0.0
Requires:	gtk-webcore-nrcore-libs >= 0.5.3
Requires:	librsvg >= 2.2.0
Requires:	xorg-lib-libXft >= 2.0.0

%description libs
gtk-webcore-nrcit is a port of the WebKit embeddable web component to
GTK+.

%description libs -l pl.UTF-8
gtk-webcore-nrcit to port osadzalnego komponentu WWW WebKit do GTK+.

%package libs-devel
Summary:	Development files for gtk-webcore-nrcit
Summary(pl.UTF-8):	Pliki programistyczne gtk-webcore-nrcit
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	curl-devel >= 7.11.0
Requires:	fontconfig-devel >= 1.0.0
Requires:	gtk-webcore-nrcore-libs-devel >= 0.5.3
Requires:	librsvg-devel >= 2.2.0
Requires:	xorg-lib-libXft-devel >= 2.0.0

%description libs-devel
Development files for gtk-webcore-nrcit.

%description libs-devel -l pl.UTF-8
Pliki programistyczne gtk-webcore-nrcit.

%package libs-static
Summary:	Static gtk-webcore-nrcit library
Summary(pl.UTF-8):	Statyczna biblioteka gtk-webcore-nrcit
Group:		Development/Libraries
Requires:	%{name}-libs-devel = %{version}-%{release}

%description libs-static
Static gtk-webcore-nrcit library.

%description libs-static -l pl.UTF-8
Statyczna biblioteka gtk-webcore-nrcit.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files libs
%defattr(644,root,root,755)
%doc AUTHORS README TODO NEWS
%attr(755,root,root) %{_libdir}/libgtk_webcore_nrcit.so.*.*.*

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk_webcore_nrcit.so
%{_libdir}/libgtk_webcore_nrcit.la
%{_includedir}/gtk-webcore/webi
%{_includedir}/gtk-webcore/webkit-gtk
%{_pkgconfigdir}/%{name}.pc

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/libgtk_webcore_nrcit.a
