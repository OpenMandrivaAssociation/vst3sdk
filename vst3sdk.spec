Name:     vst3sdk
Version:	3.7.6
Release:	1
License:	GPL-3.0
Summary:	VST 3 Plug-in SDK
URL:      https://www.steinberg.net/en/company/developers.html
# Use git clone --recursive to pull also all needed submodules. Source archive from release/tag not contains submodules.
Source0:  https://github.com/steinbergmedia/vst3sdk/archive/refs/heads/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pangoft2)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)

%description
This package provides the 'base', 'pluginterfaces' and 'public.sdk' source modules only, necessary for Steinberg VST3 Plug-in and Host application.

%prep
%autosetup -p1

%build
%cmake
  
%make_build
  
%install
%make_install -C build
  
  
%files
