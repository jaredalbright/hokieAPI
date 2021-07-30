FROM python:3.8.1-slim 

ENV PYTHONUNBUFFERED 1 
EXPOSE 8000 
WORKDIR /hokieAPI
# Copy requirements from host, to docker container in /app 
COPY ./requirements.txt .
# Copy everything from ./src directory to /app in the container
COPY ./src . 
RUN pip install -r requirements.txt 
# Run the application in the port 8000
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]