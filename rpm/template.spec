%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ros2controlcli
Version:        3.1.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2controlcli package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-pygraphviz
Requires:       ros-rolling-controller-manager
Requires:       ros-rolling-controller-manager-msgs
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-ros2cli
Requires:       ros-rolling-ros2node
Requires:       ros-rolling-ros2param
Requires:       ros-rolling-rosidl-runtime-py
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ament-copyright
BuildRequires:  ros-rolling-ament-flake8
BuildRequires:  ros-rolling-ament-pep257
BuildRequires:  ros-rolling-ament-xmllint
BuildRequires:  ros-rolling-controller-manager
BuildRequires:  ros-rolling-controller-manager-msgs
BuildRequires:  ros-rolling-rclpy
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ros2cli
BuildRequires:  ros-rolling-ros2node
BuildRequires:  ros-rolling-ros2param
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The ROS 2 command line tools for ROS2 Control.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Oct 05 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.1.0-1
- Autogenerated by Bloom

* Mon Sep 19 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.0.0-1
- Autogenerated by Bloom

* Mon Sep 19 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.15.0-1
- Autogenerated by Bloom

* Wed Aug 03 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.13.0-1
- Autogenerated by Bloom

* Thu Jul 14 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.12.1-1
- Autogenerated by Bloom

* Sat Jul 09 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.12.0-1
- Autogenerated by Bloom

* Sun Jul 03 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.11.0-1
- Autogenerated by Bloom

* Sat Jun 18 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.10.0-1
- Autogenerated by Bloom

* Thu May 19 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.9.0-1
- Autogenerated by Bloom

* Fri May 13 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.8.0-1
- Autogenerated by Bloom

* Fri Apr 29 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.7.0-1
- Autogenerated by Bloom

* Wed Apr 20 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.6.0-1
- Autogenerated by Bloom

* Fri Mar 25 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.5.0-1
- Autogenerated by Bloom

* Wed Feb 23 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.4.0-1
- Autogenerated by Bloom

* Fri Feb 18 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.3.0-1
- Autogenerated by Bloom

* Wed Feb 09 2022 Victor Lopez <victor.lopez@pal-robotics.com> - 2.1.0-3
- Autogenerated by Bloom

