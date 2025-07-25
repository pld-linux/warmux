Summary:	A free (libre) clone of Worms from Team17
Summary(de.UTF-8):	Ein kostenloser Team17 Worms-Klon
Summary(pl.UTF-8):	Wolnodostępny klon Worms z Team17
Name:		warmux
Version:	11.04.1
Release:	10
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.gna.org/warmux/%{name}-%{version}.tar.bz2
# Source0-md5:	26ff65c43a9bb61a3f0529c98b943e35
Patch0:		desktop.patch
Patch1:		optflags.patch
Patch2:		%{name}-libpng15.patch
Patch3:		%{name}-gcc47.patch
Patch4:		gcc6.patch
URL:		http://www.warmux.org/
BuildRequires:	SDL-devel >= 1.2.6
BuildRequires:	SDL_gfx-devel >= 2.0.13
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.16.4-2
BuildRequires:	gettext-tools
BuildRequires:	libpng-devel
BuildRequires:	libxml++-devel >= 2.6
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.1
Requires:	%{name}-data = %{version}-%{release}
Suggests:	warmux-bonusmaps
Obsoletes:	wormux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free (libre) clone of Worms from Team17.

%description -l de.UTF-8
Ein kostenloser Team17 Worms-Klon.

%description -l pl.UTF-8
Wolnodostępny klon gry Worms z Team17.

%package data
Summary:	warmux data files
Group:		Applications/Games
BuildArch:	noarch

%description data
warmux data files

%prep
%setup -q -n %{name}-11.04
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

# disable building unsupported locales
%{__sed} -i -e 's|cpf||g;s|ua||g' po/LINGUAS

# fix jp locale
%{__sed} -i -e 's/ja_JP/ja/g' po/LINGUAS
mv -f po/ja{_JP,}.po

%build
%{__autopoint}
%{__aclocal} -I m4 -I build/m4
%{__autoconf}
%{__automake}
%configure \
	OPTFLAGS="%{rpmcxxflags}" \
	--with-datadir-name=%{_datadir}/games/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# rename pixmap
mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}_128x128.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/warmux
%attr(755,root,root) %{_bindir}/warmux-list-games
%{_mandir}/man6/warmux.6*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

%files data
%defattr(644,root,root,755)
%{_datadir}/games/%{name}
