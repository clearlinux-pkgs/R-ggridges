#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ggridges
Version  : 0.5.1
Release  : 24
URL      : https://cran.r-project.org/src/contrib/ggridges_0.5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ggridges_0.5.1.tar.gz
Summary  : Ridgeline Plots in 'ggplot2'
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : R-DAAG
BuildRequires : R-assertthat
BuildRequires : R-dplyr
BuildRequires : R-forcats
BuildRequires : R-ggplot2
BuildRequires : R-ggplot2movies
BuildRequires : R-labeling
BuildRequires : R-mime
BuildRequires : R-plyr
BuildRequires : R-purrr
BuildRequires : R-scales
BuildRequires : R-utf8
BuildRequires : R-viridis
BuildRequires : buildreq-R

%description
ggridges
========
[![Build Status](https://travis-ci.org/clauswilke/ggridges.svg?branch=master)](https://travis-ci.org/clauswilke/ggridges) [![Coverage Status](https://img.shields.io/codecov/c/github/clauswilke/ggridges/master.svg)](https://codecov.io/github/clauswilke/ggridges?branch=master) [![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/ggridges)](https://CRAN.R-project.org/package=ggridges) [![CRAN\_Downloads\_Badge](http://cranlogs.r-pkg.org/badges/ggridges)](http://cranlogs.r-pkg.org/downloads/total/last-month/ggridges)

%prep
%setup -q -c -n ggridges

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552897091

%install
export SOURCE_DATE_EPOCH=1552897091
rm -rf %{buildroot}
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggridges
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggridges
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggridges
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  ggridges || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ggridges/DESCRIPTION
/usr/lib64/R/library/ggridges/INDEX
/usr/lib64/R/library/ggridges/LICENSE
/usr/lib64/R/library/ggridges/Meta/Rd.rds
/usr/lib64/R/library/ggridges/Meta/data.rds
/usr/lib64/R/library/ggridges/Meta/features.rds
/usr/lib64/R/library/ggridges/Meta/hsearch.rds
/usr/lib64/R/library/ggridges/Meta/links.rds
/usr/lib64/R/library/ggridges/Meta/nsInfo.rds
/usr/lib64/R/library/ggridges/Meta/package.rds
/usr/lib64/R/library/ggridges/Meta/vignette.rds
/usr/lib64/R/library/ggridges/NAMESPACE
/usr/lib64/R/library/ggridges/NEWS
/usr/lib64/R/library/ggridges/R/ggridges
/usr/lib64/R/library/ggridges/R/ggridges.rdb
/usr/lib64/R/library/ggridges/R/ggridges.rdx
/usr/lib64/R/library/ggridges/data/Rdata.rdb
/usr/lib64/R/library/ggridges/data/Rdata.rds
/usr/lib64/R/library/ggridges/data/Rdata.rdx
/usr/lib64/R/library/ggridges/doc/gallery.R
/usr/lib64/R/library/ggridges/doc/gallery.Rmd
/usr/lib64/R/library/ggridges/doc/gallery.html
/usr/lib64/R/library/ggridges/doc/index.html
/usr/lib64/R/library/ggridges/doc/introduction.R
/usr/lib64/R/library/ggridges/doc/introduction.Rmd
/usr/lib64/R/library/ggridges/doc/introduction.html
/usr/lib64/R/library/ggridges/help/AnIndex
/usr/lib64/R/library/ggridges/help/aliases.rds
/usr/lib64/R/library/ggridges/help/figures/README-diamonds-1.png
/usr/lib64/R/library/ggridges/help/ggridges.rdb
/usr/lib64/R/library/ggridges/help/ggridges.rdx
/usr/lib64/R/library/ggridges/help/paths.rds
/usr/lib64/R/library/ggridges/html/00Index.html
/usr/lib64/R/library/ggridges/html/R.css
/usr/lib64/R/library/ggridges/tests/figs/deps.txt
/usr/lib64/R/library/ggridges/tests/figs/geom-density-ridges/geom-density-ridges-basic.svg
/usr/lib64/R/library/ggridges/tests/figs/geom-density-ridges/geom-density-ridges-no-trailing-lines.svg
/usr/lib64/R/library/ggridges/tests/testthat.R
/usr/lib64/R/library/ggridges/tests/testthat/Rplots.pdf
/usr/lib64/R/library/ggridges/tests/testthat/test_geom_density_ridges.R
/usr/lib64/R/library/ggridges/tests/testthat/test_geom_gradient.R
/usr/lib64/R/library/ggridges/tests/testthat/test_geom_vridgeline.R
/usr/lib64/R/library/ggridges/tests/testthat/test_scale_cyclical.R
/usr/lib64/R/library/ggridges/tests/testthat/test_stat_binline.R
/usr/lib64/R/library/ggridges/tests/testthat/test_stat_density_ridges.R
/usr/lib64/R/library/ggridges/tests/testthat/test_theme_ridges.R
/usr/lib64/R/library/ggridges/tests/testthat/test_utils.R
