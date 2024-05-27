FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install psycopg2
RUN pip install selenium

EXPOSE 5000

CMD ["python", "dbCotacao.py"]