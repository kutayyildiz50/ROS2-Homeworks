from py_pubsub.publisher_member_function import MinimalPublisher
from py_pubsub.subscriber_member_function import MinimalSubscriber
import rclpy
from std_msgs.msg import String


def test_publisher_and_subscriber():
    rclpy.init()

    publisher_node = MinimalPublisher()
    subscriber_node = MinimalSubscriber()

    received_messages = []

    def test_callback(msg):
        received_messages.append(msg.data)

    test_subscription = subscriber_node.create_subscription(
        String,
        'topic',
        test_callback,
        10
    )

    for _ in range(20):
        rclpy.spin_once(publisher_node, timeout_sec=0.1)
        rclpy.spin_once(subscriber_node, timeout_sec=0.1)

        if received_messages:
            break

    assert len(received_messages) > 0
    assert 'Hello World' in received_messages[0]

    subscriber_node.destroy_subscription(test_subscription)
    publisher_node.destroy_node()
    subscriber_node.destroy_node()

    rclpy.shutdown()
