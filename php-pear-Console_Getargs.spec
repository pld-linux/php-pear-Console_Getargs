%include	/usr/lib/rpm/macros.php
%define		_class		Console
%define		_subclass	Getargs
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a command-line arguments parser
Summary(pl.UTF-8):	%{_pearname} - przetwarzanie argumentów linii poleceń
Name:		php-pear-%{_pearname}
Version:	1.3.4
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	30c90b46e41e023b7008c5f6306335aa
URL:		http://pear.php.net/package/Console_Getargs/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Console_Getargs package implements a Command Line arguments parser
that your CLI applications can use to parse arguments found in
$_SERVER['argv']. It performs some basic arguments validation and is
capable to return a formatted help text to the user, based on the
configuration it is given.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet Console_Getargs ma zaimplementowaną obsługę parsowania
argumentów linii poleceń, którą można użyć w aplikacjach do
przetworzenia argumentów znalezionych w $_SERVER['argv']. Wykonuje
podstawowe sprawdzanie poprawności argumentów i jest w stanie zwrócić
użytkownikowi sformatowany tekst pomocy na podstawie podanej
konfiguracji.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
