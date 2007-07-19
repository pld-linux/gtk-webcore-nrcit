%define snap	125
Summary:	Port of WebKit embeddable web component to GTK+
Name:		gtk-webcore-nrcit
Version:	0.5.3
Release:	0.%{snap}.1
License:	BSD-like
Group:		X11/Libraries
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	7dfd80800a0b92d57832af9337ae2232
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	curl-devel
BuildRequires:	gtk-webcore-nrcore-libs-devel
BuildRequires:	librsvg-devel
BuildRequires:	libssh2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-webcore-nrcit is a port of the WebKit embeddable web component to
GTK+.

%package libs
Summary:	Shared library for gtk-webcore-nrcit
Group:		X11/Libraries

%description libs
gtk-webcore-nrcit is a port of the WebKit embeddable web component to
GTK+.

%package libs-devel
Summary:	Development library for gtk-webcore-nrcit
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
gtk-webcore-nrcit is a port of the WebKit embeddable web component to
GTK+.

%prep
%setup -q -n %{name}

%build
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files libs-devel
%defattr(644,root,root,755)
%doc AUTHORS README TODO NEWS
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_includedir}/gtk-webcore/*
%{_pkgconfigdir}/%{name}.pc
