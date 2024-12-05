# C-22-38-T-DataBi
### Simulación Laboral de No-Country 
## No-Country - Area Data-Bi
# Shark![alt text](logo_m.webp)Fish - Análisis y Proyección de Seguridad Web para la detección de Phishing
### Objetivo: 
##Este proyecto tiene como objetivo analizar y proyecctar en el ámbito de la seguridad web, para detectar phishing.

### Industria: Ciberseguridad
## Colaboradores:
###1.- Florencia Saldico (Data Analyst) https://www.linkedin.com/in/fsaldico
###2.- Marisol Quinteros (Data Science) www.linkedin.com/in/marisol-quinterosbz-1r9
###3.- Elsa Beltrán (Machine Learning) https://www.linkedin.com/in/elsa-beltran-vivanco

## Tecnologías: 

### IDE:VSCode - Lenguaje: Python,R - Notebook:Jupyter - Library:Matplotlib,Seaborn,Scikit.Learn,Kaggle - Plataform: GitHub,Power.Bi,Jira,RStudio -  Version.Control: Git -  Chat: Slack-Discord-Whatsapp - Tool: Google.Meet , Google.Drive

## Enlaces : 
### https://github.com/No-Country-simulation/C-22-38-T-DataBi

# Etapas del Proyecto:
## Etapa 0:
### Seleccionar un confiable dataset, para este proyecto.
### Nuestras fuentes de origen fueron:
### https://data.mendeley.com/datasets/vfszbj9b36/1
### https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls/data

## Etapa 1:
### Preparación del dataset, esto implica, filtrar duplicados, columnas vacías, valores NaN..etc
### Agregar , desde nuestro análisis previo, nuevas columnas al dataset, que enriquezcan el análisis de cada Url, adjunta
### Normalizar sus valores,esto permitirá acotar, cada dato, de cada registro entre el rango [0, 1]
### Aplicar al dataset ya normalizado, la varianza a sus valores, esto nos permitirá seleccionar columnas, es decir, se eliminarán aquellas columnas cuya varianza se acerque a 0

## Etapa 2:
### Seleccionamos 3 algoritmos de automatización, para crear un modelo predictivo con Machine Learning
### Los algoritmos a probar son:
### 1.- Gradiente de Boosting
### 2.- Random Forest
### 3.- Regresión Logística
### Seleccionaremos el algoritmo, que , al ser entrenado, nos entregue el "Mejor Resultado".
### El  criterio para definir el "Mejor Resultado", implica maximizar los aciertos y disminuir los errores

## Etapa 3:
### Utilizar el modelo ya entrenado y seleccionado
