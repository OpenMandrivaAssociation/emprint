%define gitdate 20150506

Summary:	E17 screen captire utility
Name:		emprint
Version:	0.1.0
Release:	3.2
License:	BSD
Group:		System/Servers
Url:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.%{gitdate}.tar.xz
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(imlib2)

%description
Emprint is a utility for taking screenshots of the entire screen, a specific
window, or a specific region. It is written with the Enlightenment Foundation
Libraries.

%files
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/*
%{_datadir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{gitdate}

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

