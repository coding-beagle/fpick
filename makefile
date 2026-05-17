.PHONY: help clean clean-venv clean-build clean-cache venv build install install-dev test
.DEFAULT_GOAL := help

# --- OS detection ---
ifeq ($(OS),Windows_NT)
    VENV_BIN := .venv/Scripts
    EXE      := .exe
    RM       := rm -rf
else
    VENV_BIN := .venv/bin
    EXE      :=
    RM       := rm -rf
endif

PY  := $(VENV_BIN)/python
PIP := $(PY) -m pip

help: ## Show this help message
	@awk 'BEGIN {FS = ":.*?## "}; /^[a-zA-Z_-]+:.*?##/ { printf "\033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

clean: clean-venv clean-build clean-cache ## Clean everything

clean-venv: ## Remove virtual environment
	$(RM) .venv

clean-build: ## Remove build artifacts
	$(RM) build dist *.egg-info

clean-cache: ## Remove caches
	$(PY) -c "import pathlib, shutil; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').rglob('__pycache__')]; [p.unlink() for p in pathlib.Path('.').rglob('*.pyc')]"

venv: ## Create a virtual environment
	python -m venv .venv
	$(PIP) install --upgrade pip

build: ## Build wheel + standalone executable
	$(PY) -m build
	$(PY) -m PyInstaller --onefile fpick/__main__.py
	$(PY) -c "import sys, shutil, subprocess; name = subprocess.check_output([sys.executable, 'setup.py', '--name']).decode().strip(); shutil.move(f'dist/__main__$(EXE)', f'dist/{name}$(EXE)')"

install: ## Install the module
	$(PIP) install -e .

install-dev: ## Install the module + dev tools
	$(PIP) install -e .[dev]

test: ## Run pytest tests
	$(PY) -m pytest Tests/ -v