#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
%define		ecore_ver	1.0.0
%define		eet_ver 	1.4.0
%define		embryo_ver	1.0.0
%define		evas_ver	1.0.0
Summary:	Complex Graphical Design/Layout Engine
Summary(pl.UTF-8):	Złożony silnik graficznego projektowania/planowania
Name:		edje
Version:	1.0.0
Release:	3
License:	BSD
Group:		X11/Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	ce0fdc6c02bc6d6d99b798c27d1d9466
URL:		http://trac.enlightenment.org/e/wiki/Edje
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	ecore-devel >= %{ecore_ver}
BuildRequires:	ecore-evas-devel >= %{ecore_ver}
BuildRequires:	ecore-file-devel >= %{ecore_ver}
BuildRequires:	ecore-imf-devel >= %{ecore_ver}
BuildRequires:	ecore-imf-evas-devel >= %{ecore_ver}
BuildRequires:	eet-devel >= %{eet_ver}
BuildRequires:	embryo-devel >= %{embryo_ver}
BuildRequires:	evas-devel >= %{evas_ver}
BuildRequires:	libtool
BuildRequires:	lua51 >= 5.1.0
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python >= 1:2.5
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cpp
Requires:	evas-engine-buffer >= %{evas_ver}
Requires:	evas-loader-png >= %{evas_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx
%define		specflags_x86_64	-mfpmath=387
%define		specflags_amd64		-mfpmath=387

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

%description -l pl.UTF-8
Edje to złożony silnik graficznego projektowania i planowania.
Dostarcza mechanizm pozwalający na definiowanie elementów graficznych
za pomocą danych konfiguracyjnych poprzez rozmieszczenie, zachowanie i
wygląd. Edje pozwala na wiele kolekcji projektów w jednym pliku,
zezwalając na istnienie pełnego zbioru obrazów, animacji i kontrolek
jako całości.

Edje oddziela rozmieszczenie, wygląd i logikę zachowania na różne,
niezależne elementy. Pozwala to na współdzielenie danych obrazów i
informacji o konfiguracji elementów graficznych bez wymagania tego.
Rozdzielenie to i uproszczony model programowania sterowanego
zdarzeniami może stworzyć prawie dowolny wygląd i zachowanie
podstawowych elementów graficznych. Wszystko bardziej złożone jest
raczej domeną aplikacji lub zbioru widgetów, które mogą używać Edje
jako wygodnego sposobu konfigurowania części ekranu.

%package libs
Summary:	Edje library
Summary(pl.UTF-8):	Biblioteka edje
Group:		X11/Libraries
Requires:	ecore >= %{ecore_ver}
Requires:	ecore-file >= %{ecore_ver}
Requires:	ecore-imf >= %{ecore_ver}
Requires:	ecore-imf-evas >= %{ecore_ver}
Requires:	eet >= %{eet_ver}
Requires:	embryo >= %{embryo_ver}
Requires:	evas >= %{evas_ver}

%description libs
Edje library.

%description libs -l pl.UTF-8
Biblioteka edje.

%package devel
Summary:	Edje header files
Summary(pl.UTF-8):	Pliki nagłówkowe Edje
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	ecore-devel >= %{ecore_ver}
Requires:	ecore-file-devel >= %{ecore_ver}
Requires:	ecore-imf-devel >= %{ecore_ver}
Requires:	ecore-imf-evas-devel >= %{ecore_ver}
Requires:	eet-devel >= %{eet_ver}
Requires:	embryo-devel >= %{embryo_ver}
Requires:	evas-devel >= %{evas_ver}

%description devel
Header files for Edje.

%description devel -l pl.UTF-8
Pliki nagłówkowe Edje.

%package static
Summary:	Static Edje library
Summary(pl.UTF-8):	Statyczna biblioteka Edje
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Edje library.

%description static -l pl.UTF-8
Statyczna biblioteka Edje.

%package -n vim-syntax-edc
Summary:	EDC syntax support for Vim
Summary(pl.UTF-8):	Obsługa składni EDC dla Vima
Group:		Applications/Editors/Vim
Requires:	vim-rt

%description -n vim-syntax-edc
EDC syntax support for Vim.

%description -n vim-syntax-edc -l pl.UTF-8
Obsługa składni EDC dla Vima.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--enable-edje-cc \
	--with-vim=/usr/share/vim/vimfiles
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/edje
install -D data/edc.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax/edc.vim

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/edje_cc
%attr(755,root,root) %{_bindir}/edje_decc
%attr(755,root,root) %{_bindir}/edje_external_inspector
%attr(755,root,root) %{_bindir}/edje_inspector
%attr(755,root,root) %{_bindir}/edje_player
%attr(755,root,root) %{_bindir}/edje_recc
%attr(755,root,root) %{_bindir}/inkscape2edc
%dir %{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/mime/packages/edje.xml

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedje.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libedje.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedje.so
%{_libdir}/libedje.la
%{_includedir}/edje-1
%{_pkgconfigdir}/edje.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libedje.a
%endif

%files -n vim-syntax-edc
%defattr(644,root,root,755)
%{_datadir}/vim/vimfiles/syntax/edc.vim
