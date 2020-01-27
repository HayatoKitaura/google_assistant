#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node('publish_voice', anonymous=True)
    pub = rospy.Publisher('/voice_recognition/start', String, queue_size=10)
    r = rospy.Rate(0.2) # 10hz
    print("start")
    while not rospy.is_shutdown():
        a = "starting"
        pub.publish(a)

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException: pass
