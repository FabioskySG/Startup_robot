#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D

def callback(msg):
    print(msg.data)

rospy.init_node('node_suscriber')

sub_posavasos = rospy.Subscriber('posavasos_config', String, callback)  # Callback es lo que se hace cuando el suscriptor recibe algo
sub_parejitas = rospy.Subscriber('parejitas_config', String, callback)  # Callback es lo que se hace cuando el suscriptor recibe algo
rospy.spin()