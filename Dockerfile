FROM python:3.10-slim

# Install required system packages
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    ffmpeg \
    bash \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -U pip wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 5000

CMD flask run -h 0.0.0.0 -p 5000 & python3 main.py
