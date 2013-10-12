# revision 31306
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-gtl
Version:	20131012
Release:	1
Summary:	TeXLive gtl package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gtl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gtl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gtl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive gtl package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gtl/gtl.sty
%doc %{_texmfdistdir}/doc/latex/gtl/README
%doc %{_texmfdistdir}/doc/latex/gtl/gtl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/gtl/gtl.dtx
%doc %{_texmfdistdir}/source/latex/gtl/gtl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
