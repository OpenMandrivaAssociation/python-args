Name:		python-args
Version:	0.1.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/args/args-%{version}.tar.gz
Summary:	Command Arguments for Humans.
URL:		https://pypi.org/project/args/
License:	BSD
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Command Arguments for Humans.

%files
%{py_sitedir}/args.py
%{py_sitedir}/args-*.*-info
