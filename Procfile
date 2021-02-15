release: py manage.py makemigrations --no-input
release: py manage.py migrate --no-input

web: gunicorn contatinhosapi.wsgi
