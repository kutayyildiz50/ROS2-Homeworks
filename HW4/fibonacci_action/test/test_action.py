from fibonacci_action.action_server import FibonacciActionServer
import rclpy


def test_fibonacci_function():
    rclpy.init()

    server_node = FibonacciActionServer()

    assert server_node.is_fibonacci(5) is True
    assert server_node.is_fibonacci(8) is True
    assert server_node.is_fibonacci(13) is True

    assert server_node.is_fibonacci(4) is False
    assert server_node.is_fibonacci(6) is False
    assert server_node.is_fibonacci(10) is False

    server_node.destroy_node()
    rclpy.shutdown()
