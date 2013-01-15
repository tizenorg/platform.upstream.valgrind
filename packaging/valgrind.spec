Name:           valgrind
Url:            http://valgrind.org/
Summary:        Memory Management Debugger
License:        GPL-2.0+
Group:          Development/Tools/Debuggers
Version:        3.8.1
Release:        0
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel-32bit
BuildRequires:  libxslt
BuildRequires:  pkgconfig

%description
Valgrind checks all memory operations in an application, like read,
write, malloc, new, free, and delete. Valgrind can find uses of
uninitialized memory, access to already freed memory, overflows,
illegal stack operations, memory leaks, and any illegal
new/malloc/free/delete commands. Another program in the package is
"cachegrind," a profiler based on the valgrind engine.

To use valgrind you should compile your application with "-g -O0"
compiler options. Afterwards you can use it with:

valgrind --tool=memcheck --sloppy-malloc=yes --leak-check=yes
--db-attach=yes my_application, for example.

More valgrind options can be listed via "valgrind --help". A
debugged application runs slower and needs much more memory, but
is usually still usable. Valgrind is still in development, but it
has been successfully used to optimize several KDE applications.


%package devel
Summary:        Memory Management Debugger
Group:          Development/Tools/Debuggers
Requires:       %name = %version

%description devel
Valgrind checks all memory operations in an application, like read,
write, malloc, new, free, and delete. Valgrind can find uses of
uninitialized memory, access to already freed memory, overflows,
illegal stack operations, memory leaks, and any illegal
new/malloc/free/delete commands. Another program in the package is
"cachegrind," a profiler based on the valgrind engine.

To use valgrind you should compile your application with "-g -O0"
compiler options. Afterwards you can use it with:

valgrind --tool=memcheck --sloppy-malloc=yes --leak-check=yes
--db-attach=yes my_application, for example.

More valgrind options can be listed via "valgrind --help". A
debugged application runs slower and needs much more memory, but
is usually still usable. Valgrind is still in development, but it
has been successfully used to optimize several KDE applications.

%prep
%setup -q

%build
export CFLAGS="-O2"
export CXXFLAGS="-O2"
%autogen

%ifarch x86_64
%configure --enable-only64bit
%else
%configure
%endif

make %{?_smp_mflags}


%install
%make_install

# extra documentation available online
rm -rf %{buildroot}%{_datadir}/doc/valgrind

%docs_package

%files
%license COPYING
%{_bindir}/*
%dir %{_libdir}/valgrind
%ifarch x86_64
%{_libdir}/valgrind/*-amd64-linux
%endif
%ifarch %ix86
%{_libdir}/valgrind/*-x86-linux
%endif
%ifarch %arm
%{_libdir}/valgrind/*-arm-linux
%endif
%{_libdir}/valgrind/*-linux.so
%{_libdir}/valgrind/*.supp
%{_libdir}/valgrind/32bit-core-valgrind-s*.xml
%{_libdir}/valgrind/32bit-core.xml
%{_libdir}/valgrind/32bit-linux-valgrind-s*.xml
%{_libdir}/valgrind/32bit-linux.xml
%{_libdir}/valgrind/32bit-sse-valgrind-s*.xml
%{_libdir}/valgrind/32bit-sse.xml
%{_libdir}/valgrind/64bit-avx-valgrind-s1.xml
%{_libdir}/valgrind/64bit-avx-valgrind-s2.xml
%{_libdir}/valgrind/64bit-avx.xml
%{_libdir}/valgrind/64bit-core-valgrind-s*.xml
%{_libdir}/valgrind/64bit-core.xml
%{_libdir}/valgrind/64bit-linux-valgrind-s*.xml
%{_libdir}/valgrind/64bit-linux.xml
%{_libdir}/valgrind/64bit-sse-valgrind-s*.xml
%{_libdir}/valgrind/64bit-sse.xml
%{_libdir}/valgrind/amd64-avx-coresse-valgrind.xml
%{_libdir}/valgrind/amd64-avx-coresse.xml
%{_libdir}/valgrind/amd64-avx-linux-valgrind.xml
%{_libdir}/valgrind/amd64-avx-linux.xml
%{_libdir}/valgrind/amd64-coresse-valgrind.xml
%{_libdir}/valgrind/amd64-linux-valgrind.xml
%{_libdir}/valgrind/arm-core-valgrind-s*.xml
%{_libdir}/valgrind/arm-core.xml
%{_libdir}/valgrind/arm-vfpv3-valgrind-s*.xml
%{_libdir}/valgrind/arm-vfpv3.xml
%{_libdir}/valgrind/arm-with-vfpv3-valgrind.xml
%{_libdir}/valgrind/arm-with-vfpv3.xml
%{_libdir}/valgrind/i386-coresse-valgrind.xml
%{_libdir}/valgrind/i386-linux-valgrind.xml
%{_libdir}/valgrind/mips-cp0-valgrind-s1.xml
%{_libdir}/valgrind/mips-cp0-valgrind-s2.xml
%{_libdir}/valgrind/mips-cp0.xml
%{_libdir}/valgrind/mips-cpu-valgrind-s1.xml
%{_libdir}/valgrind/mips-cpu-valgrind-s2.xml
%{_libdir}/valgrind/mips-cpu.xml
%{_libdir}/valgrind/mips-fpu-valgrind-s1.xml
%{_libdir}/valgrind/mips-fpu-valgrind-s2.xml
%{_libdir}/valgrind/mips-fpu.xml
%{_libdir}/valgrind/mips-linux-valgrind.xml
%{_libdir}/valgrind/mips-linux.xml
%{_libdir}/valgrind/power-altivec-valgrind-s*.xml
%{_libdir}/valgrind/power-altivec.xml
%{_libdir}/valgrind/power-core-valgrind-s1.xml
%{_libdir}/valgrind/power-core-valgrind-s2.xml
%{_libdir}/valgrind/power-core.xml
%{_libdir}/valgrind/power-fpu-valgrind-s*.xml
%{_libdir}/valgrind/power-fpu.xml
%{_libdir}/valgrind/power-linux-valgrind-s*.xml
%{_libdir}/valgrind/power-linux.xml
%{_libdir}/valgrind/power64-core-valgrind-s*.xml
%{_libdir}/valgrind/power64-core.xml
%{_libdir}/valgrind/power64-linux-valgrind-s*.xml
%{_libdir}/valgrind/power64-linux.xml
%{_libdir}/valgrind/powerpc-altivec32l-valgrind.xml
%{_libdir}/valgrind/powerpc-altivec32l.xml
%{_libdir}/valgrind/powerpc-altivec64l-valgrind.xml
%{_libdir}/valgrind/powerpc-altivec64l.xml
%{_libdir}/valgrind/s390-acr-valgrind-s1.xml
%{_libdir}/valgrind/s390-acr-valgrind-s2.xml
%{_libdir}/valgrind/s390-acr.xml
%{_libdir}/valgrind/s390-fpr-valgrind-s1.xml
%{_libdir}/valgrind/s390-fpr-valgrind-s2.xml
%{_libdir}/valgrind/s390-fpr.xml
%{_libdir}/valgrind/s390x-core64-valgrind-s1.xml
%{_libdir}/valgrind/s390x-core64-valgrind-s2.xml
%{_libdir}/valgrind/s390x-core64.xml
%{_libdir}/valgrind/s390x-generic-valgrind.xml
%{_libdir}/valgrind/s390x-generic.xml
%{_libdir}/valgrind/s390x-linux64-valgrind-s1.xml
%{_libdir}/valgrind/s390x-linux64-valgrind-s2.xml
%{_libdir}/valgrind/s390x-linux64.xml

%files devel
%{_includedir}/valgrind
%{_libdir}/pkgconfig/valgrind.pc
