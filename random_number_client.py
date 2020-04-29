#!/usr/bin/env python
import rospy
 
from std_msgs.msg import Int32
from random import randint
 
# define el Publisher
def random_number_publisher():
    rospy.init_node('random_number_publisher')
    pub=rospy.Publisher('random_number', Int32, queue_size=10)
    rate= rospy.Rate(5)
# genera un numero aleatorio cada 5s
    while not rospy.is_shutdown():
        random_msg=randint(0,5000)
        rospy.loginfo(random_msg)
        pub.publish(random_msg)
        rate.sleep()
 
if __name__=='__main__':
    try:
        random_number_publisher()
    except rospy.ROSInterruptException:
        pass
