venv: env/bin/activate
env/bin/activate: requirements.txt
	test -d env || virtualenv env
	env/bin/pip3 install -Ur requirements.txt
	touch env/bin/activate

freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt

test:
	pytest tests/
start: venv
	python3 ./src/app.py
