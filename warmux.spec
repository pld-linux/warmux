Summary:	A free (libre) clone of Worms from Team17
Summary(pl):	Wolnodostêpny klon Worms z Team17
Name:		wormux
Version:	0.7
Release:	0.beta2.1
License:	BSD
Group:		Applications/Games
Source0:	http://download.gna.org/wormux/wormux-%{version}beta2.tar.bz2
# Source0-md5:	b9a93bbd732f52d2fbff8a403259fcf6
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.wormux.org/en/index.php
BuildRequires:	SDL-devel >= 1.2.6
BuildRequires:	SDL_gfx-devel >= 2.0.13
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
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

%description -l pl
Wolnodostêpny klon gry Worms z Team17.

%prep
%setup -q -n wormux-%{version}beta2

# let *.mo build
rm -f po/stamp-po

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure 
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
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/wormux
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
