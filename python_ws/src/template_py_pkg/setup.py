"""
--------------------------------------------------------------------------------
This is a template setup file for a ROS2 Python package.
It defines package metadata, install behavior, and executable node entry points.
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Use this file to:
1. Register Python modules in the package
2. Install package resources (resource index + package.xml)
3. Define runtime/test dependencies
4. Register ROS2 node executables using console_scripts
--------------------------------------------------------------------------------
"""

from setuptools import find_packages, setup

package_name = 'template_py_pkg'

setup(
    # Package name/version should match package.xml unless intentionally different.
    name=package_name,
    version='0.0.0',

    #--------------------------------------------------------------------------------
    # Python modules inside this package.
    #
    # find_packages will include folders that contain __init__.py.
    # Exclude test folders so they are not installed as runtime modules.
    #--------------------------------------------------------------------------------
    packages=find_packages(exclude=['test']),

    #--------------------------------------------------------------------------------
    # Files installed into the ament index and package share directory.
    #
    # resource/<package_name>:
    #   Required by ROS2 tooling so the package is discoverable.
    # package.xml:
    #   Installed so metadata is available after build/install.
    #--------------------------------------------------------------------------------
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],

    #--------------------------------------------------------------------------------
    # Runtime dependencies for pip-style package installation.
    # Note: ROS dependencies are primarily declared in package.xml.
    #--------------------------------------------------------------------------------
    install_requires=['setuptools'],
    zip_safe=True,

    # Package ownership and package-level metadata.
    maintainer='raven',
    maintainer_email='raven.hollick@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',

    #--------------------------------------------------------------------------------
    # Optional dependencies for development/testing.
    #--------------------------------------------------------------------------------
    extras_require={
        'test': [
            'pytest',
        ],
    },

    #--------------------------------------------------------------------------------
    # ROS2 executable entry points.
    #
    # Format:
    # '<executable_name> = <python_module>:<main_function>'
    #
    # Add additional nodes here as you create new Python entry-point files.
    # Example:
    # 'listener_node = template_py_pkg.listener_node:main'
    #--------------------------------------------------------------------------------
    entry_points={
        'console_scripts': [
            'node_name = template_py_pkg.node_name:main',
        ],
    },
)
