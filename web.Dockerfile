FROM python:3.9.16-slim

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1


# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev python3-dev make watchman

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --dev

# Add /.venv to PATH
ENV PATH="/.venv/bin:$PATH"

# Install application into container
COPY . /usr/src/app

# set work directory
WORKDIR /usr/src/app

RUN python manage.py collectstatic --no-input;
