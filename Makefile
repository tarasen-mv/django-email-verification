#!/bin/bash
ve:
	test ! -d .ve && virtualenv -p python3.8 .ve; \
	. .ve/bin/activate; \
	pip install -Ur requirements.txt

clean:
	python setup.py clean
	test -d .ve && rm -rf .ve