FROM python:3.7-slim-buster

# upgrade pip
RUN pip install --upgrade pip

# Install dependencies:
COPY requirements.txt .
COPY ./ .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./app.py"]

