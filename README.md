# Laboratorio FAIR - Bioinformática

## Integrantes
* Nicol Valentina Franco Iguaran
* Santiago Bejarano
* Julian Rodriguez Ruiz

## Descripción del Repositorio
Este repositorio organiza y estructura datos bioinformáticos bajo los **Principios FAIR** (Findable, Accessible, Interoperable, Reusable), superando los problemas de desorden y falta de metadatos.

## Estructura
* `01_datos_crudos/`: Contiene el archivo FASTA oficial y limpio obtenido de NCBI para el gen *mecA* de *Staphylococcus aureus* (Accession: `PP848319.1`).
* `02_scripts/`: Contiene el script en Python implementado en Google Colab para la traducción *in silico* de la secuencia de ADN a proteína.

## Instrucciones de Uso
Para ejecutar el algoritmo de traducción, abra el archivo ubicado en `02_scripts/traduccion.py` dentro de un entorno de Python o Google Colab e ingrese la secuencia deseada en la variable `mi_secuencia`.
