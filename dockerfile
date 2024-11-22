# Start with your base image
FROM  python:3.12.3-slim


WORKDIR /app

# clone repo
RUN apt-get install git
RUN git clone https://github.com/ocueye2/my-website.git

RUN pip install cherrypy

# Make port 8080 available to the world outside this container
EXPOSE 8080

WORKDIR /app/my-website
# Run app.py when the container launches
CMD ["python", "app.py"]
