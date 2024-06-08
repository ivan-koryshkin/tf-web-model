FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libatlas-base-dev \
    gfortran \
    libhdf5-dev \
    pkg-config \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
ENV PIP_DEFAULT_TIMEOUT=1800
RUN pip install --upgrade pip \
    && pip install pipenv setuptools wheel \
    && pipenv install --deploy --ignore-pipfile -v

CMD ["pipenv", "run", "start"]
