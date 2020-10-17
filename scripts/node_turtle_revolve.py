#!/usr/bin/env python

# Importing required libraries and dependencies
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys

PI = 3.1415926535897

# Function to print the current coordinates of the turtle 
# and the angle it makes with the positive x axis
def pose_callback(pose):
	rospy.loginfo("Turtle X = %f: Y = %f: Theta = %f \n", pose.x, 
					pose.y , pose.theta)

# Main node function
def main():

    #Starting the node
    rospy.init_node('move_turtle',anonymous=True)
    
    # Initialising Publisher and Subscriber topics
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    rospy.Subscriber('/turtle1/pose', Pose , pose_callback)    
    
    # Meme est Potentia
    print( "Whomst have summoned the elevated one? ")
    
    #speed=36 degrees/sec
    r=10
    angle=360
    
    omega=0.5 #speed*2*PI/360 radians/sec
    # Converting angle in degrees to radians
    radian_angle= (angle *2 * PI) / 360
    
    # Initialising initial positions 
    vel_msg.linear.x=1
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    
    vel_msg.angular.x=0
    vel_msg.angular.y=0
    
    # The angular velocity of z axis will be Omega
    vel_msg.angular.z=abs(omega)
    
    # Finding the initial time
    t0=rospy.Time.now().to_sec()
    
    current_angle=0
    
    # Loops till the turtle completes one circle
    while(current_angle < radian_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = omega*(t1-t0)
    
    # In the end, the turtle will be aligned horizontally    
    vel_msg.angular.z = 0
    # Finally, the linear speed will be 0 as the turtle will stop
    vel_msg.linear.x=0
    velocity_publisher.publish(vel_msg)
    

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
