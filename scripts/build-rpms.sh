#!/bin/bash
set -e

rm -rf ~/rpmbuild
rpmdev-setuptree

readonly source_home=src
readonly build_home=~/rpmbuild/BUILD

# Spec File
cp $source_home/RPMS/siakhooi-devy.spec ~/rpmbuild/SPECS

# Binary File
readonly build_bin_home=$build_home/usr/bin
mkdir -p "$build_bin_home"

find $source_home/bin -type f -exec cp -vr {} "$build_bin_home" \;
chmod 755 "$build_bin_home"/*

# License
cp -vf ./LICENSE "$build_home"

# build rpm file
rpmlint ~/rpmbuild/SPECS/siakhooi-devy.spec
rpmbuild -bb -vv ~/rpmbuild/SPECS/siakhooi-devy.spec
cp -vf ~/rpmbuild/RPMS/noarch/siakhooi-devy-*.rpm .

# query
tree ~/rpmbuild/
rpm -ql ~/rpmbuild/RPMS/noarch/siakhooi-devy-*.rpm

rpm_file=$(basename "$(ls ./siakhooi-devy-*.rpm)")

sha256sum "$rpm_file" >"$rpm_file.sha256sum"
sha512sum "$rpm_file" >"$rpm_file.sha512sum"
