import math
import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


class TrajPub(Node):
    def __init__(self):
        super().__init__('traj_pub')
        self.pub = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 10)
        self.t = 0.0
        self.timer = self.create_timer(0.2, self.tick)

    def tick(self):
        self.t += 0.2
        msg = JointTrajectory()
        msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4']
        pt = JointTrajectoryPoint()
        pt.positions = [
            0.5 * math.sin(self.t),
            0.4 * math.sin(self.t),
            -0.4 * math.sin(self.t),
            0.3 * math.sin(self.t),
        ]
        pt.time_from_start = Duration(sec=0, nanosec=200000000)
        msg.points = [pt]
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = TrajPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
