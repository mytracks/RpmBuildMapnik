%define  debug_package %{nil}

Name:           mapnik
Version:        3.0.9
Release:        1%{?dist}
Summary:        mapnik.org library

License:        LGPL
URL:            http://www.mapnik.org
Source0:        mapnik-3.0.9.tar.bz2

BuildRequires:  epel-release make gcc-c++ sqlite-devel proj-devel libjpeg-turbo-devel libtiff-devel libwebp-devel postgis2_95-devel postgresql95-devel libpqxx-devel gcc-c++ harfbuzz-devel gdal-devel cairo-devel boost-devel
Requires:       epel-release proj sqlite libjpeg-turbo libtiff libwebp postgresql95 postgis2_95 postgresql95 libpqxx harfbuzz gdal cairo boost

%description


%prep
%setup -q


%build
%configure PG_CONFIG=/usr/pgsql-9.5/bin/pg_config
make %{?_smp_mflags}


%install
#rm -rf $RPM_BUILD_ROOT
%make_install


%files
/usr/local/lib/libmapnik-json.a
/usr/local/lib/libmapnik-wkt.a
/usr/local/lib/libmapnik.so.3.0.9
/usr/local/lib/libmapnik.so.3.0
/usr/local/lib/libmapnik.so
/usr/local/include/mapnik
/usr/local/lib/mapnik
/usr/local/bin/mapnik-config
/usr/local/bin/mapnik-index
/usr/local/bin/mapnik-render
/usr/local/bin/shapeindex


%changelog
