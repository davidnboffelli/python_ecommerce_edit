# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt ./

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# RUN  pip3 -r install requirements.txt
COPY . /app

# Run app.py when the container launches
# CMD ["python", "run.py"]

# Realizar las migraciones
# RUN python ./webapp/databaseConfig.py

# Exponer el puerto en el que el servidor de Django se ejecutará
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "app.py", "runserver", "0.0.0.0:5007"]