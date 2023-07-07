
env:
	python3 -m venv env

tests:
	python3 -m pytest -s

install_editable:
	@echo === Installing ===
	@python3 -m pip install -e ./
	@echo === Installed  ===

.PHONY: tests
