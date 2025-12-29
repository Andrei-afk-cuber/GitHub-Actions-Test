FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY docker_configure.py ./develop_configure.py
COPY app.py .

CMD ["python", "app.py"]