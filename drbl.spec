# TODO
# - use pld memtest, syslinux, etc binaries in pkg/
# - code itself seems to be noarch
# - re-add pld support (why it was removed, huh?)
# - more FHS thing (config to /etc)
Summary:	DRBL (Diskless Remote Boot in Linux) package
Name:		drbl
Version:	2.1.33
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://free.nchc.org.tw/drbl-core/src/unstable/%{name}-%{version}.tar.bz2
# Source0-md5:	ab5d805195c72b7638019a1259b682b8
URL:		http://www.drbl.org/
BuildRequires:	bash
Requires:	findutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DRBL provides a diskless or systemless environment for client
machines. It works on Debian, Ubuntu, Mandriva, Red Hat, Fedora,
CentOS and OpenSuSE. DRBL uses distributed hardware resources and
makes it possible for clients to fully access local hardware. It also
includes Clonezilla, a partition and disk cloning utility similar to
Symantec Ghost(TM) or True Image(TM).

%prep
%setup -q -n %{name}-%{version}

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir /etc/drbl
/etc/drbl/*
%attr(755,root,root) /usr/sbin/*
%attr(755,root,root) /usr/bin/*
%{_datadir}/gdm/themes/drbl-gdm
%defattr(-,root,root,-)
%{_datadir}/drbl
