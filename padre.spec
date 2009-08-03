%define upstream_name    Padre
%define appli_name       padre
%define upstream_version 0.42

Name:       %{appli_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Perl Application Development and Refactoring Environment
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/S/SZ/SZABGAB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Locale::Msgfmt) 
BuildRequires: perl(Module::Build) 
BuildRequires: perl(Module::Install) 
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(File::Which)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Most)
BuildRequires: perl(Test::NeedsDisplay)
BuildRequires: perl(Test::NoWarnings)
Requires:      gettext
Requires:      perl(Class::Adapter::Builder)
Requires:      perl(Class::Accessor)
Requires:      perl(Class::Unload)
Requires:      perl(Class::XSAccessor::Array)
Requires:      perl(DBD::SQLite)
Requires:      perl(Devel::Dumpvar)
Requires:      perl(Encode)
Requires:      perl(File::Copy::Recursive)
Requires:      perl(File::Find::Rule)
Requires:      perl(File::HomeDir)
Requires:      perl(File::Which)
Requires:      perl(File::pushd)
Requires:      perl(IPC::Cmd)
Requires:      perl(IPC::Run3)
Requires:      perl(Locale::Msgfmt) 
Requires:      perl(Module::CoreList)
Requires:      perl(Module::Refresh)
Requires:      perl(Module::Starter)
Requires:      perl(PAR)
Requires:      perl(Parse::ExuberantCTags)
Requires:      perl-PathTools
Requires:      perl(Probe::Perl)
Requires:      perl(Text::FindIndent)
Requires:      perl(Thread::Queue)
Requires:      perl(Wx::Perl::ProcessStream)
Requires:      perl(threads)
Requires:      perl(threads::shared)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Obsoletes: perl-Padre-Plugin-Encode <= 0.1.3
Provides:  perl-Padre-Plugin-Encode = %{version}

Obsoletes: perl-Wx-Perl-Dialog <= 0.04
Provides:  perl-Wx-Perl-Dialog = %{version}

Obsoletes: perl-Padre <= 0.400.0
Provides:  perl-Padre = %{version}

%description
Padre - Perl Application Development and Refactoring Environment

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/padre
%{_mandir}/man3/*
%perl_vendorlib/*
