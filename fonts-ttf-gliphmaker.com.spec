%define pkgname gliphmaker.com-fonts

Summary: Fonts from gliphmaker.com Web-site
Name: fonts-ttf-gliphmaker.com
Version: 1.0
Release: %mkrel 1
License: Other/Non-commertial
Group: System/Fonts/True type
URL: http://www.gliphmaker.com/
Source0: %{pkgname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: freetype-tools

%description
A collection of non-commertial fonts from gliphmaker.com Web-site

%prep
%setup -q -n %{pkgname}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/gliphmaker.com

install -m 644 *.?tf $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/gliphmaker.com
ttmkfdir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/gliphmaker.com > $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/gliphmaker.com/fonts.dir
ln -s fonts.dir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/gliphmaker.com/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/gliphmaker.com \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-gliphmaker.com:pri=50

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_datadir}/fonts/TTF/gliphmaker.com
%{_datadir}/fonts/TTF/gliphmaker.com/*.ttf
%{_datadir}/fonts/TTF/gliphmaker.com/*.otf
%verify(not mtime) %{_datadir}/fonts/TTF/gliphmaker.com/fonts.dir
%{_datadir}/fonts/TTF/gliphmaker.com/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-gliphmaker.com:pri=50




%changelog
* Fri Jul 22 2011 Sergey Zhemoitel <serg@mandriva.org> 1.0-1mdv2012.0
+ Revision: 690971
- imported package fonts-ttf-gliphmaker.com

