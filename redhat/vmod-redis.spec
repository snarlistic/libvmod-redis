Summary: Redis VMOD for Varnish
Name: vmod-redis
Version: 0.3.3
Release: 1%{?dist}
License: BSD
URL: https://github.com/carlosabalde/libvmod-redis
Group: System Environment/Daemons
Source0: libvmod-redis.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish >= 4.1.0, hiredis >= 0.11.0
BuildRequires: make, python-docutils, varnish >= 4.1.0, varnish-libs-devel >= 4.1.0, hiredis-devel >= 0.11.0

%description
Redis VMOD for Varnish

%prep
%setup -n libvmod-redis

%build
./autogen.sh
./configure --prefix=/usr/ --docdir='${datarootdir}/doc/%{name}'
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} check

%install
[ %{buildroot} != "/" ] && %{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
[ %{buildroot} != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnish*/vmods/
%doc /usr/share/doc/%{name}/*
%{_mandir}/man?/*

%changelog
* Tue Dec 22 2015 Carlos Abalde <carlos.abalde@gmail.com> - 0.3.3-0.20151222
- Improvements & fixes.
* Mon Dec 21 2015 Carlos Abalde <carlos.abalde@gmail.com> - 0.3.2-0.20151221
- Added .stats().
* Wed Dec 16 2015 Carlos Abalde <carlos.abalde@gmail.com> - 0.3.1-0.20151216
- Removed support for server tags.
- Removed .add_cserver().
- Removed .server().
* Tue Dec 15 2015 Carlos Abalde <carlos.abalde@gmail.com> - 0.3.0-0.20151215
- Added support for multiple clusters.
- Added .retries().
- Removed redis.fini().
- Improved manual page.
* Mon Jun 08 2015 Carlos Abalde <carlos.abalde@gmail.com> - 0.2.7-0.20150608
- Fixed memory leak during redis.fini().
- Fixed initialization / reset of command execution timeout.
- Added Redis Cluster tests.
* Tue May 26 2015 Carlos Abalde <carlos.abalde@gmail.com> - 0.2.6-0.20150526
- Fixed bug when processing -MOVED and -ASK errors.
- Updated files borrowed from the Redis implementation.
* Tue May 12 2015 Carlos Abalde <carlos.abalde@gmail.com> - 0.2.5-0.20150512
- Do not require C99 standard.
* Thu Apr 17 2015 Carlos Abalde <carlos.abalde@gmail.com> - 0.2.4-0.20150417
- Added support for timeouts when executing commands.
- Maximum number of Redis Cluster hops is now configurable.
* Wed Jan 28 2015 Carlos Abalde <carlos.abalde@gmail.com> - 0.2.3-0.20150128
- Added support for hiredis 0.12.1 (redisEnableKeepAlive).
- Updated Redis Cluster key -> slot calculation.
* Fri Dec 19 2014 Carlos Abalde <carlos.abalde@gmail.com> - 0.2.2-0.20141219
- Added support for command retries.
* Wed Dec 17 2014 Carlos Abalde <carlos.abalde@gmail.com> - 0.2.1-0.20141217
- Added redis.replied().
- Minor fixes.
* Tue Dec 16 2014 Carlos Abalde <carlos.abalde@gmail.com> - 0.2.0-0.20141216
- Added Redis Cluster support.
- Minor improvements & fixes.
* Sun Dec 14 2014 Carlos Abalde <carlos.abalde@gmail.com> - 0.1.3-0.20141214
- Added support for shared pools of Redis connections.
- Refactor to simplify future support of Redis Cluster.
* Thu Oct 23 2014 Carlos Abalde <carlos.abalde@gmail.com> - 0.1.2-0.20141023
- Discard Redis contexts when connections are hung up by the server.
* Wed Sep 17 2014 Carlos Abalde <carlos.abalde@gmail.com> - 0.1.1-0.20140917
- Added missing WS_Dup()'s / WS_Copy()'s.
* Fri Aug 22 2014 Carlos Abalde <carlos.abalde@gmail.com> - 0.1-0.20140822
- Initial version.
