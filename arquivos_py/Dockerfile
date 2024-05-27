FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install -r arquivos_py/requirements.txt

EXPOSE 5000

CMD ["python", "dbCotacao.py"]