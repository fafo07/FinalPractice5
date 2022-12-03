FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY Backend/requirements.txt /code/
RUN python -m pip install -r requirements.txt
COPY . /code/
 
