build:
	docker build -t image_recognition_python .

run: build
	docker run -it --rm --name app image_recognition_python

update_requirements:
	pip freeze > requirements.txt
