%include	/usr/lib/rpm/macros.php
%define		_class		Console
%define		_subclass	Getargs
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a command-line arguments parser
Summary(pl):	%{_pearname} - przetwarzanie argumentów linii poleceñ
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3ee70869037a50bdde6e8814b1455961
URL:		http://pear.php.net/package/Console_Getargs/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

%description -l pl
Pakiet Console_Getargs ma zaimplementowan± obs³ugê parsowania
argumentów linii poleceñ, któr± mo¿na u¿yæ w aplikacjach do
przetworzenia argumentów znalezionych w $_SERVER['argv']. Wykonuje
podstawowe sprawdzanie poprawno¶ci argumentów i jest w stanie zwróciæ
u¿ytkownikowi sformatowany tekst pomocy na podstawie podanej
konfiguracji.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
