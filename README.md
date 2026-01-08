# bash-devy

dev scripts for devcontainers/wsl

## Installation

### Deb

```
sudo curl -L https://siakhooi.github.io/apt/siakhooi-apt.list | sudo tee /etc/apt/sources.list.d/siakhooi-apt.list > /dev/null
sudo curl -L https://siakhooi.github.io/apt/siakhooi-apt.gpg  | sudo tee /usr/share/keyrings/siakhooi-apt.gpg > /dev/null
sudo apt update
sudo apt install siakhooi-devy
```

### Rpm

```
sudo curl -L https://siakhooi.github.io/rpms/siakhooi-rpms.repo | sudo tee /etc/yum.repos.d/siakhooi-rpms.repo > /dev/null
sudo yum install siakhooi-devy
```

## Binaries

- `apt-search`
- `get-build-version`
- `devy-check-binaries`
- `git-commit`
- `git-get`
- `git-log`
- `git-reset`
- `mvn-deps`
- `mvn-with-settings`

## External Third party Required

- `git`
