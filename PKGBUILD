# Script generated with Bloom
pkgdesc="ROS - The main purpose of the cob_twist_controller is to convert target twists into joint velocities. Therefore it makes use of several implemented inverse kinematics approaches at the first order differential level. The inverse differential kinematics solver considers kinematic chain extensions, singularity robustness, redundancy resolution and priority-based methods. To avoid hardware destruction there is a limiter interface active as well. Via parameter server users can dynamically configure the solving strategy."


pkgname='ros-kinetic-cob-twist-controller'
pkgver='0.7.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('boost'
'eigen3'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-cob-control-msgs'
'ros-kinetic-cob-srvs'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-eigen-conversions'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kdl-conversions'
'ros-kinetic-kdl-parser'
'ros-kinetic-nav-msgs'
'ros-kinetic-orocos-kdl'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-roslint'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
)

depends=('boost'
'eigen3'
'ros-kinetic-cmake-modules'
'ros-kinetic-cob-control-msgs'
'ros-kinetic-cob-frame-tracker'
'ros-kinetic-cob-srvs'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-eigen-conversions'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kdl-conversions'
'ros-kinetic-kdl-parser'
'ros-kinetic-nav-msgs'
'ros-kinetic-orocos-kdl'
'ros-kinetic-pluginlib'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-rviz'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-topic-tools'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=cob_twist_controller
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_twist_controller $srcdir/cob_twist_controller
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

