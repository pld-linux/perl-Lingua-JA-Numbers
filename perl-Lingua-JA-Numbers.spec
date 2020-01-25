#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Lingua
%define	pnam	JA-Numbers
Summary:	Lingua::JA::Numbers - converts numeric values into their Japanese string equivalents and vice versa
Summary(pl.UTF-8):	Lingua::JA::Numbers - zamiana wartości liczbowych na japońskie odpowiedniki i odwrotnie
Name:		perl-Lingua-JA-Numbers
Version:	0.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DANKOGAI/Lingua-JA-Numbers-%{version}.tar.gz
# Source0-md5:	de7398b3207d0e97fdb48cb1b43f371d
URL:		http://search.cpan.org/dist/Lingua-JA-Numbers/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module converts Japanese text in UTF-8 (or romaji in ASCII) to
number, AND vice versa.

Do not be confused with Lingua::JA::Number by Mike Schilli. This
module is far more comprehensive. As of 0.03, it even does its
to_string() upon request.

%description -l pl.UTF-8
Ten moduł zamienia japoński tekst w UTF-8 (lub romaji w ASCII) na
liczby i odwrotnie.

Nie należy mylić go z Lingua::JA::Number autorstwa Mike'a Schilli. Ten
moduł jest dużo bardziej obszerny. Od wersji 0.03 nawet wywołuje na
żądanie to_string().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Lingua/JA
%{perl_vendorlib}/Lingua/JA/*.pm
%{_mandir}/man3/*
