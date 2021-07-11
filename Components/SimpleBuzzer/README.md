# Simple Buzzer

Componente que hace sonar un Buzzer

## Configuración

```yaml
pin: 18 #GPIO 24
initialState: LOOP #BEEP|STOP|LOOP
sequence: s1,z1    # s3 suena 3 segundos, z1 esta en silencio 1 segundo
topics:
  input: buzzer/input
``` 

Ejemplo de ejecución en _standalone_

```bash
python3 SimpleBuzzer.py --config SimpleBuzzer.yaml  --run
```

## Interfaz MQTT

Para controlar el componente hemos de escribir los siguientes
comandos en el topic `topics.input` 

|Comando | Descripción |
|---|---|
| PLAY  | Hace sonar la secuencia |
| STOP | Para la secuencia |
| LOOP | Hace sonar la secuencia en bucle |


## Casos de uso

+ Encender/Apagar un led,ventilador etc.