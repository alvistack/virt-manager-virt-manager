# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: virt-manager
Epoch: 100
Version: 4.0.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Desktop tool for managing virtual machines via libvirt
License: GPLv2+
URL: https://github.com/virt-manager/virt-manager/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: gettext
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-docutils
BuildRequires: python3-setuptools
Requires: dconf
Requires: gtk-vnc2
Requires: gtk3 >= 3.22.0
Requires: gtksourceview4
Requires: libvirt-glib >= 0.0.9
Requires: python3
Requires: python3-gobject >= 3.31.3
Requires: spice-gtk3
Requires: virt-manager-common = %{epoch}:%{version}-%{release}
Requires: vte291

%description
Virtual Machine Manager provides a graphical tool for administering
virtual machines for KVM, Xen, and LXC. Start, stop, add or remove
virtual devices, connect to a graphical or serial console, and see
resource usage statistics for existing VMs on local or remote machines.
Uses libvirt as the backend management API.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
python3 setup.py \
    --no-update-icon-cache \
    --no-compile-schemas \
    install --no-compile -O1 --root=%{buildroot}
find %{buildroot}%{_datadir}/virt-manager -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{_datadir}/virt-manager

%package -n virt-common
Summary: Common files used by the different Virtual Machine Manager interfaces
Requires: genisoimage
Requires: libosinfo >= 0.2.10
Requires: python3-argcomplete
Requires: python3-gobject-base
Requires: python3-libvirt
Requires: python3-libxml2
Requires: python3-requests
Requires: xorriso

%description -n virt-common
Common files used by the different virt-manager interfaces, as well as
virt-install related tools.

%package -n virt-install
Summary: Utilities for installing virtual machines
Requires: libvirt-client
Requires: virt-manager-common = %{epoch}:%{version}-%{release}
Provides: virt-clone
Provides: virt-xml

%description -n virt-install
Package includes several command line utilities, including virt-install
(build and install new VMs) and virt-clone (clone an existing virtual
machine).

%files
%doc COPYING
%doc NEWS.md
%doc README.md
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/schemas
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%dir %{_datadir}/virt-manager/ui
%{_bindir}/virt-manager
%{_datadir}/applications/virt-manager.desktop
%{_datadir}/glib-2.0/schemas/org.virt-manager.virt-manager.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/virt-manager.appdata.xml
%{_datadir}/virt-manager/icons
%{_datadir}/virt-manager/ui/*.ui
%{_datadir}/virt-manager/virtManager
%{_mandir}/man1/virt-manager.1*

%files -n virt-common
%dir %{_datadir}/virt-manager
%dir %{_datadir}/locale/*
%dir %{_datadir}/locale/*/LC_MESSAGES
%{_datadir}/locale/*/LC_MESSAGES/virt-manager.mo
%{_datadir}/virt-manager/virtinst

%files -n virt-install
%{_bindir}/virt-clone
%{_bindir}/virt-install
%{_bindir}/virt-xml
%{_datadir}/bash-completion/completions/virt-clone
%{_datadir}/bash-completion/completions/virt-install
%{_datadir}/bash-completion/completions/virt-xml
%{_mandir}/man1/virt-clone.1*
%{_mandir}/man1/virt-install.1*
%{_mandir}/man1/virt-xml.1*

%changelog
