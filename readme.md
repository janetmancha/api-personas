

- Ejecutar programa: python3 main.py

- Visualizar listado de personas: curl localhost:5000/personas

- Buscar una persona en concreto, en este caso buscar a persona janet: curl localhost:5000/personas/janet

- Insertar nueva persona: curl -d '{"nombre": "janet", "edad": 40}' -H "content-type: application/json" localhost:5000/nueva-persona

- Ejecutar test: python3 -m unittest -v

- Construir imagen docker: docker build -t janetmancha/api-personas

- Ejecutar imagen: docker run -p 5000:5000 janetmancha/api-personas