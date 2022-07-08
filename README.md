# OpenV2X Device Management - APIServer

[![pep8](https://github.com/open-v2x/dandelion/actions/workflows/tox-pep8.yml/badge.svg?event=push)](https://github.com/open-v2x/dandelion/actions/workflows/tox-pep8.yml)
[![ci](https://github.com/open-v2x/dandelion/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/open-v2x/dandelion/actions/workflows/ci.yml)
[![issue](https://img.shields.io/github/issues/open-v2x/dandelion)](https://github.com/open-v2x/dandelion/issues)
[![star](https://img.shields.io/github/stars/open-v2x/dandelion)](#)
[![license](https://img.shields.io/github/license/open-v2x/dandelion)](LICENSE)

## Description

TODO

## Features

TODO

## Installation

```bash
make install
```

## Configuration

**Sample:** [dandelion.conf.sample](./etc/dandelion/dandelion.conf.sample)

```bash
cp etc/dandelion/dandelion.conf.example etc/dandelion/dandelion.conf
```

Generally, you should change the following values:

[DEFAULT]
- debug
- log_file
- log_dir

[cors]
- origins

[database]
- connection

[mqtt]
- host
- port
- username
- password

[redis]
- connection

[token]
- expire_seconds

```bash
mkdir -p /etc/dandelion
DANDELION_PATH=`pwd`
cd /etc/dandelion
ln -s ${DANDELION_PATH}/etc/dandelion/dandelion.conf dandelion.conf
```

## Build && Run

Build docker image.

```bash
make build
```

Run as container.

```bash
mkdir -p /var/log/dandelion
docker run -d --name dandelion_bootstrap -e KOLLA_BOOTSTRAP="" -v /etc/dandelion/dandelion.conf:/etc/dandelion/dandelion.conf --net=host dandelion:latest
docker rm dandelion_bootstrap
docker run -d --name dandelion --restart=always -v /etc/dandelion/dandelion.conf:/etc/dandelion/dandelion.conf -v /var/log/dandelion:/var/log/dandelion --net=host dandelion:latest
```

## Local Development

### Run server

At last, you can run the server.

```bash
make server
```

You can visit the OpenAPI document at `http://127.0.0.1:28300/docs`

### Genereate the latest swagger file

```bash
make swagger
```

### Generate the latest sample config file

```bash
make config
```

## Code Format && Style

```bash
make fmt
make lint
```