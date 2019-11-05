%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Console_Getargs
Summary:	%{_pearname} - a command-line arguments parser
Summary(pl.UTF-8):	%{_pearname} - przetwarzanie argumentów linii poleceń
Name:		php-pear-%{_pearname}
Version:	1.4.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f99266907369af0191ea32f25dc6317e
URL:		http://pear.php.net/package/Console_Getargs/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.1.0
Requires:	php-pear
Obsoletes:	php-pear-Console_Getargs-tests
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

%prep
%pear_package_setup

mv docs/%{_pearname}/examples .

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Console/Getargs.php

%{_examplesdir}/%{name}-%{version}
