#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/emprint emprint; \
#cd emprint; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "emprint" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf emprint-$PKG_VERSION.tar.xz emprint/ --exclude .svn --exclude .*ignore

%define svnrev 84427

Summary:	E17 screen captire utility
Name:		emprint
Version:	0.1.0
Release:	2.%{svnrev}.1
License:	BSD
Group:		System/Servers
URL:		http://www.enlightenment.org/
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
%makeinstall_std

%files
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/*
%{_datadir}/%{name}



%changelog
* Thu Jan 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.1.0-2.64443.1
+ Revision: 760456
- new snapshot 0.1.0.64443
- cleaned up spec
- merged UnityLinux spec

* Mon Jan 03 2011 Crispin Boylan <crisb@mandriva.org> 0.1.0-1.svn20101107.1mdv2011.0
+ Revision: 627854
- New release with updated tarball

* Sun Jul 25 2010 Funda Wang <fwang@mandriva.org> 0.0.1-2.svn20100624.3mdv2011.0
+ Revision: 558264
- new snapshot

* Sat Aug 08 2009 Funda Wang <fwang@mandriva.org> 0.0.1-2.svn20090503.3mdv2010.0
+ Revision: 411573
- rebuild for new ecore

* Wed Jul 08 2009 Funda Wang <fwang@mandriva.org> 0.0.1-2.svn20090503.2mdv2010.0
+ Revision: 393506
- rebuild

* Sun May 03 2009 Funda Wang <fwang@mandriva.org> 0.0.1-2.svn20090503.1mdv2010.0
+ Revision: 370824
- New snapshot to build with newer ecore

* Mon Mar 02 2009 Antoine Ginies <aginies@mandriva.com> 0.0.1-2.svn20090227.1mdv2009.1
+ Revision: 346942
- SVN SNAPSHOT 20090227, release 0.0.1, adjust buildrequires
- adjust source tag
- adjust setup tag
- SVN SNAPSHOT 20090227, release 0.0.1, adjust buildrequires

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.0.1-2.cvs20080203.1mdv2009.0
+ Revision: 266624
- rebuild early 2009.0 package (before pixel changes)

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.0.1-0.cvs20080203.1mdv2009.0
+ Revision: 167866
- fix no-buildroot-tag

* Sun Feb 03 2008 Austin Acton <austin@mandriva.org> 0.0.1-0.cvs20080203.1mdv2008.1
+ Revision: 161745
- import emprint


