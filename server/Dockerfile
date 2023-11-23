# backend/Dockerfile
FROM python:3.8

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN pip install Flask Flask-Migrate

COPY . .

EXPOSE 4000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]
