# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

# PROD
# CMD [ "waitress-serve", "--call" , "app:create_app"]

#DEV
CMD [ "python", "app.py"]
