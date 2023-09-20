install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:	
		black \codes/project_codes/*.py 

lint:
	ruff check \codes/project_codes/*.py 

test:
	python -m pytest -vv --cov=codes/project_codes codes/test_codes/*.py

all : install test format lint 
