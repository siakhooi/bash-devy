help:
clean:
	rm -rf target *.deb *.sha256sum *.sha512sum *.rpm ~/rpmbuild
shellcheck:
	./scripts/shellcheck.sh
build-deb: clean shellcheck
	./scripts/build-deb.sh
build-rpm: clean shellcheck
	scripts/build-rpms.sh
set-version:
	scripts/set-version.sh
commit:
	scripts/git-commit.sh
release:
	scripts/create-release.sh
all-deb: clean set-version build-deb
all-rpm: clean set-version build-rpm

deb-install:
	apt install ./*.deb
deb-uninstall:
	apt remove siakhooi-devy
rpm-install:
	rpm -i ./*.rpm
rpm-uninstall:
	rpm -e siakhooi-devy

docker-build-rpm:
	docker run --rm -v $$(pwd):/workspace siakhooi/devcontainer:bash-rpm-0.1.0 scripts/build-rpms.sh
docker-build-deb:
	docker run --rm -v $$(pwd):/workspace siakhooi/devcontainer:bash-deb-0.1.0 scripts/build-deb.sh
all: clean set-version docker-build-deb docker-build-rpm
