# TODO
# - use pld memtest, syslinux, etc binaries in pkg/
# - re-add pld support (why it was removed, huh?)
# - clean up docdir (i.a. compress docs)
Summary:	DRBL (Diskless Remote Boot in Linux) package
Name:		drbl
Version:	2.19.11
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/drbl/drbl_stable/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	feeb119d9ab7116b29047cdf53fa4ed1
URL:		http://www.drbl.org/
BuildRequires:	bash
BuildRequires:	sed >= 4.0
Requires:	findutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DRBL provides a diskless or systemless environment for client
machines. It works on Debian, Ubuntu, Mandriva, Red Hat, Fedora,
CentOS and OpenSuSE. DRBL uses distributed hardware resources and
makes it possible for clients to fully access local hardware. It also
includes Clonezilla, a partition and disk cloning utility similar to
Symantec Ghost(TM) or True Image(TM).

%package gdm-theme
Summary:        GDM theme for DRBL
Group:          Themes
Requires:	%{name}
Requires:	gdm-theme
BuildArch:	noarch

%description gdm-theme
GDM theme for DRBL

%prep
%setup -q -n %{name}-%{version}

grep -rl /opt/drbl/ . | xargs sed -i -e 's,/opt/drbl,%{_libdir}/%{name},g'

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	maindir=%{_libdir}/%{name} \
	DESTDIR=$RPM_BUILD_ROOT

%{__install} -d $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}-%{version}/examples
%{__mv} $RPM_BUILD_ROOT/%{_datadir}/%{name}/doc/* $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}-%{version}/
%{__mv} $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/*.example $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}-%{version}/examples/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%{_defaultdocdir}/%{name}-%{version}
%{_sysconfdir}/%{name}
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/%{name}/setup
%{_datadir}/%{name}/lang
%{_datadir}/%{name}/pkg
%{_datadir}/%{name}/pki
%{_datadir}/%{name}/image
%{_datadir}/%{name}/sbin
%{_datadir}/%{name}/bin

%files gdm-theme
%defattr(644,root,root,755)
%defattr(-,root,root,-)
%{_datadir}/gdm/themes/drbl-gdm
