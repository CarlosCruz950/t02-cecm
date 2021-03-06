# TAREA 02 - Cruz Montero Carlos Enrique

## TRANSMISIÓN DE DATOS EN ROS

En principio al ejecutarse el programa contendrá todos los nodos de conexión entre el robot y el computador junto con los parámetros y las variables definidas para su 
funcionamiento. El robot enviara los datos del sensor laser y serán visualizados y mapeados simultáneamente utilizando el programa Rviz. 
El algoritmo de funcionamiento general permite tener una constante lectura del robot con respecto a la generación de trayectorias trazadas en el programa “Rviz”.
El funcionamiento del robot es seguido gráficamente mediante una sucesión de nodos que realizan funciones independientes. 
Cada función es construida y ejecutada desde un directorio y un archivo que define los parámetros y variables que serán necesarias. 
Los nodos asociados a la programación del ordenador y el robot permiten la comunicación con ROS mediante mensajes teniendo incluso conexión con elementos externos.
Los tópicos son acciones más específicas que el sistema pueda acceder en cada nodo. Cada nodo puede tener más de un tópico. Cuando uno nodo está en funcionamiento 
se asocia a un tópico que permitirá realizar una tarea de manera específica a través de ordenes por medio de mensajes. Los mensajes son asociados a “suscripción y 
publicador” en ROS. La suscripción es el encargado de etiquetan a un tópico con el nodo y acceder a información entre nodos y tópicos. El publicador es el encargado 
de permitir ver la información asociada a un nodo o tópico para visualizarse o realizar alguna tarea. Gráficamente los nodos son escritos con una circunferencia y 
los tópicos con un rectángulo, construidos a partir de la ejecución de archivos c++ o Python. 

Los principales nodos a considerar son:
*	El nodo /amcl permite leer la posición inicial del robot, las coordenadas y el continuo escaneo en la variación de su posición para ser publicada en el tópico /particlecloud 
el cual permite analizar la variación de sus coordenadas desde la posición (0, 0, 0) y comunicarse con el computador remotamente.

*	El nodo “Move_base” es necesario para el funcionamiento del robot, en donde se encarga de mover el robot hacia una meta o punto final. En este nodo se asocian “topicos” o 
tareas que permite realizar el funcionamiento total del robot. Este nodo recibe los datos tomados del sensor LDS unido con los datos de posicionamiento del robot para construir 
la trayectoria y variar la velocidad lineal o angular del robot “turltebot 3” mediante el uso del topic /cmd_vel.

*	El nodo /turtlebot3_slam_gmapping permite hacer el mapeo del robot alrededor de su trayectoria. Este nodo recibe los valores de posicionamiento del robot permitiendo tener una
referencia del robot dentro del mapa.

*	El nodo explore_server es el encargado de recibir el valor del punto final de la trayectoria y convertir este valor es un valor binario. Este valor binario va ser recibido por 
el nodo move_base para realizar la trayectoria desde el punto posicionado del robot hasta el punto final definido por el usuario

*	El nodo turtlebot3_core es el encargado de recibir los valores del tópico /cmd_vel y guiar el robot a través de la trayectoria creada por el nodo move_base controlando el valor de posición, orientación y covarianza del robot.

## BIBLIOGRAFÍA

Martínez, D. (Mayo de 2019). Universidad Santo Tomás. Obtenido de Facultad de Ingeniería Electrónica: 
https://repository.usta.edu.co/bitstream/handle/11634/18667/2019davidmartinez.pdf?sequence=1&isAllowed=y

