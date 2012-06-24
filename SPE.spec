# TODO:
# - fix %%files (doc to %%doc, no .py, remove unused files)

%define	_wx	2.5.2.8
%define	_bl	2.35

Summary:	SPE - Stani's Python Editor
Summary(pl):	SPE - pythonowy edytor Staniego
Name:		SPE
Version:	0.7.2.a
Release:	0.1
License:	LGPL 2.1+ (except sm library <free to use> and sm_idle <PSF>)
Group:		Applications/Text
Source0:	http://projects.blender.org/frs/download.php/244/%{name}-%{version}-linux-mac.tgz
# Source0-md5:	f3c19dcbab4d1e77b4ef34f7916d8235
URL:		http://spe.pycs.net/
BuildRequires:	rpm-pythonprov
BuildRequires:	findutils
BuildRequires:	python-devel
%pyrequires_eq	python-modules
Requires:	python-wxPython >= %{_wx}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spe is a python IDE with auto-indentation, auto completion, call tips,
syntax coloring, syntax highlighting, class explorer, source index,
auto todo list, sticky notes, integrated pycrust shell, python file
browser, recent file browser, drag&drop, context help, ... Special is
its blender support with a blender 3d object browser and its ability
to run interactively inside blender. Spe is extensible with boa. 

%description -l pl
Spe (Stani's Python Editor) to pythonowe IDE z automatycznym
wykonywaniem wci��, automatycznym dope�nianiem, podpowiedziami
wywo�a�, kolorowaniem sk�adni, pod�wietlaniem sk�adni, eksploratorem
klas, indeksem �r�de�, automatyczn� list� TODO, przyklejanymi
notatkami, zintegrowan� pow�ok� pycrust, przegl�dark� plik�w
pythonowych, przegl�dark� ostatnio u�ywanych plik�w, obs�ug� w stylu
przeci�gnij-i-upu��, pomoc� kontekstow�... Specjaln� rzecz� jest
wsparcie dla blendera z przegl�dark� obiekt�w blendera 3D i
mo�liwo�ci� automatycznego uruchamiania z poziomu blendera. Spe jest
rozszerzalne przy pomocy boa.

%prep
%setup -q -n %{name}-0.7.0.a-wx%{_wx}.-bl%{_bl}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.py' -exec rm "{}" ";"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*
