.PHONY: all

all:
	pipenv install
	python manage.py collectstatic --noinput
	python manage.py makemigrations
	python manage.py migrate

collect:
	python manage.py collectstatic --noinput

coverage:
	coverage run --source='.' manage.py test apps
	coverage report -m

coverage-html:
	coverage html

docker:
	docker-compose up -d --build

migrations:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver

superuser:
	python manage.py createsuperuser

test:
	python manage.py test apps