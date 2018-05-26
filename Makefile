make:
	@python3 eager.py

install:
	brew install python
	python -v
	pip3 install --upgrade tensorflow
	pip3 install --upgrade matplotlib
