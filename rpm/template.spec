Name:           ros-kinetic-cob-frame-tracker
Version:        0.7.1
Release:        0%{?dist}
Summary:        ROS cob_frame_tracker package

Group:          Development/Libraries
License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-cob-srvs
Requires:       ros-kinetic-control-toolbox
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-interactive-markers
Requires:       ros-kinetic-kdl-conversions
Requires:       ros-kinetic-kdl-parser
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-orocos-kdl
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslint
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cob-srvs
BuildRequires:  ros-kinetic-control-toolbox
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-interactive-markers
BuildRequires:  ros-kinetic-kdl-conversions
BuildRequires:  ros-kinetic-kdl-parser
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-orocos-kdl
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslint
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-visualization-msgs

%description
The cob_frame_tracker package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Jan 07 2018 Felix Messmer <fxm@ipa.fhg.de> - 0.7.1-0
- Autogenerated by Bloom

* Tue Jul 18 2017 Felix Messmer <fxm@ipa.fhg.de> - 0.7.0-0
- Autogenerated by Bloom

