# TODO:
# - fix %%files (doc to %%doc, no .py, remove unused files)
%include	/usr/lib/rpm/macros.python

Summary:	SPE - Stani's Python Editor
Name:		SPE
Version:	0.1.8.c
%define		_wx 2.4.1.2
%define		_bl 2.28
Release:	0.1
License:	LGPL 2.1+ (except sm library <free to use> and sm_idle <PSF>)
Group:		Applications/Text
Source0:	http://spe.pycs.net/releases/%{name}-%{version}-wx%{_wx}.-bl%{_bl}.zip
# Source0-md5:	252ace7ecf6e9c210f29a4c38ed742e8
URL:		http://spe.pycs.net/
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-wxPython >= %{_wx}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spe is a python IDE with auto-indentation, auto completion, call tips, syntax
coloring, syntax highlighting, class explorer, source index, auto todo list,
sticky notes, integrated pycrust shell, python file browser, recent file
browser, drag&drop, context help, ... Special is its blender support with a
blender 3d object browser and its ability to run interactively inside blender.
Spe is extensible with boa. 

%prep
%setup -q -n %{name}-%{version}-wx%{_wx}.-bl%{_bl}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*
