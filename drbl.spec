# TODO
# - use pld memtest, syslinux, etc binaries in pkg/
# - code itself seems to be noarch
# - re-add pld support (why it was removed, huh?)
# - more FHS thing (config to /etc)
Summary:	DRBL (Diskless Remote Boot in Linux) package
Name:		drbl
Version:	1.10.31
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/drbl/drbl_stable/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	8e5dce6822336b7d1a6672849de84827
URL:		http://www.drbl.org/
BuildRequires:	bash
BuildRequires:	sed >= 4.0
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

grep -rl /opt/drbl/ . | xargs sed -i -e 's,/opt/drbl,%{_libdir}/%{name},g'

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	maindir=%{_libdir}/%{name} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/setup
%{_libdir}/%{name}/conf
%{_libdir}/%{name}/lang
%{_libdir}/%{name}/pkg
%{_libdir}/%{name}/pki
%{_libdir}/%{name}/image
%{_libdir}/%{name}/doc
%{_libdir}/%{name}/sbin
%{_libdir}/%{name}/bin
%{_datadir}/gdm/themes/drbl-gdm
