import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, termios, tty
#made with assistance from chatgpt
class DriveRobot(Node):
    def __init__(self):
        super().__init__('drive_robot')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.get_logger().info("Robot Driver node Initialized. Use WASD keys to move the robot. Press 'q' to quit, or any other key to stop.")

    def get_key(self): #gets key pressed
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

    def main_loop(self):
        move_bindings = { #translates keys pressed to coordinates
            'w': (1, 0), #forward
            's': (-1, 0), #backward
            'a': (0, 1), #turn left
            'd': (0, -1), #turn right
        }

        speed = 0.5
        turn = 1.0

        while True:
            key = self.get_key()

            if key in move_bindings.keys():
                print(key)
                linear, angular = move_bindings[key]
                twist = Twist()
                twist.linear.x = linear * speed
                twist.angular.z = angular * turn
                self.publisher_.publish(twist)
            elif key == 'q': #stop node
                break

            else:
                twist = Twist() #on other keys send empty Twist, stops robot
                self.publisher_.publish(twist)

def main(args=None):
    global settings
    settings = termios.tcgetattr(sys.stdin)

    rclpy.init(args=args)
    DR_node = DriveRobot()

    try:
        DR_node.main_loop()
    except Exception as e:
        DR_node.get_logger().info(f"Exception: {e}")
    finally:
        DR_node.destroy_node()
        rclpy.shutdown()
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

if __name__ == '__main__':
    main()
