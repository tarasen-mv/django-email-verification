#!/bin/bash
ve:
	test ! -d .ve && virtualenv -p python3.8 .ve; \
	. .ve/bin/activate; \
	pip install -r requirements.txt

clean:
	test -d .ve && rm -rf .ve