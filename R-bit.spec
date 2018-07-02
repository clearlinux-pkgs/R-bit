#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bit
Version  : 1.1.14
Release  : 15
URL      : https://cran.r-project.org/src/contrib/bit_1.1-14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bit_1.1-14.tar.gz
Summary  : A Class for Vectors of 1-Bit Booleans
Group    : Development/Tools
License  : GPL-2.0
Requires: R-bit-lib
Requires: R-bit64
Requires: R-ff
BuildRequires : R-bit64
BuildRequires : R-ff
BuildRequires : clr-R-helpers

%description
coercion from and to logicals, integers and integer subscripts; 
  fast boolean operators and fast summary statistics. 
  With 'bit' vectors you can store true binary booleans {FALSE,TRUE} at the 
  expense of 1 bit only, on a 32 bit architecture this means factor 32 less 
  RAM and ~ factor 32 more speed on boolean operations. Due to overhead of

%package lib
Summary: lib components for the R-bit package.
Group: Libraries

%description lib
lib components for the R-bit package.


%prep
%setup -q -c -n bit

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527656141

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1527656141
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bit
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library bit|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bit/ANNOUNCEMENT-1.0.txt
/usr/lib64/R/library/bit/DESCRIPTION
/usr/lib64/R/library/bit/INDEX
/usr/lib64/R/library/bit/Meta/Rd.rds
/usr/lib64/R/library/bit/Meta/features.rds
/usr/lib64/R/library/bit/Meta/hsearch.rds
/usr/lib64/R/library/bit/Meta/links.rds
/usr/lib64/R/library/bit/Meta/nsInfo.rds
/usr/lib64/R/library/bit/Meta/package.rds
/usr/lib64/R/library/bit/NAMESPACE
/usr/lib64/R/library/bit/NEWS
/usr/lib64/R/library/bit/R/bit
/usr/lib64/R/library/bit/R/bit.rdb
/usr/lib64/R/library/bit/R/bit.rdx
/usr/lib64/R/library/bit/README_devel.txt
/usr/lib64/R/library/bit/exec/make_rd.pl
/usr/lib64/R/library/bit/exec/prebuild.sh
/usr/lib64/R/library/bit/help/AnIndex
/usr/lib64/R/library/bit/help/aliases.rds
/usr/lib64/R/library/bit/help/bit.rdb
/usr/lib64/R/library/bit/help/bit.rdx
/usr/lib64/R/library/bit/help/paths.rds
/usr/lib64/R/library/bit/html/00Index.html
/usr/lib64/R/library/bit/html/R.css
/usr/lib64/R/library/bit/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bit/libs/bit.so
/usr/lib64/R/library/bit/libs/bit.so.avx2
/usr/lib64/R/library/bit/libs/bit.so.avx512
