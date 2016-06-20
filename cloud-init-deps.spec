%global pyserial_version 3.0.1
%global jsonpatch_version 1.12
%global jsonpointer_version 1.10
%global prettytable_version 0.7.2
%global cloud_utils_version 0.29

Name: cloud-init-deps
Version: 20160520
Release: 3
Summary: Dependencies for cloud-init
License: BSD and GPLv3

Source0: https://pypi.io/packages/source/j/jsonpointer/jsonpointer-%{jsonpointer_version}.tar.gz
Source1: https://pypi.io/packages/source/j/jsonpatch/jsonpatch-%{jsonpatch_version}.tar.gz
Source2: https://pypi.io/packages/source/p/pyserial/pyserial-%{pyserial_version}.tar.gz
Source3: https://pypi.io/packages/source/p/prettytable/prettytable-%{prettytable_version}.tar.gz
Source4: https://launchpad.net/cloud-utils/trunk/%{cloud_utils_version}/+download/cloud-utils-%{cloud_utils_version}.tar.gz

Buildrequires: python
Buildrequires: python-setuptools
Buildarch: noarch

Provides: bundled(python-jsonpointer) == %{jsonpointer_version}
Provides: bundled(python-jsonpatch) == %{jsonpatch_version}
Provides: bundled(python-prettytable) == %{prettytable_version}
Provides: bundled(pyserial) == %{pyserial_version}
Provides: bundled(cloud-utils-growpart) == %{cloud_utils_version}

%description
%{summary}

%prep
%setup -q -c -T -b0 -b1 -b2 -b3 -b4

%build

(
cd jsonpatch-%{jsonpatch_version}
python setup.py build
)

(
cd jsonpointer-%{jsonpointer_version}
python setup.py build
)

(
cd prettytable-%{prettytable_version}
python setup.py build
)

(
cd pyserial-%{pyserial_version}
python setup.py build
)

%install

(
cd jsonpatch-%{jsonpatch_version}
python setup.py install --root $RPM_BUILD_ROOT --install-purelib %{python_sitelib}/cloud-init-deps
rm $RPM_BUILD_ROOT%{_bindir}/* || true
for doc in AUTHORS README.md COPYING; do
mv $doc $doc.jsonpatch
done
)

(
cd jsonpointer-%{jsonpointer_version}
python setup.py install --root $RPM_BUILD_ROOT --install-purelib %{python_sitelib}/cloud-init-deps
rm $RPM_BUILD_ROOT%{_bindir}/* || true
for doc in AUTHORS README.md COPYING; do
mv $doc $doc.jsonpointer
done
)

(
cd prettytable-%{prettytable_version}
python setup.py install --root $RPM_BUILD_ROOT --install-purelib %{python_sitelib}/cloud-init-deps
rm $RPM_BUILD_ROOT%{_bindir}/* || true
for doc in README COPYING; do
mv $doc $doc.prettytable
done
)

(
cd pyserial-%{pyserial_version}
python setup.py install --root $RPM_BUILD_ROOT --install-purelib %{python_sitelib}/cloud-init-deps
rm $RPM_BUILD_ROOT%{_bindir}/* || true
for doc in README.rst LICENSE.txt; do
mv $doc $doc.pyserial
done
)

(
cd cloud-utils-%{cloud_utils_version}
install -m 755 -d $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 bin/growpart $RPM_BUILD_ROOT%{_bindir}/growpart
install -m 644 man/growpart.1 $RPM_BUILD_ROOT%{_mandir}/man1/growpart.1
)

cat > $RPM_BUILD_ROOT%{python_sitelib}/cloud-init-deps.pth <<EOF
cloud-init-deps
EOF

%files

%doc jsonpatch-%{jsonpatch_version}/AUTHORS.jsonpatch
%doc jsonpatch-%{jsonpatch_version}/README.md.jsonpatch
%doc jsonpatch-%{jsonpatch_version}/COPYING.jsonpatch

%doc jsonpointer-%{jsonpointer_version}/AUTHORS.jsonpointer
%doc jsonpointer-%{jsonpointer_version}/README.md.jsonpointer
%doc jsonpointer-%{jsonpointer_version}/COPYING.jsonpointer

%doc prettytable-%{prettytable_version}/COPYING.prettytable
%doc prettytable-%{prettytable_version}/README.prettytable

%doc pyserial-%{pyserial_version}/README.rst.pyserial
%doc pyserial-%{pyserial_version}/LICENSE.txt.pyserial

%{python_sitelib}/cloud-init-deps/serial
%{python_sitelib}/cloud-init-deps/pyserial*egg-info
%{python_sitelib}/cloud-init-deps/jsonpatch.py*
%{python_sitelib}/cloud-init-deps/jsonpatch*egg-info
%{python_sitelib}/cloud-init-deps/jsonpointer.py*
%{python_sitelib}/cloud-init-deps/jsonpointer*egg-info
%{python_sitelib}/cloud-init-deps/prettytable.py*
%{python_sitelib}/cloud-init-deps/prettytable*egg-info

%{python_sitelib}/cloud-init-deps.pth

%{_bindir}/growpart
%{_mandir}/man1/growpart.1*

%changelog
* Mon Jun 20 2016 Lars Kellogg-Stedman <lars@redhat.com> - 20160520-3
- initial cloud-init-deps package
