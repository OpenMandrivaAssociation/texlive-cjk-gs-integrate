Name:		texlive-cjk-gs-integrate
Version:	59705
Release:	1
Summary:	Tools to integrate CJK fonts into Ghostscript
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cjk-gs-integrate
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk-gs-integrate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk-gs-integrate.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk-gs-integrate.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This script searches a list of directories for CJK fonts, and
makes them available to an installed Ghostscript. In the
simplest case, with sufficient privileges, a run without
arguments should result in a complete setup of Ghostscript.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/fonts/cjk-gs-integrate
%{_texmfdistdir}/texmf-dist/scripts/cjk-gs-integrate
%{_texmfdistdir}/texmf-dist/fonts/misc/cjk-gs-integrate
%doc %{_texmfdistdir}/texmf-dist/doc/fonts/cjk-gs-integrate

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
