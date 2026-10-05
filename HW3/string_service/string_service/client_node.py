import sys

import rclpy
from rclpy.node import Node

from string_interfaces.srv import CompareStrings


class StringClient(Node):

    def __init__(self):
        super().__init__('string_client')
        self.client = self.create_client(CompareStrings, 'compare_strings')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service waiting...')

    def send_request(self, first_string, second_string):
        request = CompareStrings.Request()
        request.first_string = first_string
        request.second_string = second_string

        return self.client.call_async(request)


def main(args=None):
    rclpy.init(args=args)

    node = StringClient()

    future = node.send_request(sys.argv[1], sys.argv[2])
    rclpy.spin_until_future_complete(node, future)

    response = future.result()

    node.get_logger().info(
        'Result: %s' % response.equal
    )

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
