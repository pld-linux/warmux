Summary:	A free (libre) clone of Worms from Team17
Summary(pl):	Wolnodostêpny klon Worms z Team17
Name:		wormux
Version:	0.2.3
Release:	2
License:	BSD
Group:		Applications/Games
Source0:	http://download.gna.org/wormux/%{name}-src-%{version}.tgz
# Source0-md5:	a4634a2c85b306acb7e131dba8553589
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.haypocalc.com/wormux/en/index.php
BuildRequires:	ClanLib-devel >= 0.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free (libre) clone of Worms from Team17.

%description -l pl
Wolnodostêpny klon gry Worms z Team17.

%prep
%setup -q -n %{name}

%build
%{__make} -C src exec \
	RELEASE=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name},%{_desktopdir},%{_pixmapsdir}}

%{__make} -C src config_install \
	DIR=$RPM_BUILD_ROOT

# Here patch is useless
mv src/constante.cpp src/constante.old
sed -e "s!REPERTOIRE_INSTALL(.*)!REPERTOIRE_INSTALL(\"/usr/\")!" \
	src/constante.old > src/constante.cpp

%{__make} -C src install \
	DIR_BIN=$RPM_BUILD_ROOT%{_bindir} \
	DIR_SHARE=$RPM_BUILD_ROOT%{_datadir}/games/%{name}/	# Makefile needs trailing slash (maybe patch will be better?)

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wormux
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
