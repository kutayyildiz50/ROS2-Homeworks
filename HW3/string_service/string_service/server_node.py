import rclpy
from rclpy.node import Node

from string_interfaces.srv import CompareStrings


class StringServer(Node):

    def __init__(self):
        super().__init__('string_server')
        self.srv = self.create_service(
            CompareStrings,
            'compare_strings',
            self.compare_strings_callback
        )

    def compare_strings_callback(self, request, response):
        response.equal = request.first_string.lower() == request.second_string.lower()

        self.get_logger().info(
            'Comparing: "%s" and "%s" -> %s' %
            (request.first_string, request.second_string, response.equal)
        )

        return response


def main(args=None):
    rclpy.init(args=args)

    node = StringServer()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
