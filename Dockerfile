FROM python:3.11-slim

WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt psycopg2-binary

# Copia el código de la aplicación
COPY . .

# Expone el puerto
EXPOSE 5001

# Comando por defecto
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "app:app"]