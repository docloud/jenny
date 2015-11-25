#
# Copyright 2015 jenny
#

help:
	@echo "develop      Init project environment"
	@echo "test         Run test cases."

develop:
	@pip install -e .

test:
	py.test -s -v tests/
