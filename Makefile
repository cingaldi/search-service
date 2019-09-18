install:
	pip3 install -r requirements.txt
	python3 setup.py install

freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt

test:
	pytest tests/

start:
	python3 ./src/app.py
