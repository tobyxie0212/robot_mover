#!/usr/bin/env python
import roslib; roslib.load_manifest('robot_mover')
import rospy

from geometry_msgs.msg import Twist

def mover():
    pub = rospy.Publisher('cmd_vel', Twist)
    rospy.init_node('robot_mover')

    twist = Twist();
    twist.linear.x = 0.5; # move forward at 0.1 m/s   

#diagonal motion
###############################################################
    rospy.loginfo("still.")
    pub.publish(twist)
    rospy.sleep(2)

    rospy.loginfo("diagonal left forward: slow.")
    twist = Twist();		twist.linear.x = 0.5;		twist.linear.y = 0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("diagonal left forward: fast.")
    twist = Twist();		twist.linear.x = 1;		twist.linear.y = 1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("diagonal right backward slow.")
    twist = Twist();		twist.linear.x = -0.5;		twist.linear.y = -0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("diagonal right backward: fast.")
    twist = Twist();		twist.linear.x = -1;		twist.linear.y = -1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("diagonal right forward: slow.")
    twist = Twist();		twist.linear.x = 0.5;		twist.linear.y = -0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("diagonal right forward: fast.")
    twist = Twist();		twist.linear.x = 1;		twist.linear.y = -1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("diagonal left backward: slow.")
    twist = Twist();		twist.linear.x = -0.5;		twist.linear.y = 0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("diagonal left backward: fast.")
    twist = Twist();		twist.linear.x = -1;		twist.linear.y = 1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);
###############################################################

#forward/back curve
###############################################################
    rospy.loginfo("left rotation forward: slow.")
    twist = Twist();		twist.linear.x = 0.5;		twist.linear.y = 0;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0.5;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation forward: fast.")
    twist = Twist();		twist.linear.x = 1;		twist.linear.y = 0;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 1;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation backward: slow.")
    twist = Twist();		twist.linear.x = -0.5;		twist.linear.y = 0;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -0.5;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation backward: fast.")
    twist = Twist();		twist.linear.x = -1;		twist.linear.y = 0;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -1;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation forward: slow.")
    twist = Twist();		twist.linear.x = 0.5;		twist.linear.y = 0;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -0.5; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation forward: fast.")
    twist = Twist();		twist.linear.x = 1;		twist.linear.y = 0;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -1; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation backward: slow.")
    twist = Twist();		twist.linear.x = -0.5;		twist.linear.y = 0;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0.5; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation backward: fast.")
    twist = Twist();		twist.linear.x = -1;		twist.linear.y = 0;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 1; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);
###############################################################

#right strafing
###############################################################
    rospy.loginfo("left rotation left: slow.")
    twist = Twist();		twist.linear.x = 0;		twist.linear.y = 0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0.5;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation left: fast.")
    twist = Twist();		twist.linear.x = 0;		twist.linear.y = 1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 1;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation right: slow.")
    twist = Twist();		twist.linear.x = 0;		twist.linear.y = -0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -0.5;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation right: fast.")
    twist = Twist();		twist.linear.x = 0;		twist.linear.y = -1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -1;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation left: slow.")
    twist = Twist();		twist.linear.x = 0;		twist.linear.y = 0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -0.5; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation left: fast.")
    twist = Twist();		twist.linear.x = 0;		twist.linear.y = 1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -1; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation right: slow.")
    twist = Twist();		twist.linear.x = 0;		twist.linear.y = -0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0.5; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation right: fast.")
    twist = Twist();		twist.linear.x = 0;		twist.linear.y = -1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 1; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);
###############################################################
    
#diagonal curve
###############################################################
    rospy.loginfo("left rotation left forward: slow.")
    twist = Twist();		twist.linear.x = 0.5;		twist.linear.y = 0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0.5;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation left forward: fast.")
    twist = Twist();		twist.linear.x = 1;		twist.linear.y = 1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 1;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation right backward: slow.")
    twist = Twist();		twist.linear.x = -0.5;		twist.linear.y = -0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -0.5;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation right backward: fast.")
    twist = Twist();		twist.linear.x = -1;		twist.linear.y = -1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -1;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation left forward: slow.")
    twist = Twist();		twist.linear.x = 0.5;		twist.linear.y = 0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -0.5; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation left forward: fast.")
    twist = Twist();		twist.linear.x = 1;		twist.linear.y = 1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -1; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation right backward: slow.")
    twist = Twist();		twist.linear.x = -0.5;		twist.linear.y = -0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0.5; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation right backward: fast.")
    twist = Twist();		twist.linear.x = -1;		twist.linear.y = -1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 1; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);
##
    rospy.loginfo("left rotation right forward: slow.")
    twist = Twist();		twist.linear.x = 0.5;		twist.linear.y = -0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0.5;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation right forward: fast.")
    twist = Twist();		twist.linear.x = 1;		twist.linear.y = -1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 1;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation left backward: slow.")
    twist = Twist();		twist.linear.x = -0.5;		twist.linear.y = 0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -0.5;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation left backward: fast.")
    twist = Twist();		twist.linear.x = -1;		twist.linear.y = 1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -1;
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation right forward: slow.")
    twist = Twist();		twist.linear.x = 0.5;		twist.linear.y = -0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -0.5; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("right rotation right forward: fast.")
    twist = Twist();		twist.linear.x = 1;		twist.linear.y = -1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = -1; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation left backward: slow.")
    twist = Twist();		twist.linear.x = -0.5;		twist.linear.y = 0.5;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 0.5; 
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("still.");
    twist = Twist();
    pub.publish(twist)
    rospy.sleep(2);

    rospy.loginfo("left rotation left backward: fast.")
    twist = Twist();		twist.linear.x = -1;		twist.linear.y = 1;		twist.linear.z = 0;		twist.angular.x = 0;		twist.angular.y = 0;		twist.angular.z = 1; 
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
