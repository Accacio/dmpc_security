
env:
	python3 -m venv env

tests:
	python3 -m pytest -s

install_editable:
	@echo === Installing in editable mode ===
	@python3 -m pip install -e ./
	@echo === Installed  in editable mode ===

install:
	@echo === Installing ===
	@python3 -m pip install ./
	@echo === Installed  ===

uninstall:
	@echo === Removing ===
	@python3 -m pip uninstall dmpc_security
	@echo === Removed  ===

.PHONY: tests
