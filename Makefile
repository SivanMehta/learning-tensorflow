make: install
	@echo see the readme, silly

.PHONY: install
install:
	pip3 install -r ./requirements.txt

.PHONY: eager-intro
eager-intro:
	@python3 eager-intro.py

tweets.csv:
	@python3 download-tweets.py