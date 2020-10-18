#!/usr/bin/env python

# Importing required libraries and dependencies
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

PI = 3.1415926535897

# Function to print the current coordinates of the turtle 
# and the angle it makes with the positive x axis
def pose_callback(pose):
	rospy.loginfo("Moving in circle \n Turtle X = %f: Y = %f: \n", pose.x, pose.y )

# Main node function
def main():

    #Starting the node
    rospy.init_node('move_turtle',anonymous=True)
    
    # Initialising Publisher and Subscriber topics
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    v = Twist()
    
    # Meme est Potentia
    print( "Whomst have summoned the elevated one? ")
    
    speed =0.8
    angle =360
    offset=0.25
    # (speed*2*PI)/360 radians/sec
    omega=0.7
    
    # Converting angle in degrees to radians
    radian_angle= (angle *2 * PI) / 360
    
    # Initialising initial positions 
    v.linear.x=speed
    v.linear.y=0
    v.linear.z=0
    
    v.angular.x=0
    v.angular.y=0
    
    # The angular velocity of z axis will be Omega
    v.angular.z=abs(omega)
    
    # Finding the initial time
    t0=rospy.Time.now().to_sec()
    
    current_angle=0
    rospy.Subscriber('/turtle1/pose', Pose , pose_callback)
        
    # Loops till the turtle completes one circle
    while(current_angle <= radian_angle + offset):
        velocity_publisher.publish(v)
        t1 = rospy.Time.now().to_sec()
        current_angle = omega*(t1-t0)
        
    # In the end, the turtle will be aligned horizontally    
    v.angular.z = 0
    # Finally, the linear speed will be 0 as the turtle will stop
    v.linear.x=0
    
    velocity_publisher.publish(v)
    

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
