FROM python:3.10-slim

# Do not generate .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Make output unbuffered
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies (useful for some Python packages)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies if requirements file exists
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip setuptools wheel \
    && if [ -s /app/requirements.txt ]; then pip install -r /app/requirements.txt; fi

# Copy project files
COPY . /app

# Default command: run tests. Override at runtime if you want to run the app instead.
CMD ["pytest", "-q"]
