Name: task-c-devel
Version: 2015.0
Release: 0.10
License: GPL
Summary: Metapackage for C development
Summary(pt_BR): Metapacote para desenvolvimento em C
Group: Development/C
Requires: autoconf
Requires: automake
Requires: binutils
Requires: bison
Requires: byacc
Requires: gcc-cpp
Requires: ctags
Requires: diffutils
Requires: flex
Requires: gcc
Requires: pkgconfig(glib-2.0)
Requires: glibc-devel
Requires: pkgconfig(slang)
Requires: libtool
Requires: pkgconfig(zlib)
Requires: m4
Requires: make
Requires: pkgconfig(ncurses)
Requires: patch
Requires: texinfo
BuildArch: noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for a complete environment for development of programs in
the C programming language.
It itself includes no software, only dependencies on software.

%description -l pt_BR
Este pacote é um metapacote, ou seja, o seu único propósito é conter
dependências para um completo ambiente de desenvolvimento de programas em C.

Este pacote não inclui nenhum programa, apenas dependências para outros
programas.

%files
