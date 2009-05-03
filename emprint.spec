%define svn 20090503

Summary: 	E17 screen captire utility
Name: 		emprint
Version: 	0.0.1
Release: 	%mkrel 2.svn%{svn}.1
Source:		%{name}-%{version}.tar.bz2
License: 	BSD
Group: 		System/Servers
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://www.enlightenment.org/
BuildRequires:	imlib2-devel, X11-devel
BuildRequires:	evas-devel >= 0.9.9.050
BuildRequires:	ecore-devel >= 0.9.9.060
BuildRequires:	edje-devel >= 0.9.9.050, edje >= 0.9.9.050

%description
Emprint is a utility for taking screenshots of the entire screen, a specific
window, or a specific region. It is written with the Enlightenment Foundation
Libraries.

%prep
%setup -q -n %name-%version

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/*
%{_datadir}/%name
