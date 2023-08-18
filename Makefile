.PHONY: all

all:
	python -m pip install --upgrade pip
	pip install .
	git clone https://github.com/tree-sitter/tree-sitter-python
	python build.py
	rm -rf tree-sitter-python
