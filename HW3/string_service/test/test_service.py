import rclpy

from string_interfaces.srv import CompareStrings
from string_service.server_node import StringServer


def test_string_service():
    rclpy.init()

    server_node = StringServer()

    request = CompareStrings.Request()
    response = CompareStrings.Response()

    request.first_string = 'Hello'
    request.second_string = 'HELLO'

    result = server_node.compare_strings_callback(request, response)

    assert result.equal is True

    request.first_string = 'Hello'
    request.second_string = 'World'

    response = CompareStrings.Response()
    result = server_node.compare_strings_callback(request, response)

    assert result.equal is False

    server_node.destroy_node()
    rclpy.shutdown()
