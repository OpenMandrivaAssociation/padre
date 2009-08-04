%define upstream_name    Padre
%define appli_name       padre
%define upstream_version 0.42

Name:       %{appli_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Perl Application Development and Refactoring Environment
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/S/SZ/SZABGAB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Capture::Tiny)
BuildRequires: perl(Class::Unload)
BuildRequires: perl(Class::XSAccessor::Array)
BuildRequires: perl(Cwd)                       >= 3.270.100
BuildRequires: perl(Devel::Dumpvar)
BuildRequires: perl(Encode)                    >= 2.260.0
BuildRequires: perl(Locale::Msgfmt) 
BuildRequires: perl(Module::Build) 
BuildRequires: perl(Module::Install) 
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::ShareDir::PAR)
BuildRequires: perl(File::Spec)                >= 3.270.100
BuildRequires: perl(File::Which)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(IO::String)
BuildRequires: perl(Module::Refresh)
BuildRequires: perl(Module::Starter)
BuildRequires: perl(ORLite)
BuildRequires: perl(ORLite::Migrate)
BuildRequires: perl(PAR)
BuildRequires: perl(PPI)
BuildRequires: perl(PPIx::EditorTools)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Parse::ErrorString::Perl)
BuildRequires: perl(Pod::Abstract)
BuildRequires: perl(Pod::POM)
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Pod::Simple::XHTML)
BuildRequires: perl(Probe::Perl)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)                >= 0.880.0
BuildRequires: perl(Test::Most)
BuildRequires: perl(Test::Script)
BuildRequires: perl(Test::NeedsDisplay)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Text::FindIndent)
BuildRequires: perl(Thread::Queue)
BuildRequires: perl(URI)
BuildRequires: perl(Wx)
BuildRequires: perl(Wx::Perl::ProcessStream)
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
