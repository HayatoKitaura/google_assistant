#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import rospy
from std_msgs.msg import String
from module import google_assistant
from module.analyse import *
import pprint
import signal
import sys

import sys
import signal
import csv
import pygame
import time
import subprocess


def handler(signal, frame):
    sys.exit(0)


signal.signal(signal.SIGINT, handler)

'''
@click.command()
@click.option("--lang", default="en-US")
@click.option("--debug", default=False)
@click.option("--answer", default=False)
'''


def start(lang, debug, answer):
    def wakeup():
        # rospy.loginfo("Recognition Start")
        result, answer = assistant.start()
        result = result.lower()
        answer = answer.lower()
        print("[Result] %s" % result)

        tagged = analyse.tagged(result)
        print(tagged)
        nns = analyse.get_nn(tagged)
        print(analyse.get_location(nns))
        print(analyse.get_vb(tagged))

        assistant.stop()

        location = analyse.get_location(nns)
        verb = analyse.get_vb(tagged)
        print(location)
        print(len(verb))
        if location is not None and len(verb) > 0:
            if verb[0][0] == "go":
                play("OK, I go to the" + location)
                navigation_publisher.publish(location)

            if verb[0][0] == "are" and "in" in result:
                play("OK, Here is " + location)
                current_publisher.publish(location)

        pub.publish(result)

    def stop(message):
        assistant.stop()

    rospy.init_node('voice_recognition', anonymous=False)
    rospy.Subscriber("voice_recognition/stop", String, stop)
    pub = rospy.Publisher('voice_recognition/result', String, queue_size=10)
    current_publisher = rospy.Publisher('location/register/current', String, queue_size=10)
    navigation_publisher = rospy.Publisher("navigation/start", String, queue_size=10)

    assistant = google_assistant.main(lang, debug, answer)
    r = rospy.Rate(10)
    analyse = Analyse("/home/ubuntu/dictionary.csv")
    while not rospy.is_shutdown():
        wakeup()
        break
        '''
        word, answer = assistant.start()
        if str(word).lower() == "excuse me":
            assistant.stop()
            play("Hi, how can I help you?")
            wakeup()
        r.sleep()
        '''


def play(text):
    # type: (str) -> int
    return subprocess.call(["bash", "/home/ubuntu/ros/sound/svox.sh", text])


if __name__ == '__main__':
    start(lang="en-US", debug=False, answer=False)
