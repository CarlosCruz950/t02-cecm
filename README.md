# TAREA 2 - Cruz Montero Carlos Enrique

# [ROS - Simulación, Tarea 02]

| Código | Description |
| ------:| ----------- |
| ***TSM*** | 02 | 
| **TSR-2022-I** | Tarea *02* |
| **Robotica-2022-I**  | Tarea *02* |

## Contenido

- [Objetivo](#Objetivo)
- [Introduccion](#Introduccion)
- [Desarrollo](#Desarrollo)
- [Conclusiones](#Conclusiones)
- [Autores](#Autores)
- [Referencias](#Referencias)

## Objetivo

* Mover al robot de su posición inicial a un punto dado de coordenadas (X, Y).
* Esquivar objetos con ayuda del sensor Lider

## Introduccion
- SENSORES QUE COMPONEN AL TURTLEBOT3

Sensor LDS (Laser Distance Sensor):  Esencial para la realización del mapeo, localización y navegación. Este sensor es conectado directamente hacia la tarjeta Rasberry Pi o SBC, la cual es encargada de recibir los datos del sensor laser y generar una simultanea localización y mapeo (SLAM) del lugar a ser recorrido.
También este laser permite hacer la detección y adquisición de datos de los objetos a su alrededor en un ángulo de 360°
Sensor Encoder(AMS): Dispositivo electromecánico que permite codificar el movimiento mecánico en distintos pulsos eléctricos ya sea en forma de digitales binarios, en función de los impulsos de onda, pulsos, etcétera.

- TRANSMISIÓN DE DATOS EN ROS

En principio al ejecutarse el programa contendrá todos los nodos de conexión entre el robot y el computador junto con los parámetros y las variables definidas para su funcionamiento. El robot enviara los datos del sensor laser y serán visualizados y mapeados simultáneamente utilizando el programa Rviz. El algoritmo de funcionamiento general permite tener una constante lectura del robot con respecto a la generación de trayectorias trazadas en el programa “Rviz”. El funcionamiento del robot es seguido gráficamente mediante una sucesión de nodos que realizan funciones independientes. Cada función es construida y ejecutada desde un directorio y un archivo que define los parámetros y variables que serán necesarias. Los nodos asociados a la programación del ordenador y el robot permiten la comunicación con ROS mediante mensajes teniendo incluso conexión con elementos externos.

Los tópicos son acciones más específicas que el sistema pueda acceder en cada nodo. Cada nodo puede tener más de un tópico. Cuando uno nodo está en funcionamiento se asocia a un tópico que permitirá realizar una tarea de manera específica a través de ordenes por medio de mensajes. Los mensajes son asociados a “suscripción y publicador” en ROS. La suscripción es el encargado de etiquetan a un tópico con el nodo y acceder a información entre nodos y tópicos. El publicador es el encargado de permitir ver la información asociada a un nodo o tópico para visualizarse o realizar alguna tarea. Gráficamente los nodos son escritos con una circunferencia y los tópicos con un rectángulo, construidos a partir de la ejecución de archivos c++ o Python. 

## Desarrollo


``` py

```
## Conclusiones

Pudimos conocer de mejor forma a través del uso de suscriptores, publicadores y otros elementos(en especial de los publicadores) como podemos hacer el cambio de estado de nuestro robot, pues cumplimos de manera satisfactoria los objetivos planteados los cuales eran principalmente el mover el robot a una serie de coordenadas, mientras que si se encontraba con un obstáculo de por medio, este se podría mover para esquivar tales obstáculos, esto debido a que el robot cuenta con un Sensor Laser que nos ayuda a detectar los objetos cercanos a él en un rango de 360°, con lo que es prácticamente imposible que pueda colisionar a menos de que encuentre un punto ciego el cual no estemos considerando a la hora de correr el programa. Si bien resultó complicado en un principio la tarea ya que la lógica manejada era más elevada que en la tarea anterior, era cuestión de suscribirnos a los nodos correctos que permitian la correcta interacción entre el robot y la programación que estabmos manejando.

## Autores
| Iniciales  | Description |
| ----------:| ----------- |
| **CMCE** | Carlos Enrique Cruz Montero [GitHub profile](https://github.com/CarlosCruz950) |
| **MTJ**  | Jaqueline Mejia Trejo [GitHub profile](https://github.com/ErikFiUNAM) |
| **TRH** | Hugo Torres Rocha [GitHub profile](https://github.com/HugoTR315) |

## Referencias

* Martínez, D. (Mayo de 2019). Universidad Santo Tomás. Obtenido de Facultad de Ingeniería Electrónica: https://repository.usta.edu.co/bitstream/handle/11634/18667/2019davidmartinez.pdf?sequence=1&isAllowed=y
* https://github.com/CarlosCruz950/t02-cecm/blob/main/docs/InvestigacionParte1.md
* https://github.com/CarlosCruz950/t02-cecm/blob/main/docs/InvestigacionParte2.md


