# TODO:
# - fix %%files (doc to %%doc, no .py, remove unused files)

%define	_wx	2.5.2.8
%define	_bl	2.35

Summary:	SPE - Stani's Python Editor
Summary(pl):	SPE - pythonowy edytor Staniego
Name:		SPE
Version:	0.7.2.b
Release:	0.1
License:	LGPL 2.1+ (except sm library <free to use> and sm_idle <PSF>)
Group:		Applications/Text
Source0:	http://projects.blender.org/frs/download.php/252/%{name}-%{version}-wx%{_wx}.-bl%{_bl}.zip
# Source0-md5:	2f72f638b6fb850b0028193a03236948
URL:		http://spe.pycs.net/
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
wykonywaniem wciêæ, automatycznym dope³nianiem, podpowiedziami
wywo³añ, kolorowaniem sk³adni, pod¶wietlaniem sk³adni, eksploratorem
klas, indeksem ¼róde³, automatyczn± list± TODO, przyklejanymi
notatkami, zintegrowan± pow³ok± pycrust, przegl±dark± plików
pythonowych, przegl±dark± ostatnio u¿ywanych plików, obs³ug± w stylu
przeci±gnij-i-upu¶æ, pomoc± kontekstow±... Specjaln± rzecz± jest
wsparcie dla blendera z przegl±dark± obiektów blendera 3D i
mo¿liwo¶ci± automatycznego uruchamiania z poziomu blendera. Spe jest
rozszerzalne przy pomocy boa.

%prep
%setup -q -n %{name}-%{version}-wx%{_wx}.-bl%{_bl}

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
