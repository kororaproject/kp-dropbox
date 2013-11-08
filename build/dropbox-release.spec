Name:       dropbox-release
Version:    1.0
Release:    1%{?dist}
Summary:    Dropbox repository configuration

Group:      System Environment/Base
License:    Unknown
URL:        http://www.dropbox.com
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch: noarch

%description
Dropbox repository configuration.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 dropbox.repo $RPM_BUILD_ROOT/etc/yum.repos.d/

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 RPM-GPG-KEY-dropbox $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/etc/pki/rpm-gpg/RPM-GPG-KEY-dropbox
%config(noreplace) /etc/yum.repos.d/dropbox.repo

%changelog
* Sat Nov 2013 Chris Smart <csmart@kororaproject.org> - 1.0-1
- Initial package.
