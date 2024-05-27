FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install requirements.txt

EXPOSE 5000

CMD ["python", "dbCotacao.py"]