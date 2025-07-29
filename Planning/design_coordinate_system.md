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
    1. `if Y supera Límite: Z += 1 o Z -= 1` dependiendo del caso.
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
<img src="/Planning/img/diagrama_coordinate_system.png" alt="Diagrama de Flujo Sistema de coord." width="720" height="750">



### Pseudo Código

Nombre de variables
```
input_user: Entrada de usuario
last_coord: Coordenadas anteriores, [M, Z, Y, X]
limit_coord: Limite de las coordenadas, [LtM, LtZ, LtY, LtX]
new_coord: Salida de las coordenadas, [NwM, NwZ, NwY, NwX]

coord_add: El valor de coord. que se sumará a after_coord, (AdM, AdZ, AdY, AdX)
```

Comprobación de entrada válida y proceso de generar un valor a sumar con `last_coord` 
```
if input_user == Q
    coord_add = (1, 0, 0, 0)
elif input_user == W
    coord_add = (0, 0, 1, 0)
elif input_user == S
    coord_add = (0, 0, -1, 0)
elif input_user == A
    coord_add = (0, 0, 0, -1)
elif input_user == D
    coord_add = (0, 0, 0, 1)
else 
    coord_add = last_coord
```

Suma
```
for i; len(last_coord)
    new_coord[i] = last_coord[i] + coord_add[i]
```

Forzar que la salida de coord. siempre este dentro de los límites presentes en `limit_coord`
```
NwM = M % LtM 
NwX = X % LtX
    
If Y < 0 or Y >= LtY
    NwZ += AdY
NwY = Y % LtY 
NwZ = Z % LtZ
```

Salida <br>
`new_coord`