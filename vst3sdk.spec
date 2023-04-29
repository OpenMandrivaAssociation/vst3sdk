%define _empty_manifest_terminate_build 0

Name:     vst3sdk
Version:	3.7.7
Release:	1
License:	GPL-3.0
Summary:	VST 3 Plug-in SDK
URL:      https://www.steinberg.net/en/company/developers.html
# Use git clone --recursive to pull also all needed submodules. Source archive from release/tag not contains submodules.
Source0:  https://github.com/steinbergmedia/vst3sdk/archive/refs/heads/%{name}-%{version}.tar.gz
Source1:       	vst3sdk.pc
Patch0:		vst3sdk-buildfix.patch
Patch1:		missing-include.patch

BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pangoft2)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: stdc++-devel
BuildRequires: stdc++-static-devel

%description
This package provides the 'base', 'pluginterfaces' and 'public.sdk' source modules only, necessary for Steinberg VST3 Plug-in and Host application.

%prep
%autosetup -p1
#cmake \
#	-G Ninja
#
%build
#ninja_build -C build

%install
#ninja_install -C build

# Try without compilation
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}/

install -D -m0644 cmake/modules/*.cmake -t %{buildroot}%{_datadir}/cmake/%{name}/

install -D -m0644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/vst3sdk.pc
sed -i "s|VERSION|%{version}|" %{buildroot}%{_libdir}/pkgconfig/vst3sdk.pc


%files
