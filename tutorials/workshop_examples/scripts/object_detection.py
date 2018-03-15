#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range

distance=0
vel_msg = Twist()
vel_msg.linear.x = 0
vel_msg.linear.y = 0
vel_msg.linear.z = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0

def callback(data):
    distance=data.range
    rospy.loginfo(rospy.get_caller_id() + "I heard %f", data.range)
    if(distance>0.8):
       	vel_msg.linear.x = 0.1
    else:
       	vel_msg.linear.x = 0

    #Publish the velocity
    velocity_publisher.publish(vel_msg)
        
if __name__ == '__main__':

    # Starts a new node
    rospy.init_node('object_detection', anonymous=True)
    rospy.Subscriber("distance", Range, callback)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    rospy.spin()
    #Checking if the move or stop
    # while not rospy.is_shutdown():

        
        

