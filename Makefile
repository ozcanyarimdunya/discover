migration:
	python3 manage.py makemigrations && python3 manage.py migrate

user:
	python3 manage.py createsuperuser

runserver:
	python3 manage.py runserver 0.0.0.0:8000

doc:
	docker-compose up --build

docd:
	docker-compose up --build -d

