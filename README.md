# Búsquedas - Ramificación y Acotación con Subestimación

Realización de la primera práctica de la asignatura ***Fundamentos de los Sistemas Inteligentes***.

El objetivo principal de la primera práctica es modificar el código base añadiendo el método de búsqueda de ***Ramificación y Acotación con Subestimación*** , usando como problema el grafo de las ciudades de Rumanía (implementado en el fichero *search.py*). 
Como heurística se usará la distancia en línea recta entre cada estado y el estado final.

A continuación se comenta brevemente que modificaciones se han realizado en cada uno de los ficheros:

  1. ***run.py***: Fichero principal en el que se encuentra el código necesario para la ejecución de la práctica. En él se hace uso de los métodos implementados en los otros ficheros. Concretamente, se hace el cáculo de todas las rutas posibles para 5 ciudades iniciales y 5 ciudades finales distintas.
  Por último, a partir de las rutas resultantes para estos 5 ejemplos, se muestra la mejor ruta obtenida por el método simple de Ramificación y Acotación, y la mejor ruta obtenida por el método de Ramificación y Acotación con Subestimación (método implementado en esta práctica),
  de tal manera que se pueda comparar el resultado de ambas.
  
  2. ***search.py***: En este fichero se modificó principalmente el método *graph_search()*, el cual se encarga de llevar a cabo la búsqueda con el método seleccionado en la ejecución. Además, para que el método de búsqueda de Ramificación y Acotación con Subestimación pueda
  ser usado en la búsqueda del grafo, también se ha implementado el método *branch_and_bound_understimation_graph_search()*, el cual se encargará de llevar a cabo la búsqueda en el grafo haciendo uso de la lista *lower_path_cost_heuristic()* implementada en el último fichero
  y la cual permite realizar la búsqueda con Ramificación y Acotación con subestimación.
  
  3. ***utils.py***: En este último fichero se encuentra como principal modificación la adición del método *lower_path_cost_heuristic()*, el cual implementa una lista y unos métodos que la modifican de tal manera que se haga uso de las heurísticas del problema y, de esta manera,
  llevar a cabo la búsqueda con el método de Ramificación y Acotación con Subestimación.
