FROM python:3.8-slim


WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app .

CMD [ "python3", "/usr/src/app/bot.py" ]