# TODO:
# - fix %%files (doc to %%doc, no .py, remove unused files)
%define	_wx	2.6.1.0
#
Summary:	SPE - Stani's Python Editor
Summary(pl.UTF-8):	SPE - pythonowy edytor Staniego
Name:		SPE
Version:	0.8.2.a
Release:	5
License:	LGPL 2.1+ (except sm library <free to use> and sm_idle <PSF>)
Group:		Applications/Text
Source0:	http://download.berlios.de/python/%{name}-%{version}-wx%{_wx}.tar.gz
# Source0-md5:	d5d5a55414aa2410ac430f7e79b271e5
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://spe.pycs.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
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

%description -l pl.UTF-8
Spe (Stani's Python Editor) to pythonowe IDE z automatycznym
wykonywaniem wcięć, automatycznym dopełnianiem, podpowiedziami
wywołań, kolorowaniem składni, podświetlaniem składni, eksploratorem
klas, indeksem źródeł, automatyczną listą TODO, przyklejanymi
notatkami, zintegrowaną powłoką pycrust, przeglądarką plików
pythonowych, przeglądarką ostatnio używanych plików, obsługą w stylu
przeciągnij-i-upuść, pomocą kontekstową... Specjalną rzeczą jest
wsparcie dla blendera z przeglądarką obiektów blendera 3D i
możliwością automatycznego uruchamiania z poziomu blendera. Spe jest
rozszerzalne przy pomocy boa.

%prep
%setup -q -n %{name}-%{version}-wx%{_wx}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%py_install

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
