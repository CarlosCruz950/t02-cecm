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

# Generamos una funcion para obtener nuestra posicion en X y Y
def newOdom(msg):
    # Generamos variables globales para usarlas en cualquier lado
    global x
    global y
    global theta

    # Obtenemos la posicion en X y Y y las guardamos en las variables x,y
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    # Obtenemos la orientacioin del robot
    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
```
Por otro lado, tenemos la construcción de nuestra funcion para obtener la distancia que exite de nuestro robot a un objeto.

``` py
# Generamos una funcion para poder hacer funcionar el sensor
def sensor_callback(msg):
    global wall
    wall = msg.ranges[300] # Obtenemos la distancia que hay hacia un obstaculo
```
En este caso hemos puesto como variable global "wall" porque la usaremos más adelante en nuestro programa para poder preguntar si debemos girar o podemos avanzar.

Para poder obtener las coordenadas a las que queremos llegar, debemos pedirla al usuario, esto lo podemos hacer con las siguientes líneas.

``` py
# Pedimos por primera vez nuestros datos
goal.x = float(input('Escribe la coordenada en x --> '))
goal.y = float(input('Escribe la coordenada en y --> '))

# Preguntamos si queremos visualizar la posicion en la que se encuentra el robot
option = int(input("Deseas saber tus coordenadas? [S = 1][N = 0] --> "))
```
En este caso pedimos tres cosas, primero sería la coordenada en X y la coordenada en Y, como tercera petición tenemos la opción de mostrar o no las coordenadas en las que nos encontramos, esto lo hacemos solamente para que el usuario se ubique en conde esta y corroborar si está en la posición correcta. Esto último podemos verlo en las siguientes líneas, esta parte del programa la podemos encontrar dentro de un while el cual nos ayuda a que el programa siga corriendo y podamos seguir pidiendo coordenadas nuevas o si queremos abortar nuestro programa.

``` py
    # Creamos la condicion donde imprimimos las coordenadas o no
    if option == 1:
        print('Estamos en la coordenada (',round(x,2),' , ',round(y,2),')')
```

Las partes de código mostradas nos ayudarán para poder saber qué es lo que tenemos en frente y además en donde nos encontramos, pero aún no podemos movernos, por ello necesitamos algunas cosas, por ejemplo, calcular la distancia que existe de nuestro robot a la coordenada X y Y, además, también debemos conocer el ángulo en el que se encuentran dichas distancias, para ello, usaremos las coordenadas que el usuario ha asignado y las coordenadas que obtenemos con ayuda de "newOdom". Los cálculos necesarios para poder hacer esto los encontramos en las siguientes lineas, donde inc_x es la distancia que existe entre nuestro robot de la coordenada x e inc_y es la distancia que existe entre el robot y la coordenada y. Por otra parte, con angle_to_goal calculamos el ángulo que existe entre inc_y, inc_x, el cual será necesario para indicarnos si tenemos que girar o no.

``` py
   # Calculamos la distancia que existe entre las coordenadas actuales y las que asignamos
    inc_x = goal.x -x
    inc_y = goal.y -y

    #Calculamos el angulo que existe entre los puntos   
    angle_to_goal = atan2(inc_y, inc_x)
```

Con los datos que obtendrémos con las variables anteriores podremos mover nuestro robot, esto con ayuda de las siguientes condiciones.

``` py
   if abs(angle_to_goal - theta) > 0.1: # Preguntamos si la diferencia de theta y el angulo calculado es igual a 0.1
        speed.linear.x = 0.0
        speed.angular.z = 0.3
    elif wall <= 1: # Tenemos un caso en el que si encontramos un obstaculo haremos lo siguiente:
        print("Obstaculo, hay que huir que nos llega la ley") # Avisamos que existe un obstaculo
        # Retrocedemos un poco para poder girar bien
        speed.linear.x = -0.3
        speed.angular.z = 0.0
        pub.publish(speed)
        time.sleep(2) # Nos ayuda a mantener la velocidad lineal por 2 segundos en lo que rerocede
        # Comenzamos a girar en sentido antihorario
        speed.linear.x = 0.0
        speed.angular.z = 0.3
        pub.publish(speed)
        time.sleep(5) # Giramos por 5 segundos
        # Avanzamos para evadir el obstaculo
        speed.linear.x = 0.5
        speed.angular.z = 0.0
        pub.publish(speed)
        time.sleep(6) # Avanzamos 6 segundos para poder tener una mayor distancia para no chocar
    else:
        speed.linear.x = 0.2
        speed.angular.z = 0.0
```

En la primer condicional tenemos que si la diferencia del ángulo calculado y la theta que calculamos con ayuda de newOdom es mayor a 0.1 debemos de pararnos y comenzar a girar hasta que la condición deje de cumplirse. En la siguiente condición nos dice que si la distancia del obstáculo "wall" es menor o igual a 1, tenemos que hacer unos movimientos que nos aparten de dicho obstáculo, para ello, primero retrocedemos un poco, giramos y posteriormente volvemos a avanzar para quitarnos de ese obstáculo, en este caso hemos usado "pub.publish(speed)" para poder asignarle las variables de velocidad lineal y angular a nuestro robot y que todo eso lo haga en esta sola condición. Finalmente, en nuestro tercer caso, no hay ningún obstáculo que nos impida seguir y además la diferencia del ángulo calculado y la theta cumplen con que es menor a 0.1, por lo cual podemos avanzar sin problema.
Todo lo anterior nos ayuda a que el robot Waffle llegue a su punto destino, sin embargo, podemos encontrarnos con la problemática en la que tengamos que volver a correr el programa creado para asignarle nuevas coordenadas, además, nos encontramos que si llegamos a las coordenadas deseadas, el robot jamás dejará de moverse, para ello, creamos dos rangos (rango_x,rango_y) los cuales nos ayudarán a saber si estamos en una tolerancia considerable para poder decir que llegamos a las coordenadas.


``` py
# Creamos dos rangos que nos serviran como tolerancia para que el robot no se quede girando
    rango_x = numpy.arange(-0.05,0.05,0.01)
    rango_y = numpy.arange(-0.05,0.05,0.01)
    # Creamos la condicion donde preguntaremos si inc_x e inc_y estan dentro de nuestra tolerancia
    if round(inc_x,2) in rango_x and round(inc_y,2) in rango_y:
        # En caso de que si estemos en la tolerancia paramos el robot
        speed.linear.x = 0.0
        speed.angular.z = 0.0
        # Publicamos la velocidad a nuestro robot
        pub.publish(speed)
        r.sleep()
        print('Hemos llegado a las coordenadas [x = ',goal.x,'y = ',goal.y,']')
```

Podemos observar que cuando entramos en el "if" asignamos la velocidad linear y angular como 0.0 para que el robot se detenga por completo y deje de girar, además indicamos que hemos llegado a las coordenadas que el usuario solicitó.

Finalmente, para que el usuario pueda añadir nuevas coordenadas, creamos las siguientes líneas.


``` py
        # Creamos una variable para preguntar si queremos coordenadas nuevas
        aux = input('Quieres coordenadas nuevas? [S = 1][N = 0] --> ')
        if aux == 0 or aux == 0: # En caso de que no, entonces el programa terminara
            print("Nos vemos :D")
            exit()
        elif aux == 1 or aux == 1: # En caso de que si, entonces pedimos los mismos datos de nuevo
            print("Va va va va ya estas, entonces vamos de nuevo 7u7r")
            goal.x = int(input('Escribe la coordenada en x --> '))
            goal.y = int(input('Escribe la coordenada en y --> '))
            option = int(input("Deseas saber tus coordenadas? [S = 1][N = 0] --> "))
        else:
            print('Ingresa bien lo que se pide por favor UnU, no seas malito :(')
 
    # Publicamos a nuestro robot la velocidad calculada
    pub.publish(speed)
    r.sleep()
```
En este caso, asignamos dos opciones, Si y no, en forma de 1 y 0, en caso en el que el usuario no quiera más coordenadas, entonces el programa terminará, pero si el usuario quiere volver a poner nuevas coordenadas, entonces volvemos a pedir los mismos datos que pedimos al inicio del programa. Finalmente, usamos pub.publish(speed) para asignar las velocidades de las condiciones de avanzar o girar.

## Conclusiones

Pudimos conocer de mejor forma a través del uso de suscriptores, publicadores y otros elementos(en especial de los publicadores) como podemos hacer el cambio de estado de nuestro robot, pues cumplimos de manera satisfactoria los objetivos planteados los cuales eran principalmente el mover el robot a una serie de coordenadas, mientras que si se encontraba con un obstáculo de por medio, este se podría mover para esquivar tales obstáculos, esto debido a que el robot cuenta con un Sensor Laser que nos ayuda a detectar los objetos cercanos a él en un rango de 360°, con lo que es prácticamente imposible que pueda colisionar a menos de que encuentre un punto ciego el cual no estemos considerando a la hora de correr el programa. Si bien resultó complicado en un principio la tarea ya que la lógica manejada era más elevada que en la tarea anterior, era cuestión de suscribirnos a los nodos correctos que permitian la correcta interacción entre el robot y la programación que estabmos manejando. Además de la correcta implementación de variables que pudieramos ocupar en distintas funciones que declaramos a lo largo del programa para que se comunicará de forma adecuada el robot.

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


