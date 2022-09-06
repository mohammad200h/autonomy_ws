#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal

def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()


    #Sequence 
    goal_seq = [
        [4.1,-3.41, 0],
        [6.5,-1.3, 0],
        [6.5,-6   , 0],
        [2  ,-6.95, 0]
    ]
    for g in goal_seq:

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = g[0]
        goal.target_pose.pose.position.y = g[1]
        goal.target_pose.pose.position.z = g[2]

        goal.target_pose.pose.orientation.w = 0.3
        goal.target_pose.pose.orientation.z = 0.9


        client.send_goal(goal)
        sucess = client.wait_for_result()
        if not sucess:
            rospy.logerr("Action server Down ;/")
        else:
            print("A Gola is Executed")
    return 1


if __name__ == '__main__':
    try:
        rospy.init_node('movebaseClient')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal is Exceuted :D")
    except rospy.ROSInerruptException:
        rospy.loginfo("Navigation Done")
        
            