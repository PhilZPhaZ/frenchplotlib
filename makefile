.PHONY: help install install-dev build clean test upload lint

help:
	@echo "Commandes disponibles:"
	@echo "  make install       - Installer le package"
	@echo "  make install-dev   - Installer le package en mode développement"
	@echo "  make build         - Builder le package (wheel + sdist)"
	@echo "  make clean         - Supprimer les fichiers de build et cache"
	@echo "  make test          - Lancer les tests"
	@echo "  make upload        - Upload sur PyPI"
	@echo "  make lint          - Lancer les vérifications de style"

install:
	pip install .

install-dev:
	pip install -e .

uninstall:
	pip uninstall frenchplotlib

build: clean
	python3 -m build

clean:
	rm -rf build/ dist/ *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

upload: build
	python3 -m twine upload dist/*
