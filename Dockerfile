FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN pip install --upgrade pip
COPY spider_project/requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./entrypoint.sh /code/
COPY . /code/
ENTRYPOINT ["/code/entrypoint.sh"]
