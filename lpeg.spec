#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v3
# autospec commit: c1050fe
#
Name     : lpeg
Version  : 1.0.2
Release  : 12
URL      : http://www.inf.puc-rio.br/~roberto/lpeg/lpeg-1.0.2.tar.gz
Source0  : http://www.inf.puc-rio.br/~roberto/lpeg/lpeg-1.0.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: lpeg-data = %{version}-%{release}
Requires: lpeg-lib = %{version}-%{release}
BuildRequires : lua-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-makefile-fixes.patch

%description
No detailed description available

%package data
Summary: data components for the lpeg package.
Group: Data

%description data
data components for the lpeg package.


%package lib
Summary: lib components for the lpeg package.
Group: Libraries
Requires: lpeg-data = %{version}-%{release}

%description lib
lib components for the lpeg package.


%prep
%setup -q -n lpeg-1.0.2
cd %{_builddir}/lpeg-1.0.2
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703191330
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
make  %{?_smp_mflags}


%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1703191330
rm -rf %{buildroot}
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib64/lua/5.4
cp -a %{buildroot}/usr/lib64/lua/*so %{buildroot}/usr/lib64/lua/5.4
mkdir -p %{buildroot}/usr/lib
cp -a %{buildroot}/usr/lib64/lua %{buildroot}/usr/lib/lua/
#cp -a %{buildroot}/usr/share/lua/5.1 %{buildroot}/usr/share/lua/5.4
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/lua/re.lua

%files lib
%defattr(-,root,root,-)
/usr/lib/lua/5.4/lpeg.so
/usr/lib/lua/lpeg.so
/usr/lib64/lua/5.4/lpeg.so
/usr/lib64/lua/lpeg.so
