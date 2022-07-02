.PHONY: help docker docker-test cli uninstall-cli install-local

help:
	@echo "Utilities to be able to develop and use PyLangoo locally."
	@echo
	@echo "   $$ make docker"
	@echo "   $$ make docker-test"
	@echo "   $$ make cli"

install-local:
	@echo "Installing full environment locally into YOUR virtualenv"
	pip install -e .[all]
	pip install -r reqs/requirements.txt

lint:
	black tests -t py310 ./clients ./plat ./tests
	isort --settings-path=./.isort.cfg ./clients ./plat ./tests
	flake8 ./clients ./plat ./tests
