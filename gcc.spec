%bcond_with	bootstrap

%define		snap	20140206

Summary:	GNU Compiler Collection: the C compiler and shared files
Name:		gcc
Version:	4.8.2
Release:	3.%{snap}.1
Epoch:		6
License:	GPL v3+
Group:		Development/Languages
#Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/%{name}-%{version}.tar.bz2
Source0:	ftp://gcc.gnu.org/pub/gcc/snapshots/4.8-%{snap}/%{name}-4.8-%{snap}.tar.bz2
# Source0-md5:	9d35549404a2326540fb88301ebd1977
%if 0
# for cross build
Source1:	http://www.mpfr.org/mpfr-current/mpfr-3.1.1.tar.xz
# Source1-md5:	91d51c41fcf2799e4ee7a7126fc95c17
Source2:	ftp://ftp.gnu.org/gnu/gmp/gmp-5.0.5.tar.xz
# Source2-md5:	8aef50959acec2a1ad41d144ffe0f3b5
Source3:	http://multiprecision.org/mpc/download/mpc-1.0.1.tar.gz
# Source3-md5:	b32a2e1a3daa392372fbd586d1ed3679
%endif
Source10:	gcc-optimize-la.pl
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=21704
Patch0:		%{name}-include.patch
Patch1:		%{name}-filename-output.patch
URL:		http://gcc.gnu.org/
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
Requires:	binutils
Requires:	cpp = %{epoch}:%{version}-%{release}
Requires:	libgcc = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_slibdir	%{_libdir}
%define		gcclibdir	%{_libdir}/gcc/%{_target_platform}/%{version}

%define		filterout	-fwrapv -fno-strict-aliasing -fsigned-char
# FIXME: unresolved symbols
%define		skip_post_check_so	'.*(libgo|libmudflap|libmudflapth)\.so.*'

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

%package -n libmudflap
Summary:	GCC mudflap shared support library
License:	GPL v2+ with unlimited link permission
Group:		Libraries

%description -n libmudflap
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations.

%package -n libmudflap-devel
Summary:	Development files for GCC mudflap library
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap = %{epoch}:%{version}-%{release}

%description -n libmudflap-devel
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains development
files.

%package -n libmudflap-multilib-devel
Summary:	Development files for GCC mudflap library
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap-devel = %{epoch}:%{version}-%{release}

%description -n libmudflap-multilib-devel
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains development
files.

%package -n libmudflap-static
Summary:	Static GCC mudflap library
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap-devel = %{epoch}:%{version}-%{release}

%description -n libmudflap-static
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains static
libraries.

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

%prep
%setup -qn %{name}-4.8-%{snap}
%patch0 -p1
%patch1 -p0

%if 0
# cross build
# undefined reference to `__stack_chk_guard'
%{__sed} -i '/k prot/agcc_cv_libc_provides_ssp=yes' gcc/configure

tar -xf %{SOURCE1}
mv mpfr-3.1.1 mpfr
tar -xf %{SOURCE2}
mv gmp-5.0.5 gmp
tar -xf %{SOURCE3}
mv mpc-1.0.1 mpc
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
	--%{?with_bootstrap:en}%{!?with_bootstrap:dis}able-bootstrap	\
	--infodir=%{_infodir}						\
	--libdir=%{_libdir}						\
	--libexecdir=%{_libdir}						\
	--mandir=%{_mandir}						\
	--prefix=%{_prefix}						\
	--with-gxx-include-dir=%{_includedir}/c++/%{version}		\
	--with-local-prefix=%{_prefix}/local				\
	--with-slibdir=%{_libdir}					\
	--x-libraries=%{_libdir}					\
	--disable-build-poststage1-with-cxx                             \
	--disable-build-with-cxx                                        \
	--disable-cld                                                   \
	--disable-cloog-version-check					\
	--disable-install-libiberty					\
	--disable-libssp                                                \
	--disable-libstdcxx-pch                                         \
	--disable-libunwind-exceptions                                  \
	--disable-multilib						\
	--disable-werror						\
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
%if 0
	--with-mpfr-include=$(pwd)/../mpfr/src	\
	--with-mpfr-lib=$(pwd)/mpfr/src/.libs
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

ln -sf gfortran $RPM_BUILD_ROOT%{_bindir}/g95
echo ".so gfortran.1" > $RPM_BUILD_ROOT%{_mandir}/man1/g95.1

# avoid -L poisoning in *.la. normalize libdir
# to avoid propagation of unnecessary RPATHs by libtool
for f in \
%ifnarch %{ix86}
	libtsan.la	\
%endif
	libatomic.la	\
	libgfortran.la	\
	libgo.la	\
	libgomp.la	\
	libitm.la	\
	libmudflap.la	\
	libmudflapth.la	\
	libquadmath.la	\
	libstdc++.la	\
	libsupc++.la
do
	%{__perl} %{SOURCE10} $RPM_BUILD_ROOT%{_libdir}/$f %{_libdir} > $RPM_BUILD_ROOT%{_libdir}/$f.fixed
	mv $RPM_BUILD_ROOT%{_libdir}/$f{.fixed,}
done

cp -p $RPM_BUILD_ROOT%{gcclibdir}/install-tools/include/*.h $RPM_BUILD_ROOT%{gcclibdir}/include
cp -p $RPM_BUILD_ROOT%{gcclibdir}/include-fixed/syslimits.h $RPM_BUILD_ROOT%{gcclibdir}/include
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/install-tools
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/include-fixed

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libstdc++.so.*-gdb.py

%find_lang gcc
%find_lang cpplib

%find_lang libstdc\+\+
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
%post	-p /usr/sbin/ldconfig -n libmudflap
%postun	-p /usr/sbin/ldconfig -n libmudflap
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
%post	-p /usr/sbin/ldconfig -n libtsan
%postun	-p /usr/sbin/ldconfig -n libtsan
%post	-p /usr/sbin/ldconfig -n libatomic
%postun	-p /usr/sbin/ldconfig -n libatomic

%files -f gcc.lang
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
%attr(755,root,root) %{gcclibdir}/liblto_plugin.so*
%attr(755,root,root) %{gcclibdir}/lto-wrapper
%attr(755,root,root) %{gcclibdir}/lto1
%dir %{gcclibdir}/include

%{gcclibdir}/crt*.o
%{gcclibdir}/include/*.h
%{gcclibdir}/libgcc.a
%{gcclibdir}/libgcc_eh.a
%{gcclibdir}/libgcov.a
%{gcclibdir}/plugin
%{gcclibdir}/specs

%{_libdir}/libitm.la
%{_libdir}/libitm.a
%{_libdir}/libitm.spec

%{_infodir}/gcc*
%{_mandir}/man1/cc.1*
%{_mandir}/man1/gcc.1*
%{_mandir}/man1/gcov.1*

%files -n cpp -f cpplib.lang
%defattr(644,root,root,755)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{_target_platform}
%dir %{gcclibdir}
%attr(755,root,root) %{_bindir}/cpp
%attr(755,root,root) %{gcclibdir}/cc1
%attr(755,root,root) /usr/lib/cpp
%{_mandir}/man1/cpp.1*
%{_infodir}/cpp*

%files -n libgcc
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir}/libgcc_s.so.1
%attr(755,root,root) %ghost %{_libdir}/libitm.so.1
%attr(755,root,root) %{_libdir}/libitm.so.*.*.*

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

%files -n libmudflap
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libmudflap.so.0
%attr(755,root,root) %ghost %{_libdir}/libmudflapth.so.0
%attr(755,root,root) %{_libdir}/libmudflap.so.*.*.*
%attr(755,root,root) %{_libdir}/libmudflapth.so.*.*.*

%files -n libmudflap-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmudflap.so
%attr(755,root,root) %{_libdir}/libmudflapth.so
%{_libdir}/libmudflap.la
%{_libdir}/libmudflapth.la
%{gcclibdir}/include/mf-runtime.h

%files -n libmudflap-static
%defattr(644,root,root,755)
%{_libdir}/libmudflap.a
%{_libdir}/libmudflapth.a

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

%files -n libstdc++ -f libstdc++.lang
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
%attr(755,root,root) %ghost %{_libdir}/libgo.so.4
%attr(755,root,root) %{_libdir}/libgo.so.*.*.*

%files -n libgo-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgo.so
%{_libdir}/libgo.la
%{_libdir}/libgobegin.a

%files -n libasan
%defattr(644,root,root,755)
%doc libsanitizer/ChangeLog* libsanitizer/LICENSE.TXT
%attr(755,root,root) %ghost %{_libdir}/libasan.so.0
%attr(755,root,root) %{_libdir}/libasan.so.*.*.*

%files -n libasan-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libasan.so
%{_libdir}/libasan_preinit.o
%{_libdir}/libasan.la

%ifnarch %{ix86}
%files -n libtsan
%defattr(644,root,root,755)
%doc libsanitizer/ChangeLog* libsanitizer/LICENSE.TXT
%attr(755,root,root) %ghost %{_libdir}/libtsan.so.0
%attr(755,root,root) %{_libdir}/libtsan.so.*.*.*

%files -n libtsan-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtsan.so
%{_libdir}/libtsan.la
%endif

%files -n libatomic
%defattr(644,root,root,755)
%doc libatomic/ChangeLog*
%attr(755,root,root) %{_libdir}/libatomic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatomic.so.1

%files -n libatomic-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatomic.so
%{_libdir}/libatomic.la

