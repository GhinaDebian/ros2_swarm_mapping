import os

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    ld = LaunchDescription()
    config = os.path.join(
        get_package_share_directory("explore_lite"), "config", "params.yaml"
    )
    use_sim_time = LaunchConfiguration("use_sim_time")
    namespace = LaunchConfiguration("namespace")
    min_frontier_size = LaunchConfiguration("min_frontier_size")

    declare_use_sim_time_argument = DeclareLaunchArgument(
        "use_sim_time", default_value="true", description="Use simulation/Gazebo clock"
    )
    declare_namespace_argument = DeclareLaunchArgument(
        "namespace",
        default_value="",
        description="Namespace for the explore node",
    )
    declare_min_frontier_size_argument = DeclareLaunchArgument(
        "min_frontier_size",
        default_value="0.75",
        description="Minimum size of the frontier to be considered",
    )

    # Map fully qualified names to relative ones so the node's namespace can be prepended.
    # In case of the transforms (tf), currently, there doesn't seem to be a better alternative
    # https://github.com/ros/geometry2/issues/32
    # https://github.com/ros/robot_state_publisher/pull/30
    remappings = [("/tf", "tf"), ("/tf_static", "tf_static")]

    node = Node(
        package="explore_lite",
        name="explore_node",
        namespace=namespace,
        executable="explore",
        parameters=[config, {"use_sim_time": use_sim_time}, {"min_frontier_size": min_frontier_size}],
        output="screen",
        remappings=remappings,
    )
    ld.add_action(declare_use_sim_time_argument)
    ld.add_action(declare_namespace_argument)
    ld.add_action(declare_min_frontier_size_argument)
    ld.add_action(node)
    return ld
