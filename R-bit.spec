#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bit
Version  : 4.0.5
Release  : 62
URL      : https://cran.r-project.org/src/contrib/bit_4.0.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bit_4.0.5.tar.gz
Summary  : Classes and Methods for Fast Memory-Efficient Boolean Selections
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-bit-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
fast boolean methods, fast unique and non-unique integer sorting,
    fast set operations on sorted and unsorted sets of integers, and
    foundations for ff (range index, compression, chunked processing).

%package lib
Summary: lib components for the R-bit package.
Group: Libraries

%description lib
lib components for the R-bit package.


%prep
%setup -q -n bit
cd %{_builddir}/bit

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1668623309

%install
export SOURCE_DATE_EPOCH=1668623309
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bit/DESCRIPTION
/usr/lib64/R/library/bit/INDEX
/usr/lib64/R/library/bit/Meta/Rd.rds
/usr/lib64/R/library/bit/Meta/features.rds
/usr/lib64/R/library/bit/Meta/hsearch.rds
/usr/lib64/R/library/bit/Meta/links.rds
/usr/lib64/R/library/bit/Meta/nsInfo.rds
/usr/lib64/R/library/bit/Meta/package.rds
/usr/lib64/R/library/bit/Meta/vignette.rds
/usr/lib64/R/library/bit/NAMESPACE
/usr/lib64/R/library/bit/NEWS
/usr/lib64/R/library/bit/R/bit
/usr/lib64/R/library/bit/R/bit.rdb
/usr/lib64/R/library/bit/R/bit.rdx
/usr/lib64/R/library/bit/doc/bit-demo.R
/usr/lib64/R/library/bit/doc/bit-demo.Rmd
/usr/lib64/R/library/bit/doc/bit-demo.pdf
/usr/lib64/R/library/bit/doc/bit-performance.R
/usr/lib64/R/library/bit/doc/bit-performance.Rmd
/usr/lib64/R/library/bit/doc/bit-performance.pdf
/usr/lib64/R/library/bit/doc/bit-usage.R
/usr/lib64/R/library/bit/doc/bit-usage.Rmd
/usr/lib64/R/library/bit/doc/bit-usage.pdf
/usr/lib64/R/library/bit/doc/index.html
/usr/lib64/R/library/bit/help/AnIndex
/usr/lib64/R/library/bit/help/aliases.rds
/usr/lib64/R/library/bit/help/bit.rdb
/usr/lib64/R/library/bit/help/bit.rdx
/usr/lib64/R/library/bit/help/paths.rds
/usr/lib64/R/library/bit/html/00Index.html
/usr/lib64/R/library/bit/html/R.css
/usr/lib64/R/library/bit/tests/testthat.R
/usr/lib64/R/library/bit/tests/testthat/test-bit.R
/usr/lib64/R/library/bit/tests/testthat/test-bitsort.R
/usr/lib64/R/library/bit/tests/testthat/test-merge.R
/usr/lib64/R/library/bit/tests/testthat/test-old-regtest.R
/usr/lib64/R/library/bit/tests/testthat/test-rle.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bit/libs/bit.so
/usr/lib64/R/library/bit/libs/bit.so.avx2
/usr/lib64/R/library/bit/libs/bit.so.avx512
