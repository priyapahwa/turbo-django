PYTHON_EXE?=python3
MANAGE=bin/python manage.py
ACTIVATE?=. bin/activate;
GET_SECRET_KEY=`base64 /dev/urandom | head -c50`
ENV_FILE=.env

PORT = 8000

virtualenv:
	@echo "-> Getting Essential Build Files"
	@sudo apt-get install python3-venv
	@echo "-> Making Virtual Environment"
	@${PYTHON_EXE} -m venv .

genkey: virtualenv
	@echo "-> Generating Secret key"
	@if test -f ${ENV_FILE}; then echo ".env file exists already"; true; fi
	@mkdir -p $(shell dirname ${ENV_FILE}) && touch ${ENV_FILE}
	@echo SECRET_KEY=\"${GET_SECRET_KEY}\"\\nDEVELOPMENT=True > ${ENV_FILE}

install: genkey
	@echo "-> Installing Dependencies"
	@${ACTIVATE} pip install -r requirements.txt

migrate:
	@echo "-> Apply database migrations"
	${MANAGE} makemigrations 
	${MANAGE} migrate

run:
	${MANAGE} runserver ${PORT}

format:
	@echo "-> Run isort imports ordering validation"
	@${ACTIVATE} isort chat_server chat
	@echo "-> Run black validation"
	@${ACTIVATE} black chat_server chat

test:
	@${MANAGE} test