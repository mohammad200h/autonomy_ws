#!/usr/bin/env python3

from lib2to3.pytree import convert
import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class Video_get():
    def __init__(self):
        self.subscriber = rospy.Subscriber("camera/rgb/image_raw", Image, self.process_data,10)
        # setting or writing the frames into a video 
        self.out = cv2.VideoWriter("/home/mamad/Hubby/autonomy_ws/src/atonomous_tb/video/output.avi",cv2.VideoWriter_fourcc('M','J','P','G'),10,(640,480))
        self.bridge = CvBridge() # converting ros images to opencv data 

    def process_data(self,data,a):
        # performing convertion 
        frame = self.bridge.imgmsg_to_cv2(data)
        # write the frames to video 
        self.out.write(frame)
        # displaying what is being recorded 
        cv2.imshow("output",frame)
        # will save video until it is interupted 
        cv2.waitKey(1)


def main(args=None):
    print("Video Recording ")
    rospy.init_node('Video_Recording_Node')
    image_subscriber = Video_get()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
        
        
            