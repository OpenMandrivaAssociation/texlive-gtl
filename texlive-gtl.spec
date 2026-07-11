%global tl_name gtl
%global tl_revision 69297

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Manipulating generalized token lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/gtl
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gtl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gtl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gtl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides tools for simple operations on lists of tokens
which are not necessarily balanced. It is in particular used a lot in
the unravel package, to go through tokens one at a time rather than
having to work with entire braced groups at a time.

