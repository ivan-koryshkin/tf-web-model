FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    pkg-config \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libatlas-base-dev \
    gfortran \
    libhdf5-dev \
    libhdf5-serial-dev \
    libhdf5-103 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
RUN pip install pipenv
RUN pipenv install -v
CMD ["pipenv", "run", "dev"]
