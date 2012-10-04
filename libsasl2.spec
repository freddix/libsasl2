%define		org_name	cyrus-sasl

Summary:	SASL library
Name:		libsasl2
Version:	2.1.25
Release:	1
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.andrew.cmu.edu/pub/cyrus/%{org_name}-%{version}.tar.gz
# Source0-md5:	341cffe829a4d71f2a6503d669d5a946
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SASL library.

%package devel
Summary:	Header files for SASL library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for SASL library.

%prep
%setup -qn %{org_name}-%{version}

rm config/libtool.*

%build
%{__libtoolize}
%{__aclocal} -I cmulocal -I config
%{__automake}
%{__autoconf}
%configure
%{__make} -C lib
%{__make} -C include

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C lib install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C include install \
	DESTDIR=$RPM_BUILD_ROOT

chmod +x $RPM_BUILD_ROOT%{_libdir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libsasl2.so.?
%attr(755,root,root) %{_libdir}/libsasl2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsasl2.so
%{_libdir}/libsasl2.la
%{_includedir}/sasl

