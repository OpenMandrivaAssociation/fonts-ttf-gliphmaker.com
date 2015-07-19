%define pkgname gliphmaker.com-fonts

Summary: Fonts from gliphmaker.com Web-site
Name: fonts-ttf-gliphmaker.com
Version: 1.0
Release: 4
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
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/gliphmaker.com

install -m 644 *.?tf %{buildroot}%{_datadir}/fonts/TTF/gliphmaker.com
ttmkfdir %{buildroot}%{_datadir}/fonts/TTF/gliphmaker.com > %{buildroot}%{_datadir}/fonts/TTF/gliphmaker.com/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/gliphmaker.com/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/gliphmaker.com \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-gliphmaker.com:pri=50

%files
%dir %{_datadir}/fonts/TTF/gliphmaker.com
%{_datadir}/fonts/TTF/gliphmaker.com/*.ttf
%{_datadir}/fonts/TTF/gliphmaker.com/*.otf
%verify(not mtime) %{_datadir}/fonts/TTF/gliphmaker.com/fonts.dir
%{_datadir}/fonts/TTF/gliphmaker.com/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-gliphmaker.com:pri=50

