FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN pip install --upgrade pip
COPY spider_project/requirements.txt /code/
COPY ./entrypoint.sh /code/
RUN pip install -r requirements.txt && \
    chmod +x /entrypoint.sh
COPY . /code/
ENTRYPOINT ["/code/entrypoint.sh"]
