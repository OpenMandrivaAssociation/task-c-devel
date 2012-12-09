Name: task-c-devel
Version: 2012.1
Release: 2
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
Requires: slang-devel
Requires: libtool
Requires: zlib-devel
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


%changelog
* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 2012.0-2mdv2012.0
+ Revision: 783343
- Rebuild due to libslang-devel no longer provided by any package.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 2012.0-1
+ Revision: 779399
- Update libz-devel requires.
- Convert pt_BR description to utf-8.
- Update version to match distro version.

* Tue Apr 19 2011 Antoine Ginies <aginies@mandriva.com> 2011.0-1
+ Revision: 655948
- bumpo to 2011 release

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2009.0-4mdv2011.0
+ Revision: 607976
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2009.0-3mdv2010.1
+ Revision: 524164
- rebuilt for 2010.1

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.0-2mdv2010.0
+ Revision: 423754
- rebuild

* Mon Sep 08 2008 Thierry Vignaud <tv@mandriva.org> 2009.0-1mdv2009.0
+ Revision: 282559
- bump version

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 2007-4mdv2009.0
+ Revision: 261377
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2007-3mdv2009.0
+ Revision: 254125
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 2007-1mdv2008.1
+ Revision: 140918
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Aug 04 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-08-04 14:58:59 (51793)
- update version to 2007

* Fri Aug 04 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-08-04 14:57:26 (51789)
- import task-c-devel-2006-1mdk

* Fri Jul 29 2005 Andreas Hasenack <andreas@mandriva.com> 2006-1mdk
- packaged for Mandriva

