FROM python:3.8-slim-buster
WORKDIR /app
EXPOSE 5000

COPY . .

RUN  python -m pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "--config", "gunicorn.py", "app:app"]