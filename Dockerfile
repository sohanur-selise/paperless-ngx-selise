FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libzbar-dev imagemagick
# Install dependencies
RUN apt-get install -y --no-install-recommends \
        gcc \
        git \
        gnupg \
        libffi-dev \
        libjpeg-dev \
        libmagic1 \
        libpq-dev \
        libtesseract-dev \
        poppler-utils \
        postgresql-client \
        tesseract-ocr \
        tesseract-ocr-eng \
        tesseract-ocr-script-latn \
        zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*


# Install pipenv
RUN pip install --no-cache-dir pipenv

# Set working directory
WORKDIR /app

# Copy Pipfile and Pipfile.lock
COPY Pipfile .
COPY Pipfile.lock .

# Install dependencies with pipenv
RUN pipenv install --system --deploy --ignore-pipfile --verbose


# Copy the application code
COPY src .

RUN mkdir /consume

COPY static .

# Run migrations and collect static files
RUN python manage.py migrate && \
    python manage.py collectstatic --noinput

# Expose port 8000 for the web server
EXPOSE 8000

# Run the web server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
