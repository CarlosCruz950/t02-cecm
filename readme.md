# Tarea 02

* Investigación. 
Investigar los diferentes sensores que componen al robot Robotis Turtlebot3 Waffle y su transmisión de datos en ROS (nodos, tópicos, servicios, simulaciones).

## SENSORES QUE COMPONEN AL TURTLEBOT3

* Sensor LDS (Laser Distance Sensor):  Esencial para la realización del mapeo, localización y navegación. Este sensor es conectado directamente hacia la tarjeta Rasberry Pi o SBC, la cual es encargada de recibir los datos del sensor laser y generar una simultanea localización y mapeo (SLAM) del lugar a ser recorrido.

También este laser permite hacer la detección y adquisición de datos de los objetos a su alrededor en un ángulo de 360°

* Sensor Encoder(AMS): Dispositivo electromecánico que permite codificar el movimiento mecánico en distintos pulsos eléctricos ya sea en forma de digitales binarios, en función de los impulsos de onda, pulsos, etcétera.
Básicamente un encoder lineal se compone de un módulo fijo y otro móvil (el que se une a las partes móviles de la máquina con la cual se hará la interfaz). El módulo fijo contiene el sensor y la electrónica necesarias para detectar y medir el movimiento, y convertirlo en impulsos eléctricos inteligibles por otro circuito digital o analógico.
El módulo de lectura puede utilizar distintas tecnologías para medir la posición de la barra móvil.

## BIBLIOGRAFÍA

Martínez, D. (Mayo de 2019). Universidad Santo Tomás. Obtenido de Facultad de Ingeniería Electrónica: https://repository.usta.edu.co/bitstream/handle/11634/18667/2019davidmartinez.pdf?sequence=1&isAllowed=y

