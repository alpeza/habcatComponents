# Simple Write

Componente que escribe en 1 o 0 en un pin.

## Configuración

```yaml
pin: 7                 # Pin al que se bindea
initialState: False    # Estado inicial del pin
topics:
  input: led1/input    # Topic en el que se escribe el nuevo estado del pin
  output: led1/output  # Topic en el que se informa el cambio de estado
``` 

Ejemplo de ejecución en _standalone_

```bash
python3 SimpleWrite.py --config SimpleWrite.yaml  --run
```

## Interfaz MQTT

Para controlar el componente hemos de escribir los siguientes
comandos en el topic `topics.input` 

|Comando | Descripción |
|---|---|
| ON  | Escribe el pin a 1 |
| OFF | Escribe el pin a 0 |
| SWITCH | Realiza un switch del estado del dispositivo |
| STATE | Informa por el topic `topics.output` del estado actual del componente con `True` si está encendido o `False` si está apagado |


## Casos de uso

+ Encender/Apagar un led,ventilador etc.