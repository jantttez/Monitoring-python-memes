#че? мне похуй
FROM python:3.10-slim-buster

WORKDIR /monitoring

COPY . /monitoring/

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["sh", "start_web.sh"]