import tkinter as tk
from builtin_interfaces.msg import Duration
import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


class JointSliderGui(Node):
    def __init__(self):
        super().__init__('joint_slider_gui')
        self.pub = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 10)
        self.root = tk.Tk()
        self.root.title('Arm Joint Controller')
        self.scales = []

        joint_names = ['joint1', 'joint2', 'joint3', 'joint4']
        for name in joint_names:
            row = tk.Frame(self.root)
            row.pack(fill='x', padx=10, pady=5)
            tk.Label(row, text=name, width=8, anchor='w').pack(side='left')
            sc = tk.Scale(
                row,
                from_=-1.57,
                to=1.57,
                resolution=0.05,
                orient='horizontal',
                length=240,
                command=lambda _val: self.publish_now(),
            )
            sc.set(0.0)
            sc.pack(side='right')
            self.scales.append(sc)

        tk.Button(self.root, text='Center (0.0)', command=self.reset_all).pack(pady=8)
        self.joint_names = joint_names

    def reset_all(self):
        for sc in self.scales:
            sc.set(0.0)
        self.publish_now()

    def publish_now(self):
        msg = JointTrajectory()
        msg.joint_names = self.joint_names
        pt = JointTrajectoryPoint()
        pt.positions = [float(sc.get()) for sc in self.scales]
        pt.time_from_start = Duration(sec=0, nanosec=200000000)
        msg.points = [pt]
        self.pub.publish(msg)

    def spin_gui(self):
        while rclpy.ok():
            rclpy.spin_once(self, timeout_sec=0.02)
            try:
                self.root.update_idletasks()
                self.root.update()
            except tk.TclError:
                break


def main(args=None):
    rclpy.init(args=args)
    node = JointSliderGui()
    node.publish_now()
    node.spin_gui()
    node.destroy_node()
    rclpy.shutdown()
