#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

Name:           dmxproto
Version:        2.3.1
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          Development/System
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)

%description
%{summary}.

%prep
%setup -q

%build

./autogen.sh
%reconfigure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs


%files
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc

