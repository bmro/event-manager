FROM python:3.9 as build

WORKDIR /usr/src/app
RUN python -m venv /usr/src/app/venv
ENV PATH="/usr/src/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt



FROM python:3.9

RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python

RUN mkdir /usr/src/app && chown python:python /usr/src/app
WORKDIR /usr/src/app

COPY --chown=python:python --from=build /usr/src/app/venv ./venv
COPY --chown=python:python . .

USER 999


ENV PATH="/usr/src/app/venv/bin:$PATH"
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-k", "gevent", "--timeout", "120", "main:app"]