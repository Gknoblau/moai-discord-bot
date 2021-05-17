FROM python:3.8-alpine


RUN apk --no-cache add gcc musl-dev
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app .

CMD [ "python3", "/usr/src/app/bot.py" ]