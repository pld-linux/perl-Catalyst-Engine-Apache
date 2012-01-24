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
Summary(pl.UTF-8):	Catalyst::Engine::Apache - silniki Apache'a dla Catalysta
Name:		perl-Catalyst-Engine-Apache
Version:	1.16
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7a7241dadd7c0eb28ce10aeb90c9944e
URL:		http://search.cpan.org/dist/Catalyst-Engine-Apache/
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

%description -l pl.UTF-8
Ten pakiet zawiera silnik Catalysta wykorzystujący mod_perla
(Apache 2.x).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# Makefile.PL turns on only t/0*.t; we're running all, and one test depends on this file
if [ ! -e t/01use.t ]; then
cat <<EOF>t/01use.t
	use Test::More tests=>1;
	ok(1);
EOF
fi

%build
%{__perl} -MExtUtils::MakeMaker -we 'WriteMakefile(NAME=>"Catalyst::Engine::Apache")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

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
