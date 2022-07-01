#
# Conditional build:
%bcond_with	tests	# unit tests

Summary:	TPM (Trusted Platform Module) 2.0 tools based on tpm2-tss
Summary(pl.UTF-8):	Narzędzia TPM (Trusted Platform Module) 2.0 oparte o tpm2-tss
Name:		tpm2-tools
Version:	5.2
Release:	1
License:	BSD
Group:		Applications/System
#Source0Download: https://github.com/tpm2-software/tpm2-tools/releases
Source0:	https://github.com/tpm2-software/tpm2-tools/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0057615ef43b9322d4577fc3bde0e8d6
URL:		https://github.com/tpm2-software/tpm2-tools
BuildRequires:	curl-devel
BuildRequires:	efivar-devel
BuildRequires:	openssl-devel >= 1.1.0
BuildRequires:	pandoc
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	tpm2-tss-devel >= 3.0.0
%if %{with tests}
BuildRequires:	cmocka-devel
BuildRequires:	expect
# for ss
BuildRequires:	iproute2
BuildRequires:	openssl-tools
BuildRequires:	python-PyYAML
BuildRequires:	tpm2-abrmd
BuildRequires:	xxd
# tpm-simulator: swtpm or tpm_server
%endif
Requires:	tpm2-tss >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TPM (Trusted Platform Module) 2.0 tools based on tpm2-tss.

%description -l pl.UTF-8
Narzędzia TPM (Trusted Platform Module) 2.0 oparte o tpm2-tss.

%package -n bash-completion-tpm2-tools
Summary:	Bash completion for tpm2 tools
Summary(pl.UTF-8):	Bashowe dopełnianie poleceń tpm2 tools
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-tpm2-tools
Bash completion for tpm2 tools.

%description -n bash-completion-tpm2-tools -l pl.UTF-8
Bashowe dopełnianie poleceń tpm2 tools.

%prep
%setup -q

%build
%configure \
	SS=/sbin/ss \
	%{?with_tests:--enable-unit} \
	--disable-silent-rules \
	--with-bashcompdir=%{bash_compdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS.md,CHANGELOG.md,LICENSE,MAINTAINERS.md,README.md}
%attr(755,root,root) %{_bindir}/tpm2
%attr(755,root,root) %{_bindir}/tpm2_*
%attr(755,root,root) %{_bindir}/tss2
%attr(755,root,root) %{_bindir}/tss2_*
%{_mandir}/man1/tpm2.1*
%{_mandir}/man1/tpm2_*.1*
%{_mandir}/man1/tss2_*.1*

%files -n bash-completion-tpm2-tools
%defattr(644,root,root,755)
%{bash_compdir}/tpm2
%{bash_compdir}/tpm2_completion.bash
%{bash_compdir}/tss2
%{bash_compdir}/tss2_*
