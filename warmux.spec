Summary:	A free (libre) clone of Worms from Team17
Name:		wormux
Version:	0.2.3
Release:	1
License:	BSD
Group:		Applications/Games
Source0:	http://download.gna.org/wormux/%{name}-src-%{version}.tgz
# Source0-md5:	a4634a2c85b306acb7e131dba8553589
URL:		http://www.haypocalc.com/wormux/en/index.php
BuildRequires:	ClanLib-devel >= 0.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free (libre) clone of Worms from Team17.

%prep
%setup -q -n %{name}

%build
cd src
%{__make} exec \
	RELEASE=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
