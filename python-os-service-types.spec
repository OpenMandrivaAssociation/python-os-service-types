Name:		python-os-service-types
Version:	1.7.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/os-service-types/os-service-types-%{version}.tar.gz
Summary:	Python library for consuming OpenStack sevice-types-authority data
URL:		https://pypi.org/project/os-service-types/
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Python library for consuming OpenStack sevice-types-authority data

%files
%{py_sitedir}/os_service_types
%{py_sitedir}/os_service_types-*.*-info
