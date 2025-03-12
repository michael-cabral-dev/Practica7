# Usa Python 3.9 como imagen base
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto a la imagen
COPY src /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que corre la app Flask
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
