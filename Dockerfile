FROM python:3.9-slim-buster
 
WORKDIR /app

COPY Requirements.txt .

RUN pip install --no-cache-dir -r Requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0 

EXPOSE 5000

CMD ["flask", "run"] 

