VENV=venv

install:
	virtualenv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt --no-deps

freeze:
	$(VENV)/bin/pip freeze > requirements.txt

resetdb:
	rm -f project/dev.db
	$(VENV)/bin/python project/manage.py syncdb --noinput

static:
	$(VENV)/bin/python project/manage.py collectstatic --noinput
