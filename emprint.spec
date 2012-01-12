#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/emprint emprint; \
#cd emprint; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "emprint" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf emprint-$PKG_VERSION.tar.xz emprint/ --exclude .svn --exclude .*ignore

%define svnrev 64443

Summary: 	E17 screen captire utility
Name: 		emprint
Version:	0.1.0
Release:	2.%{svnrev}.1
License: 	BSD
URL: 		http://www.enlightenment.org/
Group: 		System/Servers
Source0:	%{name}-%{version}.%{svnrev}.tar.xz

BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(imlib2)

%description
Emprint is a utility for taking screenshots of the entire screen, a specific
window, or a specific region. It is written with the Enlightenment Foundation
Libraries.

%prep
%setup -qn %{name}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/*
%{_datadir}/%name

