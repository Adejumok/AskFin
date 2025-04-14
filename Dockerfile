FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN test -f "/app/models/20250318-113652-tranquil-backpack.tar.gz" || (echo "No trained model found! Exiting..." && exit 1)

EXPOSE 5005

# Start Rasa server with appropriate configurations
CMD ["rasa", "run", "--endpoints", "endpoints.production.yml", "--enable-api", "--cors", "*", "--debug", "--port", "5005"]

FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5005
EXPOSE 5055

CMD rasa run --enable-api --cors "*" & rasa run actions

