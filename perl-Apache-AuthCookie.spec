%define upstream_name	 Apache-AuthCookie
%define upstream_version 3.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl Authentication and Authorization via cookies
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	apache-mod_perl
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-CGI
BuildRequires:	perl(Apache::Test) >= 1.25
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#export APACHE_TEST_HTTPD=%{_sbindir}/httpd
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Apache
%{perl_vendorlib}/Apache2
%{_mandir}/*/*
