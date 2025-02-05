
%define plugin	dxr3
%define name	vdr-plugin-%plugin
%define version	0.2.11
%define rel	1

Summary:	VDR plugin: Hardware MPEG decoder
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		https://sourceforge.net/projects/dxr3plugin
Source:		http://prdownloads.sourceforge.net/dxr3plugin/vdr-%plugin-%version.tgz
# attaches to a hack hook in VDR to inform that the device can only
# handle minimal OSD, fixing subtitling issues
Patch1:		dxr3-subtitles.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0-7
BuildRequires:	ffmpeg-devel
BuildRequires:	em8300-devel
Requires:	vdr-abi = %vdr_abi
Requires:	em8300

%description
DXR3/Hollywood+ MPEG decoder card plugin which allows using such a
card as the primary device of VDR.

%prep
%setup -q -n %plugin-%version
%patch1 -p1
%vdr_plugin_prep

%build
VDR_PLUGIN_EXTRA_FLAGS="-I%{_includedir}/libavcodec -D__STDC_CONSTANT_MACROS"
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
