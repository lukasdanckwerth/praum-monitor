#!/bin/bash
set -u
set -e

if [ -z "${SUDO_USER:-}" ]; then
  echo "This script must be run from sudo"
  exit 1
fi

I_SMB_USER="pi"
I_SMB_PASS="pi"
I_PROJECT_DIR="/srv/praum-monitor"

sudo apt-get update --assume-yes
sudo apt-get upgrade --assume-yes
sudo apt-get install --assume-yes \
  vim \
  git \
  python-dev \
  samba samba-common-bin \
  unclutter

(
  echo "${I_SMB_PASS}"
  echo "${I_SMB_PASS}"
) | sudo smbpasswd -s -a "${I_SMB_USER}"

sudo chmod 777 /srv

sudo rm -rf /etc/samba/smb.conf
sudo tee -a /etc/samba/smb.conf <<EOF
[global]
  workgroup = WORKGROUP
  security = user
  encrypt passwords = yes
  usershare allow guests = no
  guest account = nobody
  map to guest = bad user

[srv]
  path = /srv/
  read only = false
  public = true
  writable = true
  guest ok = false
  browsable = true
EOF

if [[ ! -d "/srv/py-spidev-master" ]]; then
  pushd /srv/ || exit
  wget https://github.com/doceme/py-spidev/archive/master.zip -O py-spidev.zip
  unzip py-spidev.zip
  pushd py-spidev-master || exit
  sudo python3 setup.py install
  popd || exit
  popd || exit
fi

if [[ -f /srv/py-spidev.zip ]]; then
  echo "remove /srv/py-spidev.zip"
  rm -rf /srv/py-spidev.zip
fi

if [[ ! -d "${I_PROJECT_DIR}" ]]; then
  sudo mkdir /srv/praum-monitor
fi

#sudo chown pi:pi /srv/praum-monitor

echo "Installing yarn..."
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update --assume-yes
sudo apt install yarn --assume-yes
