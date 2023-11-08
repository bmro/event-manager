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

RUN chmod +x /usr/src/app/entrypoint.sh

EXPOSE 5000

USER 999
ENV PATH="/usr/src/app/venv/bin:$PATH"
ENV FLASK_APP="main.py"

HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl -f http://localhost:5000/health || exit 1

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-k", "gevent", "--timeout", "120", "main:app"]