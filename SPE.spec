# TODO:
# - fix %%files (doc to %%doc, no .py, remove unused files)
%define	_wx	2.6.1.0
#
Summary:	SPE - Stani's Python Editor
Summary(pl):	SPE - pythonowy edytor Staniego
Name:		SPE
Version:	0.8.2.a
Release:	1
License:	LGPL 2.1+ (except sm library <free to use> and sm_idle <PSF>)
Group:		Applications/Text
Source0:	http://download.berlios.de/python/%{name}-%{version}-wx%{_wx}.tar.gz
# Source0-md5:	d5d5a55414aa2410ac430f7e79b271e5
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://spe.pycs.net/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-modules
Requires:	pydoc
%pyrequires_eq	python-modules
Requires:	python-wxPython >= %{_wx}
# below is needed - SPE doesn't start without "hacked" release of wxPython (reporting version issue)
Requires:	python-wxPython >= 2.6.1.0-3
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
%setup -q -n %{name}-%{version}-wx%{_wx}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

# SPE doesn't work without *.py files so don't remove them
#%%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
