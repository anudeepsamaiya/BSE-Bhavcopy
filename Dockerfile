FROM python:3.6.8

MAINTAINER anudeepsamaiya@gmail.com

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy project
ADD ./ /project

# Set work directory
WORKDIR /project

# Install dependencies
RUN pip install --upgrade pip && pip install pipenv \
    && pipenv install --system --deploy --dev
