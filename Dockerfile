FROM python:3.9.0

WORKDIR /home/

RUN echo "testing223355"

RUN git clone https://github.com/a5677a/humanandbook2.git

WORKDIR /home/humanandbook2/

RUN echo "testing225544"

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=humanandbook.settings.deploy && python manage.py migrate --settings=humanandbook.settings.deploy && gunicorn humanandbook.wsgi --env DJANGO_SETTINGS_MODULE=humanandbook.settings.deploy --bind 0.0.0.0:8000"]