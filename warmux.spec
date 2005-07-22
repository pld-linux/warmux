Summary:	A free (libre) clone of Worms from Team17
Summary(pl):	Wolnodostêpny klon Worms z Team17
Name:		wormux
Version:	0.5.1
Release:	1
License:	BSD
Group:		Applications/Games
Source0:	http://download.gna.org/wormux/%{name}-src-%{version}.tar.bz2
# Source0-md5:	68eae1190569c155995e29aa8a97f710
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.wormux.org/en/index.php
BuildRequires:	ClanLib-OpenGL-devel >= 0.7.0
BuildRequires:	ClanLib-Vorbis-devel >= 0.7.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libxml++1-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free (libre) clone of Worms from Team17.

%description -l pl
Wolnodostêpny klon gry Worms z Team17.

%prep
%setup -q

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
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
