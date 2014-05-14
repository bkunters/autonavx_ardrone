#!/usr/bin/env python
import rospy
import roslib; roslib.load_manifest('ardrone_python')
from ardrone_autonomy.msg import Navdata
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

pub = None

def callback(navdata):
    print("received odometry message: vx=%f vy=%f z=%f"%(navdata.vx,navdata.vy,navdata.altd))
    
if __name__ == '__main__':
    rospy.init_node('example_node', anonymous=True)
    
    # subscribe to navdata (receive from quadrotor)
    rospy.Subscriber("/ardrone/navdata", Navdata, callback)
    
    # publish commands (send to quadrotor)
    pub_velocity = rospy.Publisher('/cmd_vel', Twist)
    pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty)
    pub_land = rospy.Publisher('/ardrone/land', Empty)
    pub_reset = rospy.Publisher('/ardrone/reset', Empty)
    
    rospy.sleep(1.0)
    pub_takeoff.publish(Empty())
    rospy.sleep(5.0)
    pub_land.publish(Empty())
    
    rospy.spin()
