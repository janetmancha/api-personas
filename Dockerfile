#incluyo una imagen base en ese caso con linux y python 3.8.7
FROM python:3.8.7

#añado en la imagen docker que estoy creando el directorio actual(25-proyectoAPIPersona) en una caperta llamada app
ADD . /app

#establece el directorio de trabajo para cualquier instrucción RUN, CMD ..
WORKDIR /app

#instalo las dependencias que necesito para ejecutar el programa de python
RUN pip install -r requirements.txt

#puerto por defecto para el contenedor
EXPOSE 5000

#comandos que se van a ejecutar, accion del contenedor al crearse, su finalidad.
CMD ["python", "main.py"]
