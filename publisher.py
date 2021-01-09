#!/usr/bin/env python3
# -*- coding: utf-8 -*-

                                
import rospy, json                          # Agrego biblioteca
from std_msgs.msg import Int32, String
from geometry_msgs.msg import Pose2D

                               

f = open("config.json", "r")               # Abro fichero (modo lectura)
content = f.read()                         # Leo fichero sobre variable content
jsondecoded = json.loads(content)        

robot_name = jsondecoded["robot_name"]
pose = jsondecoded["pose"]
side = jsondecoded["side"]
mode = jsondecoded["mode"]
routines = jsondecoded["routines"]

#print("Robot = " + robot_name)
#print(robot_name + " está en " + pose)
#print("Comenzamos en el lado " + side)
#print("Activamos la rutina del modo " + mode)
#print(routines)

print("El nodo se ha lanzado")

rospy.init_node('topic_publisher')     # Iniciamos nodo

pub_posavasos = rospy.Publisher('posavasos_config', String, queue_size = 100) # Publisher está en rospy - queue_size elementos en la cola esperando a ser mandados
pub_parejitas = rospy.Publisher('parejitas_config', String, queue_size = 100) # Publisher está en rospy - queue_size elementos en la cola esperando a ser mandados
rate = rospy.Rate(2)    # Frecuencia de envío de mensajes

while not rospy.is_shutdown(): # Mientras que no esté apagado rospy

   if robot_name == "Posavasos":
      pub_posavasos.publish(robot_name)
      
   elif robot_name == "Parejitas":
      pub_parejitas.publish(robot_name)
      
   rate.sleep()