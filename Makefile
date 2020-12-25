.PHONY: deploy dev clean setup-dev lint

dev:
	FLASK_APP=app.py FLASK_ENV=development ACC_HANDLE={account_handle} flask run

setup-dev:
	pip install --upgrade -r requirements.txt -r requirements_test.txt
	cp geckodriver venv/bin

lint:
	pylint ./**/*.py ./app.py