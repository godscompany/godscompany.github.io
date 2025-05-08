.PHONY: all setup generate build clean

PYTHON=python3
VENV=venv-hugo

all: build

setup:
	@echo "🔧 Creating virtual environment..."
	@test -d $(VENV) || $(PYTHON) -m venv $(VENV)
	@. $(VENV)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

generate:
	@echo "🛠️  Generating pages from CSV..."
	@. $(VENV)/bin/activate && $(PYTHON) scripts/generate_pages_csv_gat.py

build:
	@$(MAKE) setup
	@$(MAKE) generate
	@echo "🏗️  Building Hugo site..."
	@hugo

clean:
	@echo "🧹 Cleaning up..."
	@rm -rf $(VENV) public

