MUSICTAP

Proyecto que implementa programación paralela con arquitectura SDMI

Objetivo:
Generar una serie de análisis en tiempo de real de un archivo de audio de forma paralela

Definición:
La aplicación seria un reproductor de musica que mostraria datos como duración tota, , Bfrecuencia dominantePM, energía RMS, entre otros.
La frecuencia dominante implica el suo de FFT, el RMS el promedio de cuadrados y cada parámetro un determinado calculo que según su dependencia se agruparan o no en un mismo hilo. La aplicación busca paralelizar las funciones posibles y en las que se encuentre redito. 
Ademas algunos de los parámetros serán mostrados de forma creativa en la interfaz.
