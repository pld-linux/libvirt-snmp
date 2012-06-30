Summary:	SNMP API for libvirt
Summary(pl.UTF-8):	API SNMP do libvirt
Name:		libvirt-snmp
Version:	0.0.2
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	ftp://libvirt.org/libvirt/snmp/%{name}-%{version}.tar.gz
# Source0-md5:	8fc59a917ce73bc37728c06be7c258a4
URL:		http://libvirt.org/
BuildRequires:	libvirt-devel
BuildRequires:	net-snmp-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libvirt-snmp provides SNMP functionality for libvirt. Therefore it is
now possible to gather and set domain status over SNMP from one place.
This allows to create views of entire platforms end to end.

%description -l pl.UTF-8
Libvirt-snmp udostępnia funkcjonalność SNMP dla libvirt. Dzięki temu
można pobierać i ustawiać stan domen z jednego miejsca poprzez SNMP.
Pozwala to na tworzenie widoków całych platform.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/libvirtMib_subagent
%{_datadir}/snmp/mibs/LIBVIRT-MIB.txt
%{_mandir}/man1/libvirtMib_subagent.1*
