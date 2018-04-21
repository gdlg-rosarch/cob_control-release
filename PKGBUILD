# Script generated with Bloom
pkgdesc="ROS - The cob_obstacle_distance package"


pkgname='ros-kinetic-cob-obstacle-distance'
pkgver='0.7.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('assimp'
'boost'
'eigen3'
'fcl'
'pkg-config'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-cob-control-msgs'
'ros-kinetic-cob-srvs'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-eigen-conversions'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kdl-conversions'
'ros-kinetic-kdl-parser'
'ros-kinetic-moveit-msgs'
'ros-kinetic-orocos-kdl'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-roslint'
'ros-kinetic-sensor-msgs'
'ros-kinetic-shape-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
)

depends=('assimp'
'boost'
'eigen3'
'fcl'
'pkg-config'
'ros-kinetic-cmake-modules'
'ros-kinetic-cob-control-msgs'
'ros-kinetic-cob-srvs'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-eigen-conversions'
'ros-kinetic-geometry-msgs'
'ros-kinetic-interactive-markers'
'ros-kinetic-joint-state-publisher'
'ros-kinetic-kdl-conversions'
'ros-kinetic-kdl-parser'
'ros-kinetic-moveit-msgs'
'ros-kinetic-orocos-kdl'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-roslint'
'ros-kinetic-rospy'
'ros-kinetic-rviz'
'ros-kinetic-sensor-msgs'
'ros-kinetic-shape-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=cob_obstacle_distance
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_obstacle_distance $srcdir/cob_obstacle_distance
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

