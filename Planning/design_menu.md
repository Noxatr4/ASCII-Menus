# Diseño del sistema de coordenadas


## Requerimientos


1. Menu con opciones en formato de celdas, con contorno, con titulo y visualisado por medio de la terminal.
2. Regular tamaño en base a la cantidad de opciones que se requieran.
3. Soporte para multiples páginas.
4. Scroll-Bar que indique al usuario en que página se encuentre.
5. Con dos modos de interacción (Menú Dinámico/Estático).
6. Personalización del color de fondos y letras.
7. Bloqueo de coordenadas que representen opciones vacías.
8. Cursor que retroalimente al usuario la opción que se escogerá, solo en el menú actualmente activo y en modo variable.
9. Retorno de coordenadas y nombre de la opción de cuando seleccione.

## Decisiones de diseño

### Resolución de requerimientos

1. La estructura general será:
    * Título:
        * Fila:
            * Borde
            * Título
        * Columna:
            * Borde
            * Contenido de la fila
            * Borde
    * Cuerpo:
        * Fila:
            1. Borde
            2. Espacio
            3. Opción
            4. Se puede repetir los puntos 2 y 3 n veces
            5. Borde
        * Columna:
            * Borde:
                * Borde
                * Contenido de fila
                * Borde
            * Espacios:
                * Borde
                * Contenido de fila
                * Scroll-Bar
                * Borde
            * Opciones:
                1. Borde
                2. Cursor
                3. Opcion
                4.  Se pueden repetir puntos 2 y 3 n veces
                5. Scroll-Bar
                6. Borde
    * Se imprime en la terminal una cadena de texto siguiendo el formato que corresponda.

2. El tamaño se regulará con números enteros, definiendo el número de opciones que tendrán en las filas y columnas
3. Las páginas de cada menú se establecerán è manera automática, según el desbordamiento qie ocurra por la cantidad de opciones presentes entre las filas * columnas.
4. La Scroll-Bar estará implementada por el caracter de espacio, donde la parte activa tendrá un fondo que contraste con el fondo del terminal y la parte desactivada uno del mismo color que el del terminal.
5. El modo estático se caracteriza por tener deshabilitado el sistema de coordenadas y el cursor, por lo tanto, no se puede acceder a un menú deshabilitado para poder manejarlo.
6. Personalización basada en *ANSI Escape Code* específicamente **Extended VGA Palette**.
7. Ver más avanzado en el desarrollo como implementar esta característica
8. Establecida esa retroalimentación por un caracter distintivo para indicar la posición actual del cursor y un caracter de espacio si el cursor no se encuentra en esa pocicion.
9. El valor de las coordenadas estará suministrado por el sistema de coordenadas, el nombre de la opción se dará por el valor del mismo sistema de coordenadas.


### Segmentación

1. Generador de parámetros con inputs de entrada.
2. Constructor de la string para mostrar el menu en la terminal.
3. Sistema que genere el retorno de valores necesario.

## Pre-Coding

### Esquemático

#### Formato de Input/Output

Input:
* Estructurales:
    * Número de opciones por columna.
    * Número de opciones por fila.
    * Título o nombre del menu.
    * Menu Dinámico/Estático.
    * Activación/Desactivación.
    * Las opciones del menú.
    * Input usuario.


* Estéticos:
    * Color de letras.
    * Color de fondo.
    * Color de Scroll-Bar.


#### Diagrama de Flujo
<img src="/Planning/img/diagrama_flujo_menu.png" alt="Diagrama de Flujo Bosquejo General" width="200" height="600">



### Pseudo Código

#### Generador de parámetros con inputs de entrada

* Generar el número de páginas
* Indice maximo
* Generar las constantes de caracteres
* Generar número de caracteres de columnas

#### Constructor de la string para mostrar el menu en la terminal

**Bucle para crear filas**
``` 
for i = 0; i <= 5; i++:
    if i == 0 or i == 3 or i == 5:
        Hacer FilaBorde
    elif i == 2:
        Hacer FilaTitulo
    else:
        Hacer FilaOpciones
```

**Hacer FilaBorde**
``` 
BordeColumna + (Caracter Cuerpo BordeColumna * Número de caracteres de columna) + BordeColumna
```

**Hacer FilaOpciones**
```
for i == 0; i < Número de fila; i++:
    BordeColumna + Caracter Cuerpo EspacioColumna * (Número de caracteres de columna - 1) + Scroll-Bar + BordeColumna

    for i == 0; i < Número Opciones por columna; i++
        columna_opciones = cursor + opcion
    
    BordeColumna + columna_opciones + ScrollBar + BordeColumna
    
```

**Hacer FilaTitulo**

``` 
BordeColumna + Titulo.centrado + BordeColumna
```
