# Diseño del sistema de coordenadas

## Planificación

### Requerimientos

* El sistema de coordenadas (coord.) debe poder representar las siguientes posiciones:
  * Horizontal
  * Vertical
  * Número de página de opciones.
  * Menú activo o Menú actualmente interactuable.
* Límites dinámicos
* Al llegar a los límites deben ocurrir lo siguiente.
  * **Límites horizontales**: Se consideran circulares, es decir, al llegar a un límite e intentar seguir se continua <br>
                              en la coord. que representa el límite opuesto.

  * **Límites verticales y de páginas**: Estas tienen una relación numérica de dos dígitos, en donde, <br> 
                                         el LSD (Dígito de menor valor, que representa el **movimiento vertical**) <br>
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


### Decisiones de diseño

#### Resolución de requerimientos
* **Coord. dinámicas:**
  * Coord. guardadas en una lista `[M, Z, Y, X]`.
  * Actualización realizada por el input del usuario
  * La acción específica definida por el input realizado, es decir, la tecla accionada.
* **Límites de coordenadas:**
  * Deben ser ingresados como parámetros en el mismo formato de coord. (`[M, Z, Y, X]`)
  * Estos límites también se usarán para otras características de comportamiento.

#### asd

* Representación
* Formato
* Movimiento
* Límites
