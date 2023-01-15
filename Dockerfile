FROM python:3.9.16-alpine3.16

WORKDIR /home/app

COPY . /home/app/

RUN apk update
RUN apk add py-pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]