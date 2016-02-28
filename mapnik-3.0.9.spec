# export QA_RPATHS=0x0003; rpmbuild -ba mapnik-3.0.9.spec

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
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/include
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
cp /usr/local/lib/libmapnik-json.a $RPM_BUILD_ROOT/usr/local/lib/
cp /usr/local/lib/libmapnik-wkt.a $RPM_BUILD_ROOT/usr/local/lib/
cp /usr/local/lib/libmapnik.so.3.0.9 $RPM_BUILD_ROOT/usr/local/lib/
cp -R /usr/local/include/mapnik $RPM_BUILD_ROOT/usr/local/include/
cp -R /usr/local/lib/mapnik $RPM_BUILD_ROOT/usr/local/lib/
cp /usr/local/bin/mapnik-config $RPM_BUILD_ROOT/usr/local/bin
cp /usr/local/bin/mapnik-index $RPM_BUILD_ROOT/usr/local/bin
cp /usr/local/bin/mapnik-render $RPM_BUILD_ROOT/usr/local/bin
cp /usr/local/bin/shapeindex $RPM_BUILD_ROOT/usr/local/bin
cd $RPM_BUILD_ROOT/usr/local/lib/
ln -s libmapnik.so.3.0.9 libmapnik.so.3.0
ln -s libmapnik.so.3.0.9 libmapnik.so

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
