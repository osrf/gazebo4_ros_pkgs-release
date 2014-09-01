Name:           ros-hydro-gazebo-ros
Version:        2.3.7
Release:        0%{?dist}
Summary:        ROS gazebo_ros package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://gazebosim.org/wiki/Tutorials#ROS_Integration
Source0:        %{name}-%{version}.tar.gz

Requires:       gazebo-devel
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-gazebo-msgs
Requires:       ros-hydro-gazebo-plugins
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-message-generation
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rosgraph-msgs
Requires:       ros-hydro-roslib
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-std-srvs
Requires:       ros-hydro-tf
Requires:       tinyxml-devel
BuildRequires:  gazebo-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-gazebo-msgs
BuildRequires:  ros-hydro-gazebo-plugins
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rosgraph-msgs
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-std-srvs
BuildRequires:  ros-hydro-tf
BuildRequires:  tinyxml-devel

%description
Provides ROS plugins that offer message and service publishers for interfacing
with Gazebo through ROS. Formally simulator_gazebo/gazebo

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Sep 01 2014 John Hsu <hsu@osrfoundation.org> - 2.3.7-0
- Autogenerated by Bloom

* Mon Aug 18 2014 John Hsu <hsu@osrfoundation.org> - 2.3.6-1
- Autogenerated by Bloom

* Mon Aug 18 2014 John Hsu <hsu@osrfoundation.org> - 2.3.6-0
- Autogenerated by Bloom

