Name:           ros-indigo-gazebo-ros-pkgs
Version:        2.4.6
Release:        0%{?dist}
Summary:        ROS gazebo_ros_pkgs package

Group:          Development/Libraries
License:        BSD,LGPL,Apache 2.0
URL:            http://gazebosim.org/wiki/Tutorials#ROS_Integration
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-gazebo-msgs
Requires:       ros-indigo-gazebo-plugins
Requires:       ros-indigo-gazebo-ros
BuildRequires:  ros-indigo-catkin

%description
Interface for using ROS with the Gazebo simulator.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Sep 01 2014 John Hsu <hsu@osrfoundation.org> - 2.4.6-0
- Autogenerated by Bloom

* Mon Aug 18 2014 John Hsu <hsu@osrfoundation.org> - 2.4.5-1
- Autogenerated by Bloom

* Mon Aug 18 2014 John Hsu <hsu@osrfoundation.org> - 2.4.5-0
- Autogenerated by Bloom

