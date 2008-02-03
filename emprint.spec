%define cvs		20080203

Summary: 	E17 screen captire utility
Name: 		emprint
Version: 	0.0.1
Release: 	%mkrel 0.cvs%{cvs}.1
Source:		%{name}-%{cvs}.tar.bz2
License: 	BSD
Group: 		System/Servers
URL: 		http://www.enlightenment.org/
BuildRequires:	imlib2-devel, X11-devel
BuildRequires:	evas-devel
BuildRequires:	ecore-devel
BuildRequires:	edje-devel, edje

%description
Emprint is a utility for taking screenshots of the entire screen, a specific
window, or a specific region. It is written with the Enlightenment Foundation
Libraries.

%prep
%setup -q -n %name

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/*
%{_datadir}/%name
