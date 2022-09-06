#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal
import sys

def movebase_client():
    arguments=sys.argv[1:]
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = float(arguments[0])
    goal.target_pose.pose.position.y = float(arguments[1])
    goal.target_pose.pose.position.z = 0

    goal.target_pose.pose.orientation.w = 0.3
    goal.target_pose.pose.orientation.z = 0.9


    client.send_goal(goal)
    sucess = client.wait_for_result()
    if not sucess:
        rospy.logerr("Action server Down ;/")
    else:
        return client.get_result()


if __name__ == '__main__':
    try:
        rospy.init_node('movebaseClient')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal is Exceuted :D")
    except rospy.ROSInerruptException:
        rospy.loginfo("Navigation Done")
        
            