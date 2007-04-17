Summary:	A free (libre) clone of Worms from Team17
Summary(de.UTF-8):	Ein kostenloser Team17 Worms-Klon
Summary(pl.UTF-8):	Wolnodostępny klon Worms z Team17
Name:		wormux
Version:	0.7.9
Release:	2
License:	GPL v2+
Group:		Applications/Games
Source0:	http://download.gna.org/wormux/%{name}-%{version}.tar.gz
# Source0-md5:	d921ae5bad243dec7bb6825d6e0b9d16
Patch0:		%{name}-disable-werror.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.wormux.org/en/index.php
BuildRequires:	SDL-devel >= 1.2.6
BuildRequires:	SDL_gfx-devel >= 2.0.13
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	libxml++-devel >= 2.6
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free (libre) clone of Worms from Team17.

%description -l de.UTF-8
Ein kostenloser Team17 Worms-Klon.

%description -l pl.UTF-8
Wolnodostępny klon gry Worms z Team17.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# let *.mo build
rm -f po/stamp-po

%build
touch config.rpath
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--with-datadir-name=%{_datadir}/games/%{name} 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install data/wormux.desktop $RPM_BUILD_ROOT%{_desktopdir}
install data/wormux_32x32.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/pt{-BR,_BR}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README 
%attr(755,root,root) %{_bindir}/wormux
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
%{_mandir}/man6/wormux.6*
