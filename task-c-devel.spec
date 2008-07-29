
# THIS PACKAGE IS STORED IN SVN
# PLEASE DO NOT UPLOAD WITHOUT
# COMMITTING YOUR CHANGES FIRST

Name: task-c-devel
Version: 2007
Release: %mkrel 3
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
Requires: glib2-devel
Requires: glibc-devel
Requires: libslang-devel
Requires: libtool
Requires: libz-devel
Requires: m4
Requires: make
Requires: ncurses-devel
Requires: patch
Requires: texinfo
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

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
%defattr(0644,root,root,0755)



