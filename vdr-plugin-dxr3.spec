
%define plugin	dxr3
%define name	vdr-plugin-%plugin
%define version	0.2.7
%define rel	3

Summary:	VDR plugin: Hardware MPEG decoder
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://sourceforge.net/projects/dxr3plugin
Source:		http://prdownloads.sourceforge.net/dxr3plugin/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
BuildRequires:	ffmpeg-devel
BuildRequires:	em8300-devel
Requires:	vdr-abi = %vdr_abi
Requires:	em8300

%description
DXR3/Hollywood+ MPEG decoder card plugin which allows using such a
card as the primary device of VDR.

%prep
%setup -q -n %plugin-%version

%build
%vdr_plugin_build FFMDIR="%{_includedir}/ffmpeg"

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc CONTRIBUTORS README HISTORY TROUBLESHOOTING
