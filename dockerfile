# Usa una imagen oficial de Python como base
FROM python:3.11

# Define el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de la aplicación
COPY . .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput


# Expone el puerto en el que correrá Django
EXPOSE 8000

# Comando para ejecutar Django
CMD ["gunicorn", "-b", "0.0.0.0:8000", "proyecto.wsgi:application"]
