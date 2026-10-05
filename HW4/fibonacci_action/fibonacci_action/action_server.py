from fibonacci_interfaces.action import FindFibonacci
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node


class FibonacciActionServer(Node):

    def __init__(self):
        super().__init__('fibonacci_action_server')

        self._action_server = ActionServer(
            self,
            FindFibonacci,
            'find_fibonacci',
            self.execute_callback
        )

    def is_fibonacci(self, n):
        if n < 0:
            return False

        a, b = 0, 1

        while a < n:
            a, b = b, a + b

        return a == n

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        numbers = goal_handle.request.numbers
        flags = []

        feedback_msg = FindFibonacci.Feedback()

        for number in numbers:
            if self.is_fibonacci(number):
                flags.append(True)

                feedback_msg.fibonacci_number = number
                goal_handle.publish_feedback(feedback_msg)

                self.get_logger().info(
                    'Fibonacci number found: %d' % number
                )
            else:
                flags.append(False)

        goal_handle.succeed()

        result = FindFibonacci.Result()
        result.flags = flags

        self.get_logger().info('Goal completed.')

        return result


def main(args=None):
    rclpy.init(args=args)

    action_server = FibonacciActionServer()

    rclpy.spin(action_server)

    action_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
