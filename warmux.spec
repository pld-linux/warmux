Summary:	A free (libre) clone of Worms from Team17
Summary(de):	Ein kostenloser Team17 Worms-Klon
Summary(pl):	Wolnodostępny klon Worms z Team17
Name:		wormux
Version:	0.7.4
Release:	1
License:	GPL v2
Group:		Applications/Games
Source0:	http://download.gna.org/wormux/wormux-%{version}.tar.gz
# Source0-md5:	271de7da072bc4e8c023f55e85a42eb0
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.wormux.org/en/index.php
BuildRequires:	SDL-devel >= 1.2.6
BuildRequires:	SDL_gfx-devel >= 2.0.13
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libxml++-devel >= 2.6
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free (libre) clone of Worms from Team17.

%description -l de
Ein kostenloser Team17 Worms-Klon.

%description -l pl
Wolnodostępny klon gry Worms z Team17.

%prep
%setup -q

# let *.mo build
rm -f po/stamp-po

%build
%configure \
	--with-datadir-name=%{_datadir}/games/%{name} 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/wormux
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man6/wormux.*
