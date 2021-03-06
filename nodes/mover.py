#!/usr/bin/env python
import roslib; roslib.load_manifest('robot_mover')
import rospy

from geometry_msgs.msg import Twist

def mover():
    pub = rospy.Publisher('cmd_vel', Twist)
    rospy.init_node('robot_mover')

    twist = Twist();
    twist.linear.x = 0.5; # move forward at 0.1 m/s   

#forward
###############################################################
    rospy.loginfo("still.")
    pub.publish(twist)
    rospy.sleep(2)

    rospy.loginfo("Moving the robot forward: slow.")
    twist.linear.x = 0.5; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("Moving the robot forward: fast.")
    twist.linear.x = 1; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);
###############################################################

#backward
###############################################################
    rospy.loginfo("Moving the robot backward: slow.");
    twist = Twist();
    twist.linear.x = -0.5
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("Moving the robot backward: fast.");
    twist = Twist();
    twist.linear.x = -1
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);
###############################################################

#right strafing
###############################################################
    rospy.loginfo("Moving the robot right: slow.");
    twist = Twist();
    twist.linear.y = -0.5
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("Moving the robot right: fast.");
    twist = Twist();
    twist.linear.y = -1
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);
###############################################################
    
#left strafing
###############################################################
    rospy.loginfo("Moving the robot left: slow.");
    twist = Twist();
    twist.linear.y = 0.5
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("Moving the robot left: fast.");
    twist = Twist();
    twist.linear.y = 1
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);
###############################################################

#turn right
###############################################################
    rospy.loginfo("Turning the robot right:. slow");
    twist.angular.z = -0.5
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("Turning the robot right: fast.");
    twist.angular.z = -1
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);
###############################################################

#turn left
###############################################################
    rospy.loginfo("Turning the robot left:. slow");
    twist.angular.z = 0.5
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("Turning the robot left: fast.");
    twist.angular.z = 1
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);
###############################################################

    rospy.loginfo("Stopping!")
    twist = Twist()
    pub.publish(twist)

    rospy.loginfo("Node exiting.");

if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException: pass
