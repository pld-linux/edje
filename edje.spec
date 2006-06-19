#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Complex Graphical Design/Layout Engine
Summary(pl):	Z³o¿ony silnik graficznego projektowania/planowania
Name:		edje
Version:	0.5.0.027
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	43089969884f28ed306d95d7fa780dd7
URL:		http://enlightenment.org/Libraries/Edje/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ecore-devel
BuildRequires:	embryo-devel
BuildRequires:	imlib2-devel >= 1.2.1
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cpp
Requires:	fonts-TTF-bitstream-vera
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

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
Edje to z³o¿ony silnik graficznego projektowania i planowania.
Dostarcza mechanizm pozwalaj±cy na definiowanie elementów graficznych
za pomoc± danych konfiguracyjnych poprzez rozmieszczenie, zachowanie i
wygl±d. Edje pozwala na wiele kolekcji projektów w jednym pliku,
zezwalaj±c na istnienie pe³nego zbioru obrazów, animacji i kontrolek
jako ca³o¶ci.

Edje oddziela rozmieszczenie, wygl±d i logikê zachowania na ró¿ne,
niezale¿ne elementy. Pozwala to na wspó³dzielenie danych obrazów i
informacji o konfiguracji elementów graficznych bez wymagania tego.
Rozdzielenie to i uproszczony model programowania sterowanego
zdarzeniami mo¿e stworzyæ prawie dowolny wygl±d i zachowanie
podstawowych elementów graficznych. Wszystko bardziej z³o¿one jest
raczej domen± aplikacji lub zbioru widgetów, które mog± u¿ywaæ Edje
jako wygodnego sposobu konfigurowania czê¶ci ekranu.

%package libs
Summary:	Edje library
Summary(pl):	Biblioteka edje
Group:		X11/Libraries

%description libs
Edje library.

%description libs -l pl
Biblioteka edje.

%package devel
Summary:	Edje header files
Summary(pl):	Pliki nag³ówkowe Edje
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	ecore-devel
Requires:	embryo-devel
Requires:	imlib2-devel >= 1.2.1

%description devel
Header files for Edje.

%description devel -l pl
Pliki nag³ówkowe Edje.

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
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-edje-cc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_datadir}/%{name}/data/test/fonts
VERA=$(ls Vera*.ttf)
for FONT in $VERA; do
	rm -f $FONT
	ln -s %{_fontsdir}/TTF/$FONT .
done

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN INSTALL README
%attr(755,root,root) %{_bindir}/edje
%attr(755,root,root) %{_bindir}/edje_*
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedje.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/edje-config
%attr(755,root,root) %{_libdir}/libedje.so
%{_libdir}/libedje.la
%{_includedir}/Edje*
%{_pkgconfigdir}/edje.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libedje.a
%endif
