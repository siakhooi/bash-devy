Name:           siakhooi-devy
Version:        0.10.0
Release:        1%{?dist}
Summary:        dev scripts for devcontainers/wsl

License:        MIT
URL:            https://github.com/siakhooi/bash-devy
Source0:        https://github.com/siakhooi/%{name}/archive/refs/tags/${version}.tar.gz
BuildArch:      noarch

Requires:       bash
Requires:       siakhooi-devutils

%description
dev scripts for devcontainers/wsl

%install
%{__mkdir}   -v -p %{buildroot}%{_bindir}
%{__mkdir}   -v -p %{buildroot}/usr/share/licenses/siakhooi-devy
%{__install} -v -m 0755 %{_topdir}/BUILD/usr/bin/* %{buildroot}%{_bindir}
%{__install} -v -m 644  %{_topdir}/BUILD/LICENSE %{buildroot}/usr/share/licenses/siakhooi-devy

%files
%license LICENSE
%{_bindir}/apt-search
%{_bindir}/get-build-version
%{_bindir}/devy-check-binaries
%{_bindir}/git-commit
%{_bindir}/git-get
%{_bindir}/git-log
%{_bindir}/git-reset
%{_bindir}/mvn-deps
%{_bindir}/mvn-with-settings

%changelog
* Sat Jan 10 2026 Siak Hooi <siakhooi@gmail.com> - 0.10.0
- update devy-check-binaries with node, npm, yarn version checks

* Sat Jan 10 2026 Siak Hooi <siakhooi@gmail.com> - 0.9.2
- touch up devy-check-binaries

* Fri Jan 9 2026 Siak Hooi <siakhooi@gmail.com> - 0.9.1
- fix devy-check-binaries

* Fri Jan 9 2026 Siak Hooi <siakhooi@gmail.com> - 0.9.0
- add version support for devy-check-binaries

* Thu Jan 8 2026 Siak Hooi <siakhooi@gmail.com> - 0.8.0
- add devy-check-binaries

* Wed Dec 31 2025 Siak Hooi <siakhooi@gmail.com> - 0.7.2
- fix mvn-deps script to ignore pre-release versions correctly

* Wed Dec 31 2025 Siak Hooi <siakhooi@gmail.com> - 0.7.1
- rename output-prefix for mvn-deps

* Sat Dec 20 2025 Siak Hooi <siakhooi@gmail.com> - 0.7.0
- add mvn-deps

* Wed Dec 17 2025 Siak Hooi <siakhooi@gmail.com> - 0.6.0
- add mvn-with-settings

* Wed Dec 17 2025 Siak Hooi <siakhooi@gmail.com> - 0.5.0
- add get-build-version

* Sat Nov 22 2025 Siak Hooi <siakhooi@gmail.com> - 0.4.0
- add git-log -l, git-commit, git-reset

* Wed Nov 19 2025 Siak Hooi <siakhooi@gmail.com> - 0.3.0
- add git-log

* Mon Nov 17 2025 Siak Hooi <siakhooi@gmail.com> - 0.2.1
- remove siakhooi-devutils

* Fri Nov 14 2025 Siak Hooi <siakhooi@gmail.com> - 0.2.0
- add apt-search

* Thu Nov 13 2025 Siak Hooi <siakhooi@gmail.com> - 0.1.0
- initial version
