import sys

from fibonacci_interfaces.action import FindFibonacci
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')

        self._action_client = ActionClient(
            self,
            FindFibonacci,
            'find_fibonacci'
        )

    def send_goal(self, numbers):
        goal_msg = FindFibonacci.Goal()
        goal_msg.numbers = numbers

        self._action_client.wait_for_server()

        self.get_logger().info(
            'Sending numbers: %s' % numbers
        )

        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )

        self._send_goal_future.add_done_callback(
            self.goal_response_callback
        )

    def goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            rclpy.shutdown()
            return

        self.get_logger().info('Goal accepted')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(
            self.get_result_callback
        )

    def feedback_callback(self, feedback_msg):
        number = feedback_msg.feedback.fibonacci_number

        self.get_logger().info(
            'Feedback - Fibonacci number: %d' % number
        )

    def get_result_callback(self, future):
        result = future.result().result

        self.get_logger().info(
            'Result flags: %s' % list(result.flags)
        )

        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)

    action_client = FibonacciActionClient()

    if len(sys.argv) < 2:
        action_client.get_logger().error(
            'Enter numbers. Example: 4 5 6 8'
        )
        rclpy.shutdown()
        return

    numbers = [int(x) for x in sys.argv[1:]]

    action_client.send_goal(numbers)

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
