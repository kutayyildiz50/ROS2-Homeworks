from setuptools import find_packages, setup

package_name = 'fibonacci_action'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kutay',
    maintainer_email='kutay@todo.todo',
    description='Fibonacci action server and client',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = fibonacci_action.action_server:main',
            'client = fibonacci_action.action_client:main',
        ],
    },
)
