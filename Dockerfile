FROM python:3.9

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 5000

CMD ["python", "./src/run.py"]