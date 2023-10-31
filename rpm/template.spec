%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rqt-controller-manager
Version:        3.20.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt_controller_manager package

License:        Apache License 2.0
URL:            http://ros.org/wiki/rqt_controller_manager
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-controller-manager-msgs
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-rqt-gui
Requires:       ros-rolling-rqt-gui-py
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Graphical frontend for interacting with the controller manager.

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
* Tue Oct 31 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.20.0-1
- Autogenerated by Bloom

* Wed Oct 04 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.19.1-1
- Autogenerated by Bloom

* Tue Oct 03 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.19.0-1
- Autogenerated by Bloom

* Thu Aug 17 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.18.0-1
- Autogenerated by Bloom

* Mon Aug 07 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.17.0-1
- Autogenerated by Bloom

* Sun Jul 09 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.16.0-1
- Autogenerated by Bloom

* Fri Jun 23 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.15.0-1
- Autogenerated by Bloom

* Wed Jun 14 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.14.0-1
- Autogenerated by Bloom

* Thu May 18 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.13.0-1
- Autogenerated by Bloom

* Sat Apr 29 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.12.2-1
- Autogenerated by Bloom

* Fri Apr 14 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.12.1-1
- Autogenerated by Bloom

* Sun Apr 02 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.12.0-1
- Autogenerated by Bloom

* Tue Mar 28 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.11.0-2
- Autogenerated by Bloom

* Tue Mar 21 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.10.0-2
- Autogenerated by Bloom

