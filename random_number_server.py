#!/usr/bin/env python
 
import rospy
 
from std_msgs.msg import Int32
# texto a mostrar
def callback(data):
    rospy.loginfo(data.data)
 
# define el subscriber
def random_subscriber():
    rospy.init_node('random_number_subscriber')
    rospy.Subscriber('random_number',Int32, callback)
    rospy.spin()
 
if __name__=='__main__':
    random_subscriber()
