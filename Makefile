build:
	make reset-db
	make collect-static
	python manage.py tailwind install

reset-db:
	python manage.py reset_schema --noinput
	python manage.py makemigrations
	python manage.py migrate
#
collect-static:
	python manage.py collectstatic --noinput

run:
	concurrently --kill-others --raw "python manage.py runserver_plus 0.0.0.0:8000" "python manage.py tailwind start"

make-migrations:
	python manage.py makemigrations

remove-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

generate-secret-key:
	python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

#translations:
#	 python manage.py makemessages -a

create-app:
	docker-compose -f docker-compose.yml run --rm web bash -c "cd apps && django-admin startapp $(app)"
