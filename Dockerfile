FROM python:3.8-slim-buster
WORKDIR /app

COPY . .

RUN  python -m pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "--config", "gunicorn.py", "app:app"]