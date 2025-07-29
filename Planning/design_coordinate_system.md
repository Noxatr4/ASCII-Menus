# Diseño del sistema de coordenadas

## Requerimientos

* El sistema de coordenadas (coord.) debe poder representar las siguientes posiciones:
  * Horizontal
  * Vertical
  * Número de página de opciones.
  * Menú activo o Menú actualmente interactuable.
* Límites dinámicos
* Al desbordar los límites debe ocurrir lo siguiente.
  * **Límites horizontales**: Se consideran circulares, es decir, al llegar a un límite e intentar seguir se continua <br>
                              en la coord. que representa el límite opuesto.

  * **Límites de páginas y verticales**: Estas tienen una "notación posicional" de dos dígitos, en donde, <br> 
                                         el LSD (Dígito menos significativo, que representa el **movimiento vertical**) <br>
                                         suma o resta, dependiendo del caso, al MSD (**movimiento por páginas**). <br>
                                         A su vez, el conjunto de coord. (Verticales y páginas) se consideran de límites circulares.

  * **Límites Menús**: Se consideran circulares.

* **Coordenadas dinámicas**: Las coordenadas cambiarán según un input establecido.
* **Límites de coordenadas**: Para que este sistema se adapte a distintos menús.
* Cuatro dimensiones de coordenadas: 
  * Coordenada **X**: Derecha/Izquierda
  * Coordenada **Y**: Arriba/Abajo
  * Coordenada **Z**: Páginas
  * Coordenada **M**: Menús
* Movimiento y teclas:
  * Coordenadas X, Y, Z por **Flechas del teclado**.
  * Coordenada M tecla aparte (**Por escoger**).


## Decisiones de diseño

### Resolución de requerimientos

* **Representación**: Se basará en cuatro números enteros, <br>
                      uno para cada una de las posiciones descritas en "Requerimientos". <br>
                      También se expresarán con los siguientes nombres de variables:
  * `X`: Movimiento **horizontal**
  * `Y`: Movimiento **Vertical**
  * `Z`: **Páginas**
  * `M`: **Menús**
* **Formato**: Tendrá un formato de lista (`[M, Z, Y, X]`)
* **Límites dinámicos**: Deben ser proporcionados como un parámetro, ocupando el formato descrito en el punto anterior. <br>
                         Al ser dinámicos, estos límites son particulares para cada manú.
* Manejo del desbordamiento de límites:
  * Circulares: Se utiliza la función módulo `%`, donde el divisor es el límite ingresado como parámetro según corresponda <br>
                Ej: Para la variable `X` sería `X % Límite de X`
  * Notación posicional: Sería parecida a los **Límnites Circulares**, solo tiene que ser una agrupación de más de una coord. <br>
                         Ej: Agarrando la idea vista en [Límites de páginas y verticales](#Requerimientos), tenemos dos coord. que se relacionan. <br>
                         El funcinamiento es parecido al sistema numérico decimal (Decimal: `[Decenas, Unidades]`, Notación posicional: `[Z, Y]`). <br>
                         Por tanto, Se tendría:
    1. `if Y supera Límite: Y += 1 o Y -= 1` dependiendo del caso.
    2. `Y % Límite de Y`.
    3. `Z % Límite de Z`.

### Segmentación
1. Convertidor de input `alfabético → numérico`.
2. Sumatoria o Resta y tratamiento de los límites de coord.
3. Generación de una lista con todas las coord. actualizadas. 


## Pre-Coding

### Esquemático

#### Formato de Input/Output

* **Input:**
  * user: `q, w, a, s, d`
  * last coord: `[M, Z, Y, X]`
  * coord. limit: `[M, Z, Y, X]`
*  **Output:**
  * new coord: `[M, Z, Y, X]`


#### Diagrama de Flujo



### Pseudo Código
