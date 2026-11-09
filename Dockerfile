# 1. Usamos una versión ligera oficial de Python
FROM python:3.10-slim

# 2. Creamos y nos movemos a la carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos la lista de librerías e instalamos todo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiamos el código de nuestra API dentro del contenedor
COPY main.py .

# 5. Exponemos el puerto 8000 (la puerta por donde entrarán las peticiones)
EXPOSE 8000

# 6. Comando final para encender el servidor al arrancar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
