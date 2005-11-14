#
# Sorry, only Apache2 version...
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Engine-Apache
Summary:	Catalyst::Engine::Apache - Catalyst Apache Engines
#Summary(pl):	
Name:		perl-Catalyst-Engine-Apache
Version:	0.99002
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	636cb5481d927a03650a81ff7eb0fe54
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.49_02
%endif
Conflicts:	perl-Catalyst < 5.49
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These classes provide mod_perl (Apache 2) support for Catalyst.

%description -l pl
Ten pakiet zawiera silnik Catalysta wykorzystuj�cy mod_perla
(Apache 2.x).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Engine/*.pm
%dir %{perl_vendorlib}/Catalyst/Engine/Apache2
%{perl_vendorlib}/Catalyst/Engine/Apache2/MP20.pm
%exclude %{_mandir}/man3/*MP19*
%{_mandir}/man3/Catalyst::Engine::Apache.*
%{_mandir}/man3/Catalyst::Engine::Apache2*