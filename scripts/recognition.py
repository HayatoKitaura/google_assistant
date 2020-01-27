#!/usr/bin/env python
# coding: utf-8
import click
import rospy
from std_msgs.msg import String
from module import google_assistant
from crane_x7_examples.srv import call_dso, call_dsoResponse

#引数は en-US か ja_jp
@click.command()
@click.option("--lang", default="ja_jp")
@click.option("--debug", default=False)
@click.option("--answer", default=False)
def start(lang, debug, answer):
    def callback(data):
        rospy.loginfo("Recognition Start")
        result, answer = assistant.start()

        print("debug:" + result)

        result = result.encode('utf_8')
        if(result == 'ペンライトを掴んで' or result == 'ペンライト' or result == 'ペンライトを振って'):
            rospy.wait_for_service('detect_swing_object')
            call = rospy.ServiceProxy('detect_swing_object', call_dso)
            call(True)

    rospy.Subscriber("voice_recognition/start", String, callback)
    r = rospy.Rate(10)

    assistant = google_assistant.main(lang, debug, answer)

    rospy.spin()


if __name__ == '__main__':
    rospy.init_node('voice_recognition', anonymous=False)
    # assistant = google_assistant.main(lang, debug, answer)
    start()
