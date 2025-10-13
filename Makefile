PROJECT_NAME=st-taylor

deploy:
	rsync -avz --delete --exclude venv --exclude .venv --exclude .git --exclude '..?*' --exclude .idea ../${PROJECT_NAME} klab:

image:
	sudo docker build -t ${PROJECT_NAME} .

run:
	sudo docker run -d -p 8501:8501 ${PROJECT_NAME}

