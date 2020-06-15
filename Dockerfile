# Pull base image
FROM python:3.7
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /project
# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /project/
RUN pipenv install --system
# Copy project
COPY . /project/