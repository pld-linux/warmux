Summary:	A free (libre) clone of Worms from Team17
Summary(pl):	Wolnodostêpny klon Worms z Team17
Name:		wormux
Version:	0.3.1
Release:	2
License:	BSD
Group:		Applications/Games
Source0:	http://download.gna.org/wormux/%{name}-src-%{version}.tgz
# Source0-md5:	b65aef5d76192cac4c61f8dfc1f98a28
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.haypocalc.com/wormux/en/index.php
BuildRequires:	ClanLib-devel >= 0.6.0
BuildRequires:	libxml++-devel >= 2.6.0
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free (libre) clone of Worms from Team17.

%description -l pl
Wolnodostêpny klon gry Worms z Team17.

%prep
%setup -q -n %{name}

%{__perl} -pi -e 's/libxml\+\+-1\.0/libxml++-2.6/' src/Makefile src/make.env
%{__perl} -pi -e 's/-O3/%{rpmcflags}/' src/make.env

%build
%{__make} -C src \
	RELEASE=1 \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name},%{_desktopdir},%{_pixmapsdir}}

%{__make} -C src config_install \
	DIR=$RPM_BUILD_ROOT \
	DIR_OK=%{_usr}/

%{__make} -C src install \
	DIR_BIN=$RPM_BUILD_ROOT%{_bindir} \
	DIR_SHARE=$RPM_BUILD_ROOT%{_datadir}/games/%{name}/	# Makefile needs trailing slash (maybe patch will be better?)

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGELOG.txt BUGS.txt TODO.txt README.txt FAQ.txt HACKERS.txt doc
%attr(755,root,root) %{_bindir}/wormux
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
