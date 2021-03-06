# based on PLD Linux spec git://git.pld-linux.org/packages/gcc.git
%bcond_with	pass2

%define		mver	4.9
%define		snap	20150204

Summary:	GNU Compiler Collection: the C compiler and shared files
Name:		gcc
Version:	4.9.2
Release:	1.%{snap}.1
Epoch:		6
License:	GPL v3+
Group:		Development/Languages
#Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/%{name}-%{version}.tar.bz2
Source0:	ftp://gcc.gnu.org/pub/gcc/snapshots/%{mver}-%{snap}/%{name}-%{mver}-%{snap}.tar.bz2
# Source0-md5:	5a59c19c4ff7acd3db7f8d94843f7f85
%if %{with pass2}
# for cross build
Source1:	http://www.mpfr.org/mpfr-current/mpfr-3.1.2.tar.xz
# Source1-md5:	e3d203d188b8fe60bb6578dd3152e05c
Source2:	ftp://ftp.gnu.org/gnu/gmp/gmp-6.0.0a.tar.xz
# Source2-md5:	1e6da4e434553d2811437aa42c7f7c76
Source3:	http://multiprecision.org/mpc/download/mpc-1.0.2.tar.gz
# Source3-md5:	68fadff3358fb3e7976c7a398a0af4c3
%endif
Source10:	gcc-optimize-la.pl
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=21704
Patch0:		%{name}-include.patch
Patch1:		%{name}-filename-output.patch
URL:		http://gcc.gnu.org/
%if %{without pass2}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils
BuildRequires:	bison
BuildRequires:	chrpath
BuildRequires:	cloog-devel
BuildRequires:	coreutils
BuildRequires:	flex
BuildRequires:	gettext
BuildRequires:	glibc-devel
BuildRequires:	gmp-devel
BuildRequires:	mpc-devel
BuildRequires:	mpfr-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
%else
BuildRequires:	libstdc++-bootstrap
BuildConflicts:	gmp-devel
BuildConflicts:	mpc-devel
BuildConflicts:	mpfr-devel
%endif
Requires:	binutils
Requires:	cpp = %{epoch}:%{version}-%{release}
Requires:	libgcc = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_slibdir	%{_libdir}
%define		gcclibdir	%{_libdir}/gcc/%{_target_platform}/%{version}

%define		filterout	-fwrapv -fno-strict-aliasing -fsigned-char
# FIXME: unresolved symbols
%define		skip_post_check_so	'.*(libgo)\.so.*'

%if %{with pass2}
%define		no_install_post_strip   1
%define		no_install_post_chrpath 1
%define		_enable_debug_packages  0
%endif

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

This package contains the C compiler and some files shared by various
parts of the GNU Compiler Collection. In order to use another GCC
compiler you will need to install the appropriate subpackage.

%package -n cpp
Summary:	C Preprocessor
Group:		Development/Languages

%description -n cpp
Cpp is the GNU C-Compatible Compiler Preprocessor.
Cpp is a macro processor which is used automatically
by the C compiler to transform your program before actual
compilation. It is called a macro processor because it allows
you to define macros, abbreviations for longer
constructs.

%package -n libgcc
Summary:	Shared gcc library
License:	GPL v2+ with unlimited link permission
Group:		Libraries

%description -n libgcc
Shared gcc library.

%package -n libgomp
Summary:	GNU OpenMP library
License:	LGPL v2.1+ with unlimited link permission
Group:		Libraries

%description -n libgomp
GNU OpenMP library.

%package -n libgomp-devel
Summary:	Development files for GNU OpenMP library
License:	LGPL v2.1+ with unlimited link permission
Group:		Development/Libraries
Requires:	libgomp = %{epoch}:%{version}-%{release}

%description -n libgomp-devel
Development files for GNU OpenMP library.

%package -n libgomp-static
Summary:	Static GNU OpenMP library
License:	LGPL v2.1+ with unlimited link permission
Group:		Development/Libraries
Requires:	libgomp-devel = %{epoch}:%{version}-%{release}

%description -n libgomp-static
Static GNU OpenMP library.

Group:		Libraries

%package c++
Summary:	C++ support for gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description c++
This package adds C++ support to the GNU Compiler Collection. It
includes support for most of the current C++ specification, including
templates and exception handling. It does not include a standard C++
library, which is available separately.

%package -n libstdc++
Summary:	GNU C++ library
License:	GPL v2+ with free software exception
Group:		Libraries
# >= instead of = to allow keeping older libstdc++ (with different soname)
Requires:	libgcc >= %{epoch}:%{version}-%{release}

%description -n libstdc++
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%package -n libstdc++-devel
Summary:	Header files and documentation for C++ development
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	glibc-devel
Requires:	libstdc++ = %{epoch}:%{version}-%{release}

%description -n libstdc++-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files needed for C++ development and
library documentation.

%package -n libstdc++-static
Summary:	Static C++ standard library
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	libstdc++-devel = %{epoch}:%{version}-%{release}

%description -n libstdc++-static
Static C++ standard library.

%package fortran
Summary:	Fortran 95 support for gcc
Group:		Development/Languages/Fortran
Requires:	libgfortran = %{epoch}:%{version}-%{release}
Requires:	libquadmath-devel = %{epoch}:%{version}-%{release}
Provides:	gcc-g77 = %{epoch}:%{version}-%{release}

%description fortran
This package adds support for compiling Fortran 95 programs with the
GNU compiler.

%package -n libgfortran
Summary:	Fortran 95 Libraries
License:	GPL v2+ with unlimited link permission
Group:		Libraries

%description -n libgfortran
Fortran 95 Libraries.

%package -n libquadmath
Summary:	GCC __float128 shared support library
License:	GPL v2+ with linking exception
Group:		Libraries

%description -n libquadmath
This package contains GCC shared support library which is needed for
__float128 math support and for Fortran REAL*16 support.

%package -n libquadmath-devel
Summary:	Header files for GCC __float128 support library
License:	GPL v2+ with linking exception
Group:		Development/Libraries
Requires:	libquadmath = %{epoch}:%{version}-%{release}

%description -n libquadmath-devel
This package contains header files for GCC support library which is
needed for __float128 math support and for Fortran REAL*16 support.

%package go
Summary:	Go language support for gcc
License:	GPL v3+ (gcc), BSD (Go-specific part)
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgo-devel = %{epoch}:%{version}-%{release}

%description go
This package adds Go language support to the GNU Compiler Collection.

%package -n libgo
Summary:	Go language library
License:	BSD
Group:		Libraries
Requires:	libgcc >= %{epoch}:%{version}-%{release}

%description -n libgo
Go language library.

%package -n libgo-devel
Summary:	Development files for Go language library
License:	BSD
Group:		Development/Libraries
Requires:	glibc-devel
Requires:	libgo = %{epoch}:%{version}-%{release}

%description -n libgo-devel
Development files for Go language library.

%package -n libasan
Summary:	The Address Sanitizer library
Group:		Libraries

%description -n libasan
This package contains the Address Sanitizer library
which is used for -fsanitize=address instrumented programs.

%package -n libasan-devel
Summary:	Development files for the Address Sanitizer library
Group:		Development/Libraries
Requires:	libasan = %{epoch}:%{version}-%{release}

%description -n libasan-devel
This package contains development files for the Address Sanitizer
library.

%package -n liblsan
Summary:	The Address Sanitizer library
Group:		Libraries

%description -n liblsan
This package contains the Address Sanitizer library
which is used for -fsanitize=address instrumented programs.

%package -n liblsan-devel
Summary:	Development files for the Address Sanitizer library
Group:		Development/Libraries
Requires:	liblsan = %{epoch}:%{version}-%{release}

%description -n liblsan-devel
This package contains development files for the Address Sanitizer
library.

%package -n libtsan
Summary:	The Thread Sanitizer library
Group:		Libraries

%description -n libtsan
This package contains the Thread Sanitizer library
which is used for -fsanitize=thread instrumented programs.

%package -n libtsan-devel
Summary:	Development files for the Thread Sanitizer library
Group:		Development/Libraries
Requires:	libtsan = %{epoch}:%{version}-%{release}

%description -n libtsan-devel
This package contains development files for Thread Sanitizer library.

%package -n libubsan
Summary:	The Address Sanitizer library
Group:		Libraries

%description -n libubsan
This package contains the Address Sanitizer library
which is used for -fsanitize=address instrumented programs.

%package -n libubsan-devel
Summary:	Development files for the Address Sanitizer library
Group:		Development/Libraries
Requires:	libubsan = %{epoch}:%{version}-%{release}

%description -n libubsan-devel
This package contains development files for the Address Sanitizer
library.

%package -n libatomic
Summary:	The GNU Atomic library
Group:		Libraries

%description -n libatomic
This package contains the GNU Atomic library which is a GCC support
library for atomic operations not supported by hardware.

%package -n libatomic-devel
Summary:	Development files for the GNU Atomic library
Group:		Development/Libraries
Requires:	libatomic = %{epoch}:%{version}-%{release}

%description -n libatomic-devel
This package contains development files for the GNU Atomic libraries.

%package -n libcilkrts
Summary:	The GNU cilkrts library
Group:		Libraries

%description -n libcilkrts
This package contains the GNU cilkrts library which is a GCC support
library for cilkrts operations not supported by hardware.

%package -n libcilkrts-devel
Summary:	Development files for the GNU cilkrts library
Group:		Development/Libraries
Requires:	libcilkrts = %{epoch}:%{version}-%{release}

%description -n libcilkrts-devel
This package contains development files for the GNU cilkrts libraries.

%package -n libvtv
Summary:	The GNU vtv library
Group:		Libraries

%description -n libvtv
This package contains the GNU vtv library which is a GCC support
library for vtv operations not supported by hardware.

%package -n libvtv-devel
Summary:	Development files for the GNU vtv library
Group:		Development/Libraries
Requires:	libvtv = %{epoch}:%{version}-%{release}

%description -n libvtv-devel
This package contains development files for the GNU vtv libraries.

%prep
%setup -qn %{name}-%{mver}-%{snap}
%patch0 -p1
%patch1 -p0

%if %{with pass2}
# undefined reference to `__stack_chk_guard'
%{__sed} -i '/k prot/agcc_cv_libc_provides_ssp=yes' gcc/configure
tar -xf %{SOURCE1}
mv mpfr-3.1.2 mpfr
tar -xf %{SOURCE2}
mv gmp-6.0.0 gmp
tar -xf %{SOURCE3}
mv mpc-1.0.2 mpc
%endif

# override snapshot version.
echo %{version} > gcc/BASE-VER
echo "release" > gcc/DEV-PHASE

# Do not run fixincludes
%{__sed} -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in

%build
cp -f %{_datadir}/automake/config.* .
install -d build
cd build

CC="%{__cc}"			\
CFLAGS="%{rpmcflags}"		\
CXXFLAGS="%{rpmcxxflags}"	\
TEXCONFIG=false			\
../configure %{_target_platform}	\
	--infodir=%{_infodir}						\
	--libdir=%{_libdir}						\
	--libexecdir=%{_libdir}						\
	--mandir=%{_mandir}						\
	--prefix=%{_prefix}						\
	--with-gxx-include-dir=%{_includedir}/c++/%{version}		\
	--with-local-prefix=%{_prefix}/local				\
	--with-slibdir=%{_libdir}					\
	--x-libraries=%{_libdir}					\
	--disable-bootstrap						\
	--disable-build-poststage1-with-cxx				\
	--disable-build-with-cxx					\
	--disable-cld							\
	--disable-cloog-version-check					\
	--disable-install-libiberty					\
	--disable-libssp						\
	--disable-libstdcxx-pch						\
	--disable-libunwind-exceptions					\
	--disable-multilib						\
	--disable-werror						\
%if %{with pass2}
	--disable-libgomp						\
	--disable-lto							\
	--enable-languages="c,c++"					\
	--with-mpfr-include=$(pwd)/../mpfr/src				\
	--with-mpfr-lib=$(pwd)/mpfr/src/.libs				\
%else
	--enable-__cxa_atexit						\
	--enable-checking=release					\
	--enable-clocale=gnu						\
	--enable-cloog-backend=isl					\
	--enable-gnu-unique-object					\
	--enable-languages="c,c++,fortran,go"				\
	--enable-ld=default						\
	--enable-libgomp						\
	--enable-libstdcxx-allocator=new				\
	--enable-libstdcxx-time						\
	--enable-linker-build-id					\
	--enable-lto							\
	--enable-nls							\
	--enable-shared							\
	--enable-threads=posix 						\
	--with-demangler-in-ld						\
	--with-gnu-as							\
	--with-gnu-ld							\
	--with-linker-hash-style=gnu					\
	--with-pkgversion="Freddix"					\
	--with-system-zlib						\
	--without-x
%endif

cd ..

%{__make} -C build 				\
	BOOT_CFLAGS="%{rpmcflags}"		\
	LDFLAGS_FOR_TARGET="%{rpmldflags}"	\
	STAGE1_CFLAGS="%{rpmcflags} -O0 -g0"	\
	infodir=%{_infodir}			\
	mandir=%{_mandir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/lib,%{_aclocaldir},%{_datadir},%{_infodir}}

%{__make} -j1 -C build install	\
	DESTDIR=$RPM_BUILD_ROOT		\
	infodir=%{_infodir}		\
	mandir=%{_mandir}

cp -p build/gcc/specs $RPM_BUILD_ROOT%{gcclibdir}

ln -sf %{_bindir}/cpp $RPM_BUILD_ROOT/usr/lib/cpp
ln -sf gcc $RPM_BUILD_ROOT%{_bindir}/cc
echo ".so gcc.1" > $RPM_BUILD_ROOT%{_mandir}/man1/cc.1

%if %{without pass2}
ln -sf gfortran $RPM_BUILD_ROOT%{_bindir}/g95
echo ".so gfortran.1" > $RPM_BUILD_ROOT%{_mandir}/man1/g95.1
%endif

# avoid -L poisoning in *.la. normalize libdir
# to avoid propagation of unnecessary RPATHs by libtool
for f in \
%ifnarch %{ix86}
	libtsan.la	\
	liblsan.la	\
%endif
%if %{without pass2}
	libgfortran.la	\
	libgo.la	\
	libgomp.la	\
%endif
	libasan.la	\
	libatomic.la	\
	libcilkrts.la	\
	libitm.la	\
	libquadmath.la	\
	libstdc++.la	\
	libsupc++.la	\
	libubsan.la	\
	libvtv.la

do
	%{__perl} %{SOURCE10} $RPM_BUILD_ROOT%{_libdir}/$f %{_libdir} > $RPM_BUILD_ROOT%{_libdir}/$f.fixed
	mv $RPM_BUILD_ROOT%{_libdir}/$f{.fixed,}
done

cp -p $RPM_BUILD_ROOT%{gcclibdir}/install-tools/include/*.h $RPM_BUILD_ROOT%{gcclibdir}/include
cp -p $RPM_BUILD_ROOT%{gcclibdir}/include-fixed/syslimits.h $RPM_BUILD_ROOT%{gcclibdir}/include
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/install-tools
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/include-fixed

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libstdc++.so.*-gdb.py

%if %{without pass2}
%find_lang gcc
%find_lang cpplib
%find_lang libstdc\+\+
%endif
install libstdc++-v3/include/precompiled/* $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n cpp -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n cpp -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post fortran -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun fortran -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	go -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	go -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-p /usr/sbin/ldconfig -n libgcc
%postun	-p /usr/sbin/ldconfig -n libgcc
%post	-p /usr/sbin/ldconfig -n libgomp
%postun	-p /usr/sbin/ldconfig -n libgomp
%post	-p /usr/sbin/ldconfig -n libstdc++
%postun	-p /usr/sbin/ldconfig -n libstdc++
%post	-p /usr/sbin/ldconfig -n libgfortran
%postun	-p /usr/sbin/ldconfig -n libgfortran
%post	-p /usr/sbin/ldconfig -n libquadmath
%postun	-p /usr/sbin/ldconfig -n libquadmath
%post	-p /usr/sbin/ldconfig -n libgo
%postun	-p /usr/sbin/ldconfig -n libgo
%post	-p /usr/sbin/ldconfig -n libasan
%postun	-p /usr/sbin/ldconfig -n libasan
%post	-p /usr/sbin/ldconfig -n liblsan
%postun	-p /usr/sbin/ldconfig -n liblsan
%post	-p /usr/sbin/ldconfig -n libtsan
%postun	-p /usr/sbin/ldconfig -n libtsan
%post	-p /usr/sbin/ldconfig -n libubsan
%postun	-p /usr/sbin/ldconfig -n libubsan
%post	-p /usr/sbin/ldconfig -n libatomic
%postun	-p /usr/sbin/ldconfig -n libatomic
%post	-p /usr/sbin/ldconfig -n libcilkrts
%postun	-p /usr/sbin/ldconfig -n libcilkrts
%post	-p /usr/sbin/ldconfig -n libvtv
%postun	-p /usr/sbin/ldconfig -n libvtv

%files %{!?with_pass2:-f gcc.lang}
%defattr(644,root,root,755)
%doc ChangeLog MAINTAINERS
%doc gcc/{ChangeLog,ONEWS,README.Portability}
%attr(755,root,root) %{_bindir}/*-gcc*
%attr(755,root,root) %{_bindir}/cc
%attr(755,root,root) %{_bindir}/gcc
%attr(755,root,root) %{_bindir}/gcc-ar
%attr(755,root,root) %{_bindir}/gcc-nm
%attr(755,root,root) %{_bindir}/gcc-ranlib
%attr(755,root,root) %{_bindir}/gcov
%attr(755,root,root) %{_slibdir}/libgcc_s.so
%attr(755,root,root) %{_libdir}/libitm.so
%attr(755,root,root) %{gcclibdir}/collect2
%if %{without pass2}
%attr(755,root,root) %{gcclibdir}/liblto_plugin.so*
%attr(755,root,root) %{gcclibdir}/lto-wrapper
%attr(755,root,root) %{gcclibdir}/lto1
%endif
%dir %{gcclibdir}/include

%dir %{gcclibdir}/include/sanitizer
%{gcclibdir}/include/sanitizer/common_interface_defs.h
%{_libdir}/libsanitizer.spec

%{gcclibdir}/crt*.o
%{gcclibdir}/include/*.h
%{gcclibdir}/libgcc.a
%{gcclibdir}/libgcc_eh.a
%{gcclibdir}/libgcov.a
%if %{without pass2}
%{gcclibdir}/plugin
%endif
%{gcclibdir}/specs

%{_libdir}/libitm.la
%{_libdir}/libitm.a
%{_libdir}/libitm.spec

%{!?with_pass2:%{_infodir}/gcc*}
%{_mandir}/man1/cc.1*
%{_mandir}/man1/gcc.1*
%{_mandir}/man1/gcov.1*

%files -n cpp %{!?with_pass2:-f cpplib.lang}
%defattr(644,root,root,755)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{_target_platform}
%dir %{gcclibdir}
%attr(755,root,root) %{_bindir}/cpp
%attr(755,root,root) %{gcclibdir}/cc1
%attr(755,root,root) /usr/lib/cpp
%{_mandir}/man1/cpp.1*
%{!?with_pass2:%{_infodir}/cpp*}

%files -n libgcc
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir}/libgcc_s.so.1
%attr(755,root,root) %ghost %{_libdir}/libitm.so.1
%attr(755,root,root) %{_libdir}/libitm.so.*.*.*

%if %{without pass2}
%files -n libgomp
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgomp.so.?
%attr(755,root,root) %{_libdir}/libgomp.so.*.*.*

%files -n libgomp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgomp.so
%{_libdir}/libgomp.la
%{_libdir}/libgomp.spec
%{gcclibdir}/finclude
%{gcclibdir}/include/omp.h

%files -n libgomp-static
%defattr(644,root,root,755)
%{_libdir}/libgomp.a
%endif

%files c++
%defattr(644,root,root,755)
%doc gcc/cp/{ChangeLog,NEWS}
%attr(755,root,root) %{_bindir}/g++
%attr(755,root,root) %{_bindir}/*-g++
%attr(755,root,root) %{_bindir}/c++
%attr(755,root,root) %{_bindir}/*-c++
%attr(755,root,root) %{gcclibdir}/cc1plus
%{_libdir}/libsupc++.a
%{_libdir}/libsupc++.la
%{_mandir}/man1/g++.1*

%files -n libstdc++ %{!?with_pass2:-f libstdc++.lang}
%defattr(644,root,root,755)
%doc libstdc++-v3/{ChangeLog,README}
%attr(755,root,root) %ghost %{_libdir}/libstdc++.so.?
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*

%files -n libstdc++-devel
%defattr(644,root,root,755)
%doc libstdc++-v3/doc/html
%dir %{_includedir}/c++
%{_includedir}/c++/%{version}
%{_includedir}/extc++.h
%{_includedir}/stdc++.h
%{_includedir}/stdtr1c++.h
%{_libdir}/libstdc++.la
%attr(755,root,root) %{_libdir}/libstdc++.so

%files -n libstdc++-static
%defattr(644,root,root,755)
%{_libdir}/libstdc++.a

%if %{without pass2}
%files fortran
%defattr(644,root,root,755)
%doc gcc/fortran/ChangeLog
%attr(755,root,root) %{_bindir}/*-gfortran
%attr(755,root,root) %{_bindir}/g95
%attr(755,root,root) %{_bindir}/gfortran
%attr(755,root,root) %{_libdir}/libgfortran.so
%attr(755,root,root) %{gcclibdir}/f951
%{_libdir}/libgfortran.la
%{_libdir}/libgfortran.spec
%{gcclibdir}/libcaf_single.a
%{gcclibdir}/libcaf_single.la
%{gcclibdir}/libgfortranbegin.a
%{gcclibdir}/libgfortranbegin.la
%{_mandir}/man1/g95.1*
%{_mandir}/man1/gfortran.1*

%files -n libgfortran
%defattr(644,root,root,755)
%doc libgfortran/ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libgfortran.so.?
%attr(755,root,root) %{_libdir}/libgfortran.so.*.*.*
%endif

%files -n libquadmath
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquadmath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libquadmath.so.0

%files -n libquadmath-devel
%defattr(644,root,root,755)
%{gcclibdir}/include/quadmath.h
%{gcclibdir}/include/quadmath_weak.h
%attr(755,root,root) %{_libdir}/libquadmath.so
%{_libdir}/libquadmath.la

%if %{without pass2}
%files go
%defattr(644,root,root,755)
%doc gcc/go/gofrontend/{LICENSE,PATENTS,README}
%attr(755,root,root) %{_bindir}/gccgo
%attr(755,root,root) %{gcclibdir}/go1
%dir %{_libdir}/go
%{_libdir}/go/%{version}
%{_mandir}/man1/gccgo.1*
%{_infodir}/gccgo.info*

%files -n libgo
%defattr(644,root,root,755)
%doc libgo/{LICENSE,PATENTS,README}
%attr(755,root,root) %ghost %{_libdir}/libgo.so.5
%attr(755,root,root) %{_libdir}/libgo.so.*.*.*

%files -n libgo-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgo.so
%{_libdir}/libgo.la
%{_libdir}/libgobegin.a
%endif

%files -n libasan
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libasan.so.1
%attr(755,root,root) %{_libdir}/libasan.so.*.*.*

%files -n libasan-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libasan.so
%{_libdir}/libasan_preinit.o
%{_libdir}/libasan.la
%{gcclibdir}/include/sanitizer/asan_interface.h

%ifnarch %{ix86}
%files -n liblsan
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/liblsan.so.0
%attr(755,root,root) %{_libdir}/liblsan.so.*.*.*

%files -n liblsan-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblsan.so
%{_libdir}/liblsan.la
%{gcclibdir}/include/sanitizer/lsan_interface.h

%files -n libtsan
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libtsan.so.0
%attr(755,root,root) %{_libdir}/libtsan.so.*.*.*

%files -n libtsan-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtsan.so
%{_libdir}/libtsan.la
%endif

%files -n libubsan
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libubsan.so.0
%attr(755,root,root) %{_libdir}/libubsan.so.*.*.*

%files -n libubsan-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libubsan.so
%{_libdir}/libubsan.la

%files -n libatomic
%defattr(644,root,root,755)
%doc libatomic/ChangeLog*
%attr(755,root,root) %{_libdir}/libatomic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatomic.so.1

%files -n libatomic-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatomic.so
%{_libdir}/libatomic.la

%files -n libcilkrts
%defattr(644,root,root,755)
%doc libcilkrts/ChangeLog*
%attr(755,root,root) %ghost %{_libdir}/libcilkrts.so.5
%attr(755,root,root) %{_libdir}/libcilkrts.so.*.*.*

%files -n libcilkrts-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcilkrts.so
%{_libdir}/libcilkrts.la
%{_libdir}/libcilkrts.spec
%{gcclibdir}/include/cilk

%files -n libvtv
%defattr(644,root,root,755)
%doc libvtv/ChangeLog*
%attr(755,root,root) %ghost %{_libdir}/libvtv.so.0
%attr(755,root,root) %{_libdir}/libvtv.so.*.*.*

%files -n libvtv-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvtv.so
%{_libdir}/libvtv.la

