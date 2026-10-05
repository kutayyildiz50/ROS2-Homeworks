from setuptools import find_packages, setup

package_name = 'string_service'

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
    maintainer_email='yildizkutay35@hotmail.com',
    description='ROS2 string comparison service',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = string_service.server_node:main',
            'client = string_service.client_node:main',
        ],
    },
)
