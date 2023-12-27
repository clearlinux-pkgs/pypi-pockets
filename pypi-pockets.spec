#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pockets
Version  : 0.9.1
Release  : 11
URL      : https://files.pythonhosted.org/packages/df/8e/0601097cfcce2e8c2297db5080e9719f549c2bd4b94420ddc8d3f848bbca/pockets-0.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/df/8e/0601097cfcce2e8c2297db5080e9719f549c2bd4b94420ddc8d3f848bbca/pockets-0.9.1.tar.gz
Summary  : A collection of helpful Python tools!
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pockets-license = %{version}-%{release}
Requires: pypi-pockets-python = %{version}-%{release}
Requires: pypi-pockets-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(six)

%description
====================================
        
        *Let me check my pockets...*
        ----------------------------
        
        The Pockets library pulls together many of the Python helper functions I've
        found useful over the years.
        
        If you've worked on a project that exports an API and accesses a data store,

%package license
Summary: license components for the pypi-pockets package.
Group: Default

%description license
license components for the pypi-pockets package.


%package python
Summary: python components for the pypi-pockets package.
Group: Default
Requires: pypi-pockets-python3 = %{version}-%{release}

%description python
python components for the pypi-pockets package.


%package python3
Summary: python3 components for the pypi-pockets package.
Group: Default
Requires: python3-core
Provides: pypi(pockets)
Requires: pypi(six)

%description python3
python3 components for the pypi-pockets package.


%prep
%setup -q -n pockets-0.9.1
cd %{_builddir}/pockets-0.9.1
pushd ..
cp -a pockets-0.9.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656394781
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pockets
cp %{_builddir}/pockets-0.9.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pockets/c4ae5a01d4e8f961d887ccbfafd4b3a5e903835a
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
/usr/share/package-licenses/pypi-pockets/c4ae5a01d4e8f961d887ccbfafd4b3a5e903835a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
