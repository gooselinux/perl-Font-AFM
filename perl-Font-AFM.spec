Name:           perl-Font-AFM
Version:        1.20
Release: 	3.1%{?dist}
Summary:        Perl interface to Adobe Font Metrics files

Group: 		Development/Libraries
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Font-AFM/
Source0:	http://www.cpan.org/authors/id/G/GA/GAAS/Font-AFM-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:	%{_datadir}/a2ps/afm/phvr.afm

%description
Interface to Adobe Font Metrics files

%prep
%setup -q -n Font-AFM-%{version}
# We don't have Helvetica, use phvr.afm instead
sed -i -e 's,Helvetica,phvr,g' t/afm.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test METRICS=%{_datadir}/a2ps/afm

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Font
%{_mandir}/man3/Font*

%changelog
* Fri Jan 22 2010 Dennis Gregorovic <dgregor@redhat.com> - 1.20-3.1
- Rebuilt for RHEL 6
Related: rhbz#543948

* Thu Jul 02 2009 Jeff Fearn <jfearn@redhat.com> - 1.20-3
- bump for RHEL

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jun 10 2008 Ralf Corsépius <rc040203@freenet.de> - 1.20-1
- Upstream update.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.19-7
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.19-6
- rebuild for new perl

* Fri Aug 31 2007 Ralf Corsépius <rc040203@freenet.de> - 1.19-5
- BR: perl(ExtUtils::MakeMaker).
- Update license tag.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.19-4
- Mass rebuild.

* Tue Feb 28 2006 Ralf Corsépius <rc040203@freenet.de> - 1.19-3
- Rebuild for perl-5.8.8.

* Sun Aug 21 2005 Ralf Corsepius <ralf@links2linux.de>	- 1.19-3
- Changelog cleanup.

* Sun Aug 21 2005 Ralf Corsepius <ralf@links2linux.de>	- 1.19-2
- Review feedback.

* Thu Aug 18 2005 Ralf Corsepius <ralf@links2linux.de>	- 1.19-1
- FE submission.
