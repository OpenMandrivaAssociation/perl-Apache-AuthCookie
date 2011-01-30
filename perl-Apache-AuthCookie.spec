%define upstream_name	 Apache-AuthCookie
%define upstream_version 3.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl Authentication and Authorization via cookies
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	apache-mod_perl
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-CGI
BuildRequires:	perl(Apache::Test) >= 1.25
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Apache::AuthCookie allows you to intercept a user's first unauthenticated
access to a protected document. The user will be presented with a custom
form where they can enter authentication credentials. The credentials are
posted to the server where AuthCookie verifies them and returns a session
key.

The session key is returned to the user's browser as a cookie. As a cookie,
the browser will pass the session key on every subsequent accesses.
AuthCookie will verify the session key and re-authenticate the user.

All you have to do is write a custom module that inherits from AuthCookie.
See the POD documentation for more details.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
export APACHE_TEST_HTTPD=%{_sbindir}/httpd
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Apache
%{perl_vendorlib}/Apache2
%{_mandir}/*/*
