Name:           dmxproto
Version:        2.3.1
Release:        0
License:        MIT
Summary:        X.org DMXProto protocol headers
Url:            http://cgit.freedesktop.org/xorg/proto/dmxproto/
Group:          Development/X11 Protocols
Source0:        %{name}-%{version}.tar.bz2
Source1001:     dmxproto.manifest
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildArch:      noarch

%description
X.org DMXProto protocol headers.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

%__make %{?_smp_mflags}

%install
%make_install

%remove_docs


%files
%manifest %{name}.manifest
%license COPYING
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc

