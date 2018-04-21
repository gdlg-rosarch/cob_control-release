# Script generated with Bloom
pkgdesc="ROS - The cob_footprint_observer package adjusts the footprint of the robot based on the setup (e.g. arm and/or tray)."
url='http://ros.org/wiki/cob_footprint_observer'

pkgname='ros-kinetic-cob-footprint-observer'
pkgver='0.7.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('boost'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-generation'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

depends=('boost'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=cob_footprint_observer
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_footprint_observer $srcdir/cob_footprint_observer
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

