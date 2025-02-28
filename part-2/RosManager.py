import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from collections import deque
import time

class RosManager(Node):
    def __init__(self, path):
        rclpy.init(args=None)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.path = deque(path)

    def execute_path(self):
        twist = Twist()

        speed_x = 1.0
        turn_90 = 1.0
        turn_270 = 4.0

        while self.path:
            action = self.path.popleft()
            self.get_logger().info(f"Executing: {action}")

            if action == 'Up':
                twist.linear.x = -speed_x
                self.publisher_.publish(twist)
                time.sleep(1.0)
            if action == 'Down':
                twist.linear.x = speed_x
                self.publisher_.publish(twist)
                time.sleep(1.0)
            if action == 'Right':
                twist.angular.z = -turn_90
                self.publisher_.publish(twist)
                time.sleep(1.0)

                twist.linear.x = speed_x
                self.publisher_.publish(twist)
                time.sleep(1.0)

                twist.angular.z = -turn_270
                self.publisher_.publish(twist)
                time.sleep(1.0)
            if action == 'Left':
                twist.angular.z = turn_270
                self.publisher_.publish(twist)
                time.sleep(1.0)

                twist.linear.x = speed_x
                self.publisher_.publish(twist)
                time.sleep(1.0)

                twist.angular.z = turn_90
                self.publisher_.publish(twist)
                time.sleep(1.0)

            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.publisher_.publish(twist)
            time.sleep(3.0)

    def exit(self):
        self.get_logger().info("¡Salida encontrada! Finalizando ejecución.")
        self.destroy_node()
        rclpy.shutdown()