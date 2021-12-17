# Práctica 3 IA Aprendizaje Automático

## Introducción
Aplicación para la predicción de ataques de corazón a partir de. El resultado de la predicción se basa en distintos campos

- Autor: José Manuel Martínez
- Lenguaje de programación: **Python 3.8.10**
- Sistema Operativo: **Ubuntu 20.04.3 LTS**

## Instalación
Para instalar los módulos requeridos ejecutar la instrucción
```
pip install -r requirements.txt
```

Los paquetes necesarios para la ejecución de la aplicación son
```
scikit-learn (version 1.0.1)
pandas (version 1.3.4)
scipy (version 1.7.3)
numpy (version 1.21.4)
joblib (version 1.1.0)
python-dateutil (version 2.7.3)
pytz (version 2019.3)
matplotlib (version 3.5.0)
graphviz (version 0.19)
```

## Ejecución
- Para **obtener el manual** se puede ejecutar la instrucción
```
./app -h
```
- Para **generar un nuevo modelo** a partir de los datos se debe ejecutar la instrucción
```
./app -c <nombre-modelo>
```
- Para **obtener la puntuación de un modelo** se debe ejecutar la instrucción
```
./app -l <nombre-modelo> -s
```
- Para **generar el grafo de un modelo** se debe ejecutar la instrucción
```
./app -l <nombre-modelo> -g
```
- Para **realizar una consulta** se debe ejecutar la instrucción
```
./app -l <nombre-modelo> -q 
```

## Datos

| Columnas            | Información                                                       | Tipo de Dato |
| ------------------- | ----------------------------------------------------------------- | ------------ |
| Age                 | Edad del paciente                                                 | INT          |
| Anemia              | Sufre el paciente anemia                                          | BOOLEAN      |
| CPK                 | Nivel de la encima CPK                                            | INT          |
| Diabetes            | Sufre el paciente diabetes                                        | BOOLEAN      |
| Ejection Fraction   | Porcentaje de sangre que sale del corazón cada vez que se contrae | INT          |
| High Blood Preasure | Sufre el paciente de Presión Arterial Alta                        | BOOLEAN      |
| Platelets           | Número de plaquetas                                               | FLOAT        |
| Creatinine          | Nivel de suero de creatinina en la sangre                         | FLOAT        |
| Sodium              | Nivel de suero de sodio en la sangre                              | INT          |
| Sex                 | Sexo del paciente                                                 | INT          |
| Smoking             | Es fumador el paciente                                            | INT          |
| Time                | Días en seguimiento por el doctor                                 | INT          |
| Death               | Evento Final                                                      | INT          |

| Age | Anemia | CPK  | Diabetes | Ejection Fraction | High Blood Preasure | Platelets    | Creatinine | Sodium | Sex | Smoking | Time | Death |
| --- | ------ | ---- | -------- | ----------------- | ------------------- | ------------ | ---------- | ------ | --- | ------- | ---- | ----- |
| 75  | 0      | 582  | 0        | 20                | 1                   | 265000       | 1.9        | 130    | 1   | 0       | 4    | 1     |
| 55  | 0      | 7881 | 0        | 38                | 0                   | 263358.03    | 1.1        | 136    | 1   | 0       | 6    | 1     |
| 65  | 0      | 146  | 0        | 20                | 0                   | 162000       | 1.3        | 129    | 1   | 1       | 7    | 1     |
| 50  | 1      | 111  | 0        | 20                | 0                   | 210000       | 1.9        | 137    | 1   | 0       | 7    | 1     |
| 65  | 1      | 160  | 1        | 20                | 0                   | 327000       | 2.7        | 116    | 0   | 0       | 8    | 1     |


## Test
Para ejecutar los test usar el comando
```
make test
```
