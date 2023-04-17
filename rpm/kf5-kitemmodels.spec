%global kf5_version 5.105.0

Name: opt-kf5-kitemmodels
Version: 5.105.0
Release: 1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with item models

License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/kitemmodels

Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros

BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qtdeclarative-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtdeclarative

%description
KDE Frameworks 5 Tier 1 addon with item models.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/kitemmodels.*
%{_opt_kf5_libdir}/libKF5ItemModels.so.*
%{_opt_kf5_qmldir}/org/kde/kitemmodels/

%files devel

%{_opt_kf5_includedir}/KF5/KItemModels/
%{_opt_kf5_libdir}/libKF5ItemModels.so
%{_opt_kf5_libdir}/cmake/KF5ItemModels/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KItemModels.pri
