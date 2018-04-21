# Script generated with Bloom
pkgdesc="ROS - cob_control meta-package"
url='http://ros.org/wiki/cob_control'

pkgname='ros-kinetic-cob-control'
pkgver='0.7.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-cob-base-velocity-smoother'
'ros-kinetic-cob-cartesian-controller'
'ros-kinetic-cob-collision-velocity-filter'
'ros-kinetic-cob-control-mode-adapter'
'ros-kinetic-cob-control-msgs'
'ros-kinetic-cob-footprint-observer'
'ros-kinetic-cob-frame-tracker'
'ros-kinetic-cob-model-identifier'
'ros-kinetic-cob-obstacle-distance'
'ros-kinetic-cob-omni-drive-controller'
'ros-kinetic-cob-trajectory-controller'
'ros-kinetic-cob-twist-controller'
)

conflicts=()
replaces=()

_dir=cob_control
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_control $srcdir/cob_control
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

