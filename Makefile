BLUE=\033[0;34m
RESET_COLOR=\033[0m

install:
	@echo "$(BLUE)--> Installing requirements$(RESET_COLOR)"
	pip install -r requirements.txt
	@echo ""

install-dev:
	@echo "$(BLUE)--> Installing requirements$(RESET_COLOR)"
	pip install -r requirements-dev.txt
	@echo ""

lint:
	@echo "$(BLUE)--> Running flake8$(RESET_COLOR)"
	flake8 .
	@echo ""
	@echo "$(BLUE)--> Running isort$(RESET_COLOR)"
	isort -c
	@echo ""

safety:
	@echo "$(BLUE)--> Running safety$(RESET_COLOR)"
	safety check
	@echo ""

test:
	@echo "$(BLUE)--> Running tests$(RESET_COLOR)"
	coverage run manage.py test
	coverage report --fail-under 90
	@echo ""

clean:
	@echo "$(BLUE)--> Removing .pyc and __pycache__$(RESET_COLOR)"
	find . | grep -E "__pycache__|.pyc$$" | xargs rm -rf
	@echo ""
	@echo "$(BLUE)--> Removing coverage data$(RESET_COLOR)"
	rm -rf .coverage .cache cover

.PHONY: test
