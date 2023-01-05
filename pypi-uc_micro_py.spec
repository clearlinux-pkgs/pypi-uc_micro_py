#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-uc_micro_py
Version  : 1.0.1
Release  : 11
URL      : https://files.pythonhosted.org/packages/8d/01/865815288cb9b2cd2e7181bbe17fe55e4e3d30f29f28efcef2be4247e6a0/uc-micro-py-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8d/01/865815288cb9b2cd2e7181bbe17fe55e4e3d30f29f28efcef2be4247e6a0/uc-micro-py-1.0.1.tar.gz
Summary  : Micro subset of unicode data files for linkify-it-py projects.
Group    : Development/Tools
License  : MIT
Requires: pypi-uc_micro_py-license = %{version}-%{release}
Requires: pypi-uc_micro_py-python = %{version}-%{release}
Requires: pypi-uc_micro_py-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# uc.micro-py
[![pypi](https://img.shields.io/pypi/v/uc-micro-py)](https://pypi.org/project/uc-micro-py/)
[![CI](https://github.com/tsutsu3/uc.micro-py/workflows/CI/badge.svg?branch=main)](https://github.com/tsutsu3/uc.micro-py/actions)
[![codecov](https://codecov.io/gh/tsutsu3/uc.micro-py/branch/main/graph/badge.svg?token=5Y7559D69U)](https://codecov.io/gh/tsutsu3/uc.micro-py)

%package license
Summary: license components for the pypi-uc_micro_py package.
Group: Default

%description license
license components for the pypi-uc_micro_py package.


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
pushd ..
cp -a uc-micro-py-1.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656364983
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

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-uc_micro_py
cp %{_builddir}/uc-micro-py-1.0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-uc_micro_py/8a4bfa3e5251fba4bf05110c8fa4df5a6abd0225
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-uc_micro_py/8a4bfa3e5251fba4bf05110c8fa4df5a6abd0225

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
