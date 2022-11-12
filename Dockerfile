FROM python:3.10

ENV PYTHONUNBUFFERED 1


RUN apt-get update && apt-get -y install libpq-dev gcc


RUN pip install pipenv

WORKDIR /app


COPY Pipfile .

COPY Pipfile.lock .

#RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --skip-lock

RUN mkdir /app/.venv

ADD . /app


RUN pipenv install --system --deploy --skip-lock




#RUN python admissiontool/manage.py migrate --settings=admissiontool.settings.production

#RUN pipenv install
