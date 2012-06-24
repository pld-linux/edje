Summary:	Complex Graphical Design/Layout Engine
Summary(pl):	Z�o�ony silnik graficznego projektowania/planowania
Name:		edje
Version:	0.5.0
%define	_snap	20050701
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e17/libs/%{name}-%{_snap}.tar.gz
# Source0-md5:	94cd1aabb9fc7785123fb4d92255f85e
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
or widget set that may use Edje as a convenient way of being able to
configure parts of the display.

%description -l pl
Edje to z�o�ony silnik graficznego projektowania i planowania.
Dostarcza mechanizm pozwalaj�cy na definiowanie element�w graficznych
za pomoc� danych konfiguracyjnych poprzez rozmieszczenie, zachowanie i
wygl�d. Edje pozwala na wiele kolekcji projekt�w w jednym pliku,
zezwalaj�c na istnienie pe�nego zbioru obraz�w, animacji i kontrolek
jako ca�o�ci.

Edje oddziela rozmieszczenie, wygl�d i logik� zachowania na r�ne,
niezale�ne elementy. Pozwala to na wsp�dzielenie danych obraz�w i
informacji o konfiguracji element�w graficznych bez wymagania tego.
Rozdzielenie to i uproszczony model programowania sterowanego
zdarzeniami mo�e stworzy� prawie dowolny wygl�d i zachowanie
podstawowych element�w graficznych. Wszystko bardziej z�o�one jest
raczej domen� aplikacji lub zbioru widget�w, kt�re mog� u�ywa� Edje
jako wygodnego sposobu konfigurowania cz�ci ekranu.

%package devel
Summary:	Edje header files
Summary(pl):	Pliki nag��wkowe Edje
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ecore-devel
Requires:	embryo-devel
Requires:	imlib2-devel

%description devel
Header files for Edje.

%description devel -l pl
Pliki nag��wkowe Edje.

%package static
Summary:	Static Edje library
Summary(pl):	Statyczna biblioteka Edje
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Edje library.

%description static -l pl
Statyczna biblioteka Edje.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-edje-cc
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
%doc AUTHORS COPYING COPYING-PLAIN INSTALL README
%attr(755,root,root) %{_bindir}/edje
%attr(755,root,root) %{_bindir}/edje_*
%attr(755,root,root) %{_libdir}/libedje.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/edje-config
%attr(755,root,root) %{_libdir}/libedje.so
%{_libdir}/libedje.la
%{_includedir}/Edje*
%{_pkgconfigdir}/edje.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libedje.a
