%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pname networking_infoblox_tests

%global service networking-infoblox-tests
Name:           python-%{service}
Version:        14.0.0
Release:        0
Summary:        Infoblox IPAM plugin for OpenStack Neutron
License:        ASL 2.0
URL:            https://pypi.org/project/networking-infoblox/

Source0:        http://tarballs.openstack.org/%{service}/%{service}-master.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git

Requires:       python-pbr
Requires:       python-setuptools

# test dependencies requirements
BuildRequires:  python-hacking
BuildRequires:  python-mock
BuildRequires:  python-coverage

%description
This project contains networking-infoblox test framework.

%package -n openstack-%{service}-doc
Summary:        OpenStack networking-infoblox tests Documentation

BuildRequires:  python-sphinx

Requires:    %{name} = %{version}-%{release}

%description -n openstack-%{service}-doc
It contains the documentation of networking-infoblox package.

%prep
%setup -q -n %{service}-%{upstream_version}
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%{__python2} setup.py build

# Build Documentation
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}


install -d -m 755 %{buildroot}%{_sysconfdir}/
mv %{buildroot}/usr/etc/* %{buildroot}%{_sysconfdir}/


%check
%{__python2} setup.py test

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pname}
%{python2_sitelib}/%{pname}-*.egg-info
%{_bindir}/<test binary>
%{_sysconfdir}/<config path>/*

%files -n openstack-%{networking-infoblox}-doc
%license LICENSE
%doc html

%changelog
