<<<<<<< HEAD
# Dockerfile placeholder
=======
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8000
CMD ["uvicorn", "backend.fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> b7842c8451143b9d8a9e23566b76e83ac52c2c40
