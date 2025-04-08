FROM python:3.10

LABEL maintainer="Здесь могла быть Ваша реклама"

ENV HOST="0.0.0.0"
ENV PORT=8070

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

CMD ["python", "./main.py"]