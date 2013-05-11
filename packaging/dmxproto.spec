Name:           dmxproto
Version:        2.3.1
Release:        1
License:        MIT
Summary:        X.org DMXProto protocol headers
Url:            http://www.x.org
Group:          Development/X11 Protocols
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildArch:      noarch

%description
X.org DMXProto protocol headers.

%prep
%setup -q

%build
%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs


%files
%license COPYING
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc

