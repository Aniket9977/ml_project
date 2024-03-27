FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r req.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PROT app:app