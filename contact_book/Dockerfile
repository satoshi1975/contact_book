
FROM python:3.10.7

WORKDIR /app

COPY . /app

RUN pip install -r req.txt

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=contact_book.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
