FROM python:3.8
COPY . /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ['python', 'app.py']