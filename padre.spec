%define upstream_name    Padre
%define appli_name       padre
%define upstream_version 0.96

Name:		%{appli_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

License:	GPLv1+ or Artistic
Group:		Development/Perl
Summary:	Perl Application Development and Refactoring Environment
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SZ/SZABGAB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Alien::wxWidgets)          >= 0.460.0
BuildRequires:	perl(App::Ack)
BuildRequires:	perl(App::cpanminus) >= 0.992.3
BuildRequires:	perl(Capture::Tiny) >= 0.060.0
BuildRequires:	perl(Class::Adapter) >= 1.050
BuildRequires:	perl(Class::Inspector) >= 1.220
BuildRequires:	perl(Class::Unload)  >= 0.030
BuildRequires:	perl(Class::XSAccessor) >= 1.050
BuildRequires:	perl(Cwd)               >= 3.270.100
BuildRequires:	perl(DBD::SQLite) >= 1.270.0
BuildRequires:	perl(DBI) >= 1.580.0
BuildRequires:	perl(Data::Dumper) >= 2.101
BuildRequires:	perl(Debug::Client) >= 0.110
BuildRequires:	perl(Devel::Dumpvar) >= 0.040
BuildRequires:	perl(Devel::Refactor) >= 0.05
BuildRequires:	perl(Digest::MD5) >= 2.380
BuildRequires:	perl(Encode) >= 2.260
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.560.0
BuildRequires:	perl(ExtUtils::Manifest) >= 1.560.0
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy::Recursive) >= 0.370
BuildRequires:	perl(File::Find::Rule) >= 0.300
BuildRequires:	perl(File::Glob)
BuildRequires:	perl(File::HomeDir) >= 0.910
BuildRequires:	perl(File::Path) >= 2.080
BuildRequires:	perl(File::Remove) >= 1.400
BuildRequires:	perl(File::ShareDir) >= 1.0
BuildRequires:	perl(File::ShareDir::PAR)
BuildRequires:	perl(File::Spec) >= 3.270.100
BuildRequires:	perl(File::Spec::Functions) >= 3.270.1
BuildRequires:	perl(File::Temp) >= 0.200
BuildRequires:	perl(File::Which) >= 1.080
BuildRequires:	perl(File::pushd) >= 1.0
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Format::Human::Bytes) >= 0.060
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(HTML::Entities) >= 3.570
BuildRequires:	perl(HTML::Parser) >= 3.580
BuildRequires:	perl(IO::Scalar) >= 2.110
BuildRequires:	perl(IO::Socket) >= 1.300
BuildRequires:	perl(IO::String) >= 1.080
BuildRequires:	perl(IPC::Open2)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl(JSON::XS) >= 2.290 
BuildRequires:	perl(LWP) >= 5.815
BuildRequires:	perl(LWP::UserAgent) 
BuildRequires:	perl(List::MoreUtils) >= 0.220 
BuildRequires:	perl(List::Util) >= 1.180
BuildRequires:	perl(Locale::Msgfmt) 
BuildRequires:	perl(Module::Build) >= 0.360.3
BuildRequires:	perl(Module::CoreList)
BuildRequires:	perl(Module::Install) 
BuildRequires:	perl(Module::Manifest) >= 0.080
BuildRequires:	perl(Module::Refresh) >= 0.130
BuildRequires:	perl(Module::Starter) >= 1.500
BuildRequires:	perl(ORLite) >= 1.480
BuildRequires:	perl(ORLite::Migrate)
BuildRequires:	perl(PAR)
BuildRequires:	perl(POD2::Base) >= 0.043
BuildRequires:	perl(POSIX)
BuildRequires:	perl(PPI) >= 1.213
BuildRequires:	perl(PPIx::EditorTools) >= 0.130
BuildRequires:	perl(PPIx::Regexp) >= 0.011
BuildRequires:	perl(Params::Util) >= 0.330
BuildRequires:	perl(Parse::ErrorString::Perl) >= 0.140
BuildRequires:	perl(Parse::ExuberantCTags) >= 1.0
BuildRequires:	perl(Pod::Abstract) >= 0.160
BuildRequires:	perl(Pod::Functions)
BuildRequires:	perl(Pod::POM) >= 0.170
BuildRequires:	perl(Pod::Perldoc)              >= 3.150.0
BuildRequires:	perl(Pod::Simple) >= 3.070
BuildRequires:	perl(Pod::Simple::XHTML) >= 3.040
BuildRequires:	perl(Probe::Perl)
BuildRequires:	perl(Storable) >= 2.150
BuildRequires:	perl(Template::Tiny) >= 0.110
BuildRequires:	perl(Term::ReadLine)
BuildRequires:	perl(Text::Balanced)                >= 2.010
BuildRequires:	perl(Text::Diff)                >= 0.350.0
BuildRequires:	perl(Text::FindIndent) >= 0.100
BuildRequires:	perl(Test::Exception)           >= 0.310
BuildRequires:	perl(Time::HiRes)           >= 1.971.800
BuildRequires:	perl(Test::MockObject)          >= 1.090.0
BuildRequires:	perl(Test::More)                >= 0.880.0
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::NeedsDisplay)
BuildRequires:	perl(Test::NoWarnings)          >= 0.084.0
BuildRequires:	perl(Test::Script)              >= 1.070.0
BuildRequires:	perl(Thread::Queue)             >= 2.110.0
BuildRequires:	perl(URI)
BuildRequires:	perl(Wx) >= 0.910
BuildRequires:	perl(Wx::Perl::ProcessStream) >= 0.290
BuildRequires:	perl(YAML::Tiny) >= 1.320
BuildRequires:	perl(threads)                   >= 1.710.0
BuildRequires:	perl(threads::shared)           >= 1.330.0

BuildArch: noarch

Requires:	gettext
# not auto-detected but required
Requires:	perl(Alien::wxWidgets)
Requires:	perl(Class::Adapter::Builder)
Requires:	perl(File::pushd)
Requires:	perl(Text::FindIndent)
Requires:	perl(Probe::Perl)
Requires:	perl(Template::Tiny)

Obsoletes:	perl-Padre-Plugin-Encode <= 0.1.3
Provides:	perl-Padre-Plugin-Encode = %{EVRD}

Obsoletes:	perl-Wx-Perl-Dialog <= 0.04
Provides:	perl-Wx-Perl-Dialog = %{EVRD}

Obsoletes:	perl-Padre <= 0.400.0
Provides:	perl-Padre = %{EVRD}

Provides:	perl-Padre-Wx-Panel-FoundInFiles = %{EVRD}
Provides:	perl(Padre::Wx::Dialog) = %{EVRD}

Suggests: perl(Padre::Plugin::Autoformat)
Suggests: perl(Padre::Plugin::CSS)
Suggests: perl(Padre::Plugin::Catalyst)
Suggests: perl(Padre::Plugin::ClassSniff)
Suggests: perl(Padre::Plugin::DataWalker)
Suggests: perl(Padre::Plugin::Ecliptic)
Suggests: perl(Padre::Plugin::Git)
Suggests: perl(Padre::Plugin::HTML)
Suggests: perl(Padre::Plugin::Kate)
Suggests: perl(Padre::Plugin::Nopaste)
Suggests: perl(Padre::Plugin::PAR)
Suggests: perl(Padre::Plugin::Parrot)
Suggests: perl(Padre::Plugin::Perl6)
Suggests: perl(Padre::Plugin::PerlCritic)
Suggests: perl(Padre::Plugin::PerlTidy)
Suggests: perl(Padre::Plugin::SpellCheck)
Suggests: perl(Padre::Plugin::Swarm)
Suggests: perl(Padre::Plugin::ViewInBrowser)

%description
Padre - Perl Application Development and Refactoring Environment

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod a-x share/%{name}.desktop

%build
DISPLAY= perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#DISPLAY= %make test

%install
%makeinstall_std

# menu-entry
%__mkdir_p  %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Name=Padre
Comment=The Perl IDE
Exec=padre
Icon=%{perl_vendorlib}/auto/share/dist/%{upstream_name}/icons/padre/64x64/logo.png
Categories=Development;Perl;IDE;
Terminal=false
EOF

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc Changes README
%{_bindir}/padre
%{_mandir}/man3/*
%{_datadir}/applications/%{name}.desktop
%{perl_vendorlib}/%{upstream_name}
%{perl_vendorlib}/%{upstream_name}.pm
%dir %{perl_vendorlib}/auto/share/dist/%{upstream_name}
%dir %{perl_vendorlib}/auto/share/dist/%{upstream_name}/locale
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/doc
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/examples
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/icons
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/languages
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/padre.desktop
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/padre.desktop.README
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/padre-splash-ccnc.png
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/padre-splash.png
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/ppm
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/README.txt
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/templates
%{perl_vendorlib}/auto/share/dist/%{upstream_name}/themes

