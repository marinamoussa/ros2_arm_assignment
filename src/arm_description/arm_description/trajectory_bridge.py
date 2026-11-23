import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
from trajectory_msgs.msg import JointTrajectory


class TrajectoryBridge(Node):
    def __init__(self):
        super().__init__('trajectory_bridge')
        self.joints = ['joint1', 'joint2', 'joint3', 'joint4']
        self.current_pos = [0.0, 0.0, 0.0, 0.0]

        self.cmd_pubs = {
            name: self.create_publisher(Float64, f'/model/robotic_arm/joint/{name}/cmd_pos', 10)
            for name in self.joints
        }
        self.js_pub = self.create_publisher(JointState, '/joint_states', 10)
        self.sub = self.create_subscription(
            JointTrajectory,
            '/arm_controller/joint_trajectory',
            self.on_trajectory,
            10,
        )
        self.timer = self.create_timer(0.05, self.publish_joint_states)

    def on_trajectory(self, msg: JointTrajectory):
        if not msg.points:
            return
        pt = msg.points[-1]
        for idx, name in enumerate(msg.joint_names):
            if name in self.joints and idx < len(pt.positions):
                val = float(pt.positions[idx])
                j_idx = self.joints.index(name)
                self.current_pos[j_idx] = val
                out = Float64()
                out.data = val
                self.cmd_pubs[name].publish(out)

    def publish_joint_states(self):
        js = JointState()
        js.header.stamp = self.get_clock().now().to_msg()
        js.name = self.joints
        js.position = list(self.current_pos)
        self.js_pub.publish(js)


def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
