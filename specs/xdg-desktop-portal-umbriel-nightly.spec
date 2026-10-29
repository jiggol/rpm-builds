%{!?snapshot:%global snapshot git0.unknown}
%{!?upstream_version:%global upstream_version 0.1.0}

Name:           xdg-desktop-portal-umbriel-nightly
Version:        %{upstream_version}
Release:        0.%{snapshot}%{?dist}
Summary:        Development snapshot of the XDG Desktop Portal backend for Umbriel
License:        MIT
URL:            https://github.com/noctalia-dev/xdg-desktop-portal-umbriel
Source0:        xdg-desktop-portal-umbriel-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 1.3
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(sdbus-c++) >= 2.0
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.39
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(gtk4) >= 4.12
BuildRequires:  glib2-devel
BuildRequires:  systemd-rpm-macros

Requires:       xdg-desktop-portal
Provides:       xdg-desktop-portal-umbriel = %{version}-%{release}

%description
An unofficial Git snapshot of Umbriel's XDG Desktop Portal backend,
including the GTK4 screen and window sharing picker. Provides
ScreenCast, Screenshot, and InputCapture portals.

%prep
%autosetup -n xdg-desktop-portal-umbriel-%{version}

%build
%meson -Dtests=false -Dpicker=enabled
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libexecdir}/xdg-desktop-portal-umbriel
%{_libexecdir}/umbriel-share-picker
%{_datadir}/xdg-desktop-portal/portals/umbriel.portal
%{_datadir}/xdg-desktop-portal/umbriel-portals.conf
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.umbriel.service
%{_userunitdir}/xdg-desktop-portal-umbriel.service
