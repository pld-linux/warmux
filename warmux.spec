Summary:	A free (libre) clone of Worms from Team17
Summary(pl):	Wolnodostêpny klon Worms z Team17
Name:		wormux
Version:	0.4.0
Release:	2
License:	BSD
Group:		Applications/Games
Source0:	http://download.gna.org/wormux/%{name}-src-%{version}.tgz
# Source0-md5:	14f7b9c9b3f2fba7eb20afbf2deb219e
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-fix-install-dir.patch
URL:		http://www.haypocalc.com/wormux/en/index.php
BuildRequires:	ClanLib-Vorbis-devel >= 0.6.0
BuildRequires:	gettext-devel
BuildRequires:	libxml++-devel >= 2.6.0
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free (libre) clone of Worms from Team17.

%description -l pl
Wolnodostêpny klon gry Worms z Team17.

%prep
%setup -q -n %{name}
%patch0 -p1

%{__perl} -pi -e 's/libxml\+\+-1\.0/libxml++-2.6/' src/Makefile src/make.env
%{__perl} -pi -e 's/-O3/%{rpmcflags}/' src/make.env

%build
%{__make} -C src \
	RELEASE=1 \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name},%{_desktopdir},%{_pixmapsdir},%{_datadir}/locale}

%{__make} -C src install \
	DIR_SHARE_PLD=%{_datadir}/games/%{name}/ \
	DIR_BIN=$RPM_BUILD_ROOT%{_bindir} \
	DIR_SHARE=$RPM_BUILD_ROOT%{_datadir}/games/%{name}/	# Makefile needs trailing slash (maybe patch will be better?)

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

cp -ar locale/* $RPM_BUILD_ROOT%{_datadir}/locale
find $RPM_BUILD_ROOT%{_datadir}/locale -name \*.po -exec rm {} \;

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.txt BUGS.txt CHANGELOG.txt FAQ.txt HACKERS.txt README.txt TODO.txt doc
%attr(755,root,root) %{_bindir}/wormux
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
