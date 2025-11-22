Name:           siakhooi-devy
Version:        0.4.0
Release:        1%{?dist}
Summary:        dev scripts for devcontainers/wsl

License:        MIT
URL:            https://github.com/siakhooi/bash-devy
Source0:        https://github.com/siakhooi/%{name}/archive/refs/tags/${version}.tar.gz
BuildArch:      noarch

Requires:       bash

%description
dev scripts for devcontainers/wsl

%install
%{__mkdir}   -v -p %{buildroot}%{_bindir}
%{__mkdir}   -v -p %{buildroot}/usr/share/licenses/siakhooi-devy
%{__install} -v -m 0755 %{_topdir}/BUILD/usr/bin/* %{buildroot}%{_bindir}
%{__install} -v -m 644  %{_topdir}/BUILD/LICENSE %{buildroot}/usr/share/licenses/siakhooi-devy

%files
%license LICENSE
%{_bindir}/git-commit
%{_bindir}/git-get
%{_bindir}/git-log
%{_bindir}/apt-search

%changelog
* Sat Nov 22 2025 Siak Hooi <siakhooi@gmail.com> - 0.4.0
- add git-log -l, git-commit

* Wed Nov 19 2025 Siak Hooi <siakhooi@gmail.com> - 0.3.0
- add git-log

* Mon Nov 17 2025 Siak Hooi <siakhooi@gmail.com> - 0.2.1
- remove siakhooi-devutils

* Fri Nov 14 2025 Siak Hooi <siakhooi@gmail.com> - 0.2.0
- add apt-search

* Thu Nov 13 2025 Siak Hooi <siakhooi@gmail.com> - 0.1.0
- initial version
