Summary:	Apertium pipeline module to detect proper nouns
Summary(pl.UTF-8):	Moduł potoku Apertium do rozpoznawania rzeczowników własnych
Name:		apertium-pn-recogniser
Version:	0.1.0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/%{name}-%{version}.tar.gz
# Source0-md5:	48e23ad48e54b8f5a251a7175cc938b4
URL:		http://www.apertium.org/
BuildRequires:	apertium >= 3.1.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bash
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	lttoolbox-devel >= 3.1.0
Requires:	apertium >= 3.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is a module for the Apertium pipeline which detects
proper nouns in the input and marks them as unknown words so that the
rest of the modules in the pipeline do not process them. This avoids
the common case of wrong translations of source-language proper nouns
which are also common nouns according to the dictionaries. The proper
noun recogniser is mainly based on the one already included in the
Freeling project (<http://www.lsi.upc.edu/~nlp/freeling/>).

%description -l pl.UTF-8
Ten program jest modułem dla potoku Apertium wykrywającym na wejściu
rzeczowniki własnych i zaznaczający je jako nieznane słowa w ten
sposób, że reszta modułów w potoku nie będzie ich przetwarzała.
Zapobiega to błędnemu tłumaczeniu rzeczowników własnych z języka
źródłowego, w którym są także rzeczownikami pospolitymi, występującymi
w słownikach. Moduł rozpoznający rzeczowniki własne jest oparty
głównie na module włączonym do projektu Freeling
(<http://www.lsi.upc.edu/~nlp/freeling/>).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO.txt doc/decisiones-diseno.txt
%attr(755,root,root) %{_bindir}/apertium-pn-recogniser
%attr(755,root,root) %{_bindir}/apertium-pn-recogniser-final
