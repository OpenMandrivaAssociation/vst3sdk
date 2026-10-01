%define _empty_manifest_terminate_build 0

Name:		vst3sdk
Version:	3.7.12
Release:	1
# pluginterfaces is GPL-3.0-only (or Steinberg's proprietary terms; we ship the GPL).
# base and public.sdk are BSD-3-Clause.
License:	BSD-3-Clause AND GPL-3.0-only
Group:		Development/C++
Summary:	VST 3 Plug-in SDK
URL:		https://www.steinberg.net/en/company/developers.html
# Audacity 4.0.1 pins 3.7.12_build_20 as these three commits. The meta
# repository no longer ships base, pluginterfaces and public.sdk itself.
Source0:	https://github.com/steinbergmedia/vst3_base/archive/f0998e7b8424b32ba275cf4218aa56beef29821c.tar.gz
Source1:	https://github.com/steinbergmedia/vst3_pluginterfaces/archive/151ecde4d6ee1c457dcce848342b162461944fe6.tar.gz
Source2:	https://github.com/steinbergmedia/vst3_public_sdk/archive/3fce096d6ee575479753f1aab23033d2e2ffdc6e.tar.gz
Source3:	vst3sdk.pc

%description
This package provides the 'base', 'pluginterfaces' and 'public.sdk' source
modules necessary for Steinberg VST3 plug-ins and host applications.
Consumers compile the sources they need.

%prep
%setup -q -c -T -n %{name}-%{version}
mkdir base pluginterfaces public.sdk
tar -xf %{SOURCE0} --strip-components=1 -C base
tar -xf %{SOURCE1} --strip-components=1 -C pluginterfaces
tar -xf %{SOURCE2} --strip-components=1 -C public.sdk

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a base pluginterfaces public.sdk %{buildroot}%{_datadir}/%{name}/

install -D -m0644 %{SOURCE3} %{buildroot}%{_libdir}/pkgconfig/vst3sdk.pc
sed -i "s|VERSION|%{version}|" %{buildroot}%{_libdir}/pkgconfig/vst3sdk.pc

# %doc and %license keep only the basename, so the three trees cannot share README.md / LICENSE.txt.
mkdir -p doc lic
cp base/README.md doc/base-README.md
cp pluginterfaces/README.md doc/pluginterfaces-README.md
cp public.sdk/README.md doc/public.sdk-README.md
cp base/LICENSE.txt lic/base-LICENSE.txt
cp pluginterfaces/LICENSE.txt lic/pluginterfaces-LICENSE.txt
cp public.sdk/LICENSE.txt lic/public.sdk-LICENSE.txt

%files
%license lic/base-LICENSE.txt lic/pluginterfaces-LICENSE.txt lic/public.sdk-LICENSE.txt
%doc doc/base-README.md doc/pluginterfaces-README.md doc/public.sdk-README.md
%{_libdir}/pkgconfig/vst3sdk.pc
%{_datadir}/vst3sdk/
