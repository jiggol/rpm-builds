%{!?snapshot:%global snapshot git0.unknown}

Name:           umbriel-git
Version:        0.1.0
Release:        0.%{snapshot}%{?dist}
Summary:        Git snapshot of the Umbriel Wayland compositor
License:        MIT
URL:            https://github.com/noctalia-dev/umbriel
Source0:        umbriel-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 1.3
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.24
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.47
BuildRequires:  pkgconfig(wlroots-0.20) >= 0.20.1
BuildRequires:  pkgconfig(xkbcommon) >= 1.10.0
BuildRequires:  pkgconfig(libinput) >= 1.29
BuildRequires:  pkgconfig(libeis-1.0) >= 1.3
BuildRequires:  pkgconfig(pixman-1) >= 0.43
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(libdrm) >= 2.4.129
BuildRequires:  pkgconfig(libdisplay-info) >= 0.3
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  systemd-rpm-macros

Requires:       xorg-x11-server-Xwayland
Provides:       umbriel = %{version}-%{release}
Conflicts:      umbriel-nightly

%description
Unofficial development snapshot of the Umbriel Wayland compositor,
built from a pinned Git commit for Fedora 44.

%prep
%autosetup -n umbriel-%{version}

%build
%meson -Dtests=disabled -Dtest_ipc=disabled
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/umbriel
%{_bindir}/start-umbriel
%{_datadir}/umbriel/
%{_datadir}/wayland-sessions/umbriel.desktop
%{_userunitdir}/umbriel.service
%{_userunitdir}/umbriel-session.target
%{_userunitdir}/umbriel-shutdown.target
