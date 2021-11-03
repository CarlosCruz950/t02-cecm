#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from pubsub.msg import Estatus
from geometry_msgs.msg import Twist

def process_msg_callback(msg):
        #comm=comando a ingresar para mover el robot
    comm=raw_input("Ingrese la instrucción a realizar:")
    if comm[:1]=='Avanza':
            vel.linear.x=float(comm[1:])
    elif comm[:2]=="Gira":
            vel.angular.z=float(comm[2:])
    elif comm=="Detente":
            vel.linear.x=0
            vel.angular.z=0
    else:
            rospy.loginfo("Error")
    pub1.publish(vel)
    dx = msg.twist.twist.linear.x
    #Debido a que nuestro robot es (2,0) no puede moverse sobre el eje Y
    #dy = msg.twist.twist.linear.y
    theta = round(msg.twist.twist.angular.z, 2)
    rospy.loginfo('La velocidad lineal del robot es de={:.2f} m/s, su velocidad angular es={:.2f} radianes'.format(dx,theta))
    if dx == 0.0 and theta == 0.0:
            pubmsg.codigo=0
            pubmsg.estado='Detenido'
    elif dx != 0.0 and theta == 0.0:
            pubmsg.codigo = 100 
            pubmsg.estado = 'Avanza linealmente: {} m'.format(dx)
    elif dx == 0.0 and theta != 0.0:
            pubmsg.codigo = 200 
            pubmsg.estado = 'Giro(angular): {} rads' .format(theta)
    elif dx != 0.0 and theta != 0.0:
            pubmsg.codigo = 300 
            pubmsg.estado = 'Velocidad lineal: {} m y angular:{} rads'.format(dx,theta)
    else:
            pubmsg.codigo = 1000
            pubmsg.estado = 'Error'
    pub2.publish(pubmsg)


rospy.init_node('robot_comm')
sub = rospy. Subscriber('odom', Odometry, process_msg_callback)
pub1 = rospy.Publisher('cmd_vel',Twist,queue_size=1)
pub2 = rospy.Publisher('estatus', Estatus, queue_size=2)    
rate = rospy.Rate(2)
vel = Twist()
pubmsg=Estatus()
rospy.spin()
