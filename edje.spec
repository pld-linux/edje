Summary:	Complex Graphical Design/Layout Engine
Name:		edje
Version:	0.5.0
%define	_snap	20050105
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	99e72c15341ba6cad42aed8f3e29814d
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ecore-devel
BuildRequires:	embryo-devel
BuildRequires:	imlib2-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Edje is a complex graphical design and layout engine. It provides a
mechanism for allowing configuration data to define visual elements in
terms of layout, behavior, and appearance. Edje allows for multiple
collections of layouts in one file, allowing a complete set of images,
animations, and controls to exist as a unified whole.

Edje separates the arrangement, appearance, and behavior logic into
distinct independent entities. This allows visual objects to share
image data and configuration information without requiring them to do
so. This separation and simplistic event driven style of programming
can produce almost any look and feel one could want for basic visual
elements. Anything more complex is likely the domain of an application
or widget set that may use Edje as a conveneient way of being able to
configure parts of the display.

%package devel
Summary:	Edje headers, documentation and test programs
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	ecore-devel
Requires:	embryo-devel
Requires:	imlib2-devel

%description devel
Headers, static libraries, test programs and documentation for Edje

%package static
Summary:	Static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries.

%prep
#%%setup -q
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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libedje.so.*
%attr(755,root,root) %{_bindir}/edje
%attr(755,root,root) %{_bindir}/edje_*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedje.so
%{_libdir}/libedje.la
%attr(755,root,root) %{_bindir}/edje-config
%{_includedir}/Edje*
%{_pkgconfigdir}/edje.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libedje.a
