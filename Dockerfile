FROM python:3.11.8

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /usr/src/app/requirements.txt

COPY . /usr/src/app/

CMD [ "uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8501", "--reload" ]