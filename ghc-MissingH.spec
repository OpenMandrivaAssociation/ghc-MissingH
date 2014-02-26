%global debug_package %{nil}
%define module MissingH

Summary:	Large utility library for Haskell
Name:		ghc-%{module}
Version:	1.2.0.0
Release:	3
License:	BSD
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	haskell(HUnit)
BuildRequires:	haskell(hslogger)
BuildRequires:	haskell(network)
BuildRequires:	haskell(parsec)
BuildRequires:	haskell(random)
BuildRequires:	haskell(regex-compat)
Requires(post,preun):	ghc
Obsoletes:	haskell-%{module} < 1.2.0.0-3

%description
MissingH is a library of all sorts of utility functions for Haskell
programmers. It is written in pure Haskell and thus should be extremely
portable and easy to use.

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build


%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

