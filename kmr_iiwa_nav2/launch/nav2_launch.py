import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from ros_gz_bridge.actions import RosGzBridge
from ros_gz_sim.actions import GzServer


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    pkg_project = get_package_share_directory('kmr_iiwa_nav2')

    # Get the launch directory
    slam_toolbox_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(pkg_project + '/launch/online_async_launch.py'),
        launch_arguments={
            #'namespace': 'kmr_iiwa',
            'use_sim_time': use_sim_time,
            'slam_params_file': os.path.join(pkg_project, 'config', 'mapper_online_params_online_async.yaml'),
            }.items()
    )

    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    nav2_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_bringup_dir + '/launch/bringup_launch.py'),
        launch_arguments={
            #'namespace': 'kmr_iiwa',
            #'use_namespace': 'True',
            'use_sim_time': use_sim_time,
            'use_localization': 'False', #since we are using slam_toolbox for localization
            'use_keepout_zones': 'False',
            'use_speed_zones': 'False',
            'params_file': os.path.join(pkg_project, 'config', 'nav2_params.yaml'),
            }.items()
    )

    # nav2_costmap_2d_markers_node = Node(
    #     package='nav2_costmap_2d',
    #     executable='nav2_costmap_2d_markers',
    #     name='nav2_costmap_2d_markers',
    #     output='screen',
    #     parameters=[{
    #         'voxel_grid': '/local_costmap/voxel_grid',
    #         'visualization_marker': '/local_costmap/obstacle_markers'
    #     }]
    # )

    return LaunchDescription([
        DeclareLaunchArgument(name='use_sim_time', default_value='True', description='Flag to enable use_sim_time'),
        slam_toolbox_launch,
        nav2_bringup_launch,   
        #nav2_costmap_2d_markers_node
    ])