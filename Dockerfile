FROM python:3-alpine

WORKDIR /web
COPY . .
RUN pip install fastapi uvicorn

EXPOSE 8000
CMD ["python", "main.py"]
