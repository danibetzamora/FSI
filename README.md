# Redes Neuronales - IA Clasificadora

Proyecto realizado para la asignatura ***Fundamentos de los Sistemas Inteligentes*** en el que se pretende llevar a cabo la clasificación de imágenes pertenecientes a diferentes clases de un dataset. 

El dataset en cuestión está compuesto por 5 clases distintas de felinos, pudiendo distinguir entre: Caracal, Leopardo, Ocelote, León y Tigre. En este conjunto de datos se aplica la técnica de ***Data Augmentation***, mediante la cual se pretende lograr
un aumento de la diversidad del conjunto de datos mediante la aplicación de transformaciones a las muestras existentes.

#--------------------------------------------------------EXPLICACIÓN DE LA RED--------------------------------------------------------#

La estructura de la red está formada por 4 capas convolutivas, en las cuales se incrementa el número de neuronas proporcionalmente (32, 64, 128 y 256 filtros por capa convolutiva). Al añadir varias capas consecutivas e incrementar los filtros se pretende 
lograr un aumento de la capacidad de extración de características y una mayor profundidad y representación jerárquica. A continuación se explicará detalladamente esto:
  - ***Capacidad de extracción de características***: Al agregar una capas convolucionales adicionales, el modelo puede aprender representaciones más complejas y sofisticadas de las características presentes en las imágenes. A medida que aumenta el número de capas 
  convolucionales y neuronas, el modelo puede detectar características de mayor nivel de abstracción.
  
  - ***Mayor profundidad y representación jerárquica***: A medida que se añaden capas convolucionales adicionales, se crea una representación jerárquica más profunda de las características de la imagen. Las primeras capas pueden capturar características más 
  simples como bordes y texturas, mientras que las capas posteriores capturan características más complejas y abstractas. Esto permite que el modelo comprenda y discrimine mejor las diferencias sutiles entre las clases de felinos que se están clasificando.
  
Además, cabe destacar que se ha hecho uso de un Kernel de 3x3 en lugar de uno mayor, ya que para este dataset en concreto los resultados son mejores, al capturar características locales detalladas en vez de características globales con un kernel mayor.
  
Por otra parte, es importante resaltar que todas las capas convolutivas son intercaladas con capas de ***Maxpooling*** de 2x2 y de ***Dropout*** (el cual también se va incrementando: 0.2, 0.3 y 0.4). El dropout progresivo ayuda a regularizar la red y prevenir 
el sobreajuste al apagar más unidades en capas convolucionales posteriores, haciendo que la red sea menos dependiente en las capas más profundas y tienda a generalizar mejor las características con conjuntos de datos nunca vistos. 
  
Finalmente, después de las capas convolutivas se aplica la operación de *flatten* para transformar los mapas de características generados por las capas convolucionales en una representación plana adecuada para las capas densas. Y, acto seguido, se añaden dos capas
densas o ***fully connected*** con 128 neuronas cada una e intercaladas con un Droput mayor (0.5), con el objetivo de capturar características especificas y mejorar la discriminación entre las clases de felinos. 
  
Al tener capas densas adicionales al final del modelo, se logra un mayor aprendizaje de características específicas de los felinos. Las capas densas tienen una mayor capacidad para capturar relaciones complejas entre las características extraídas por las capas convolucionales. 
Esto puede ser útil para reconocer patrones distintivos de los felinos, como la forma de las orejas, los ojos o los patrones del pelaje.
  
Mediante la última capa densa y la función de activación ***Softmax***, se podrá finalmente obtener la clase.

#-------------------------------------------------------------RESULTADOS--------------------------------------------------------------#

Con la estructura recién explicada se obtuvo como mejor resultado una precisión en el conjunto de validación del **89.7%**, tal y como se puede observar:

![1](https://github.com/danibetzamora/FSI/assets/72496191/aa15e19e-8ae6-4aa4-824c-86d64735adda)

Además, tal y como se puede observar en la siguiente gráfica, a medida que avanza el entrenamiento de la red se va reduciendo el ***overfitting*** y el error disminuye considerablemente.

![2](https://github.com/danibetzamora/FSI/assets/72496191/ab6a594f-a3e3-46b3-877d-b7765ef65204)

Por último, en la siguiente imagen se visualiza la matriz de confusión resultante:

![3](https://github.com/danibetzamora/FSI/assets/72496191/3e835bbd-cf6c-46bc-9036-dc4e11183721)
