Name:		python-os-service-types
Version:	1.9.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/os_service_types/os_service_types-%{version}.tar.gz
Summary:	Python library for consuming OpenStack sevice-types-authority data
URL:		https://pypi.org/project/os-service-types/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pbr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%build -p
export PBR_VERSION="%{version}"

%description
Python library for consuming OpenStack sevice-types-authority data

%files
%{py_sitedir}/os_service_types
%{py_sitedir}/os_service_types-*.*-info
