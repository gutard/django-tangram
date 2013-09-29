VENV=venv

install:
	virtualenv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt --no-deps

freeze:
	$(VENV)/bin/pip freeze > requirements.txt
