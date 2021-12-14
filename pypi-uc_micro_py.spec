#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-uc_micro_py
Version  : 1.0.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/8d/01/865815288cb9b2cd2e7181bbe17fe55e4e3d30f29f28efcef2be4247e6a0/uc-micro-py-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8d/01/865815288cb9b2cd2e7181bbe17fe55e4e3d30f29f28efcef2be4247e6a0/uc-micro-py-1.0.1.tar.gz
Summary  : Micro subset of unicode data files for linkify-it-py projects.
Group    : Development/Tools
License  : MIT
Requires: pypi-uc_micro_py-python = %{version}-%{release}
Requires: pypi-uc_micro_py-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# uc.micro-py
[![pypi](https://img.shields.io/pypi/v/uc-micro-py)](https://pypi.org/project/uc-micro-py/)
[![CI](https://github.com/tsutsu3/uc.micro-py/workflows/CI/badge.svg?branch=main)](https://github.com/tsutsu3/uc.micro-py/actions)
[![codecov](https://codecov.io/gh/tsutsu3/uc.micro-py/branch/main/graph/badge.svg?token=5Y7559D69U)](https://codecov.io/gh/tsutsu3/uc.micro-py)

%package python
Summary: python components for the pypi-uc_micro_py package.
Group: Default
Requires: pypi-uc_micro_py-python3 = %{version}-%{release}

%description python
python components for the pypi-uc_micro_py package.


%package python3
Summary: python3 components for the pypi-uc_micro_py package.
Group: Default
Requires: python3-core
Provides: pypi(uc_micro_py)

%description python3
python3 components for the pypi-uc_micro_py package.


%prep
%setup -q -n uc-micro-py-1.0.1
cd %{_builddir}/uc-micro-py-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639061896
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
