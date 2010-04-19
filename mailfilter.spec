%define name mailfilter
%define version 0.8.2
%define release %mkrel 2

Name: %{name}
Version: %{version}
Release: %{release}
Summary: A program that filters your incoming e-mail to help remove spam
License: GPL
Group: Networking/Mail
Source: http://downloads.sourceforge.net/project/mailfilter/Mailfilter/%{version}/%{name}-%{version}.tar.gz
Patch0: mailfilter-0.8.2-gcc44.patch
Patch1: mailfilter-0.8.2-openssl.patch
Buildrequires: byacc bison flex libopenssl-devel
Buildroot: %{_tmppath}/%{name}-buildroot
URL: http://mailfilter.sourceforge.net/

%description
Mailfilter is very flexible utility for UNIX (-like) operating systems to get
rid of unwanted e-mail messages, before having to go through the trouble of
downloading them to the local computer. It offers support for one or many
POP3 accounts and is especially useful for dialup connections via modem,
ISDN, etc. Install Mailfilter if you'd like to remove spam from your POP3 mail
accounts.

%prep
%setup -q
%patch0 -p1 -b .gcc44
%patch1 -p0 -b .openssl

%build
%configure2_5x
make

%install
rm -fr %buidlroot
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS
%doc doc/FAQ 
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*


