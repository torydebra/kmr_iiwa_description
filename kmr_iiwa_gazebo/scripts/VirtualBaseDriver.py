import math, rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray

class VirtualBaseDriver(Node):
    def __init__(self):
        super().__init__('virtual_base_driver')
        self.yaw = 0.0
        self.create_subscription(JointState, '/kmr_iiwa/joint_states', self.on_js, 10)
        self.create_subscription(Twist, '/kmr_iiwa/cmd_vel', self.on_cmd, 10)
        self.pub = self.create_publisher(
            Float64MultiArray, '/kmr_iiwa/base_velocity_controller/commands', 10)

    def on_js(self, msg):
        if 'base_yaw_joint' in msg.name:
            self.yaw = msg.position[msg.name.index('base_yaw_joint')]

    def on_cmd(self, t):
        c, s = math.cos(self.yaw), math.sin(self.yaw)
        out = Float64MultiArray()
        out.data = [t.linear.x * c - t.linear.y * s,   # base_x_joint
                    t.linear.x * s + t.linear.y * c,   # base_y_joint
                    t.angular.z]                       # base_yaw_joint
        self.pub.publish(out)

def main():
    rclpy.init(); 
    rclpy.spin(VirtualBaseDriver())