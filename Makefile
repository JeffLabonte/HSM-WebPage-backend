SHELL := /usr/bin/env bash

install: venv upgrade_pip
	.venv/bin/pip install -r requirements.txt

install-dev: venv upgrade_pip
	.venv/bin/pip install -r requirements.dev.txt

upgrade_pip:
	@if [ -d .venv ]; then\
		echo "[-] Upgrading pip";\
		.venv/bin/pip install --upgrade pip;\
	else\
		echo "[-] Requires .venv, please run make venv";\
	fi

venv:
	@if [ ! -d .venv ]; then\
		echo "[-] Creating venv";\
		python3 -m venv .venv;\
	else\
		echo "[-] venv already exists";\
	fi

start_dev:
	BROKER_HOST=localhost bash docker-entrypoint.sh

unit_test:
	cd src/ && py.test tests/unit/

generate_doc:
	plantuml docs/*puml && mv docs/*.png docs/generated/
