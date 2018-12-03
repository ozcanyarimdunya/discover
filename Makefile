migration:
	python3 manage.py makemigrations && python manage.py migrate

runserver:
	python3 manage.py runserver 0.0.0.0:8000

doc:
	docker-compose up --build

docd:
	docker-compose up --build -d

