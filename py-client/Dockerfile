FROM python:3-alpine
WORKDIR /srv

COPY . .
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["python", "/srv/main.py"]