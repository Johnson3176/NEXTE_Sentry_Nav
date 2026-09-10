#!/usr/bin/python3
# coding=utf8
from __future__ import print_function, division, absolute_import

import argparse

import rospy
import tf.transformations
from geometry_msgs.msg import Pose, Point, Quaternion, PoseWithCovarianceStamped

DEFAULT_COVARIANCE = [
    0.25, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.25, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.06853892326654787,
]

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('x', type=float)
    # parser.add_argument('y', type=float)
    # parser.add_argument('z', type=float)
    # parser.add_argument('yaw', type=float)
    # parser.add_argument('pitch', type=float)
    # parser.add_argument('roll', type=float)
    # args = parser.parse_args()

    rospy.init_node('publish_initial_pose')
    pub_pose = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=1, latch=True)

    # 转换为pose
    xyz=[0.06097930669784546, -0.36113089323043823, 0.0]
    quat = [0.0, 0.0, -0.026097733595889842, 0.999659396145086]
    # quat = tf.transformations.quaternion_from_euler(args.roll, args.pitch, args.yaw)
    # xyz = [args.x, args.y, args.z]

    initial_pose = PoseWithCovarianceStamped()
    initial_pose.pose.pose = Pose(Point(*xyz), Quaternion(*quat))
    initial_pose.pose.covariance = DEFAULT_COVARIANCE
    initial_pose.header.stamp = rospy.Time.now()
    initial_pose.header.frame_id = 'map'
    rospy.sleep(1)
    # rospy.loginfo('Initial Pose: {} {} {} {} {} {}'.format(
    #     args.x, args.y, args.z, args.yaw, args.pitch, args.roll, ))
    # pub_pose.publish(initial_pose)
    rospy.loginfo('Published /initialpose with covariance.')
    rospy.sleep(20)
    pub_pose.publish(initial_pose)
