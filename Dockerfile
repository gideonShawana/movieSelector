# Dockerfile, Image, Container

FROM python:3.11.5

ADD main.py .

RUN pip install requests beautifulSoup4

CMD ["python", "./main.py"]
