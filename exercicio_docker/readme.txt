
# Proyecto FastAPI de Ordenación de Lista

Este es un proyecto simple usando FastAPI, que contiene dos endpoints:

- **`/lista-ordenada/`**: Recibe una lista desordenada de valores y devuelve la lista ordenada junto con la hora actual del sistema.
- **`/healthcheck`**: Endpoint de verificación de estado para confirmar que el servicio está en funcionamiento.

## Endpoints

### 1. `/lista-ordenada/`

- **Descripción**: Recibe una lista de valores desordenada en formato de cadena de texto y devuelve la lista ordenada.
- **Método**: `GET`
- **Parámetro**:
  - `lista_no_ordenada` (cadena): Una lista de valores desordenada representada como una cadena de texto.
- **Retorno**: Un JSON que contiene:
  - `hora_sistema`: La hora actual del sistema en formato `DD/MM/YYYY HH:MM:SS`.
  - `lista_ordenada`: La lista ordenada de los valores proporcionados.

- **Ejemplo de uso**:
  ```bash
  curl -X 'GET' 'http://localhost:8000/lista-ordenada/?lista_no_ordenada=[5, 3, 2, 4]'
  ```

- **Ejemplo de respuesta**:
  ```json
  {
    "hora_sistema": "07/11/2024 10:20:30",
    "lista_ordenada": [2, 3, 4, 5]
  }
  ```

### 2. `/healthcheck`

- **Descripción**: Verifica si el servicio está activo y en funcionamiento.
- **Método**: `GET`
- **Retorno**: Una cadena de texto simple `"Ok"`.

- **Ejemplo de uso**:
  ```bash
  curl -X 'GET' 'http://localhost:8000/healthcheck'
  ```

- **Ejemplo de respuesta**:
  ```json
  "Ok"
  ```

## Instrucciones para Ejecutar el Proyecto con Docker

1. **Crear la Imagen Docker**:
   En el terminal, ejecute el comando para crear la imagen Docker:
   ```bash
   docker build -t fastapi-lista-ordenada .
   ```

2. **Ejecutar el Contenedor**:
   Inicie el contenedor, mapeando el puerto 8000:
   ```bash
   docker run -p 8000:8000 fastapi-lista-ordenada
   ```

3. **Acceder a la API**:
   Acceda a los endpoints de la API en `http://localhost:8000`.

## Dependencias

- **FastAPI**: Framework para la construcción de APIs rápidas y eficientes.
- **Uvicorn**: Servidor ASGI para ejecutar FastAPI.

Para instalar las dependencias localmente (sin Docker), use:
```bash
pip install -r requirements.txt
```

## Observaciones

- Asegúrese de que la cadena pasada a `lista_no_ordenada` esté correctamente formateada como una lista en formato de cadena, por ejemplo, `"[1, 2, 3]"`.
- Este proyecto usa `ast.literal_eval` para evaluar la cadena recibida como lista, por lo tanto, **no ingrese** valores inseguros, ya que esto podría causar problemas de seguridad.

