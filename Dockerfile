FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

# Modified to support both port 80 and 443 (bonus task)
ENV PORT=443
EXPOSE 80 443

CMD ["python", "counter-service.py"]