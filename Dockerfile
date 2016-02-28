#
# RpmBuildMapnik
#

FROM centos:7
MAINTAINER "Dirk Stichling" <mytracks@mytracks4mac.com>

# Change root password
RUN echo "root:admin" | chpasswd

RUN yum install -y epel-release \
&& rpm -ivh http://yum.postgresql.org/9.5/redhat/rhel-7-x86_64/pgdg-centos95-9.5-2.noarch.rpm \
&& yum install -y rpmdevtools rpmlint bzip2 make gcc-c++ sqlite-devel proj-devel libjpeg-turbo-devel libtiff-devel libwebp-devel postgis2_95-devel postgresql95-devel libpqxx-devel gcc-c++ harfbuzz-devel gdal-devel cairo-devel boost-devel \
&& rpmdev-setuptree \
&& cd ~/rpmbuild/SOURCES/ \
&& curl -O https://mapnik.s3.amazonaws.com/dist/v3.0.9/mapnik-v3.0.9.tar.bz2 \
&& tar jxf mapnik-v3.0.9.tar.bz2 \
&& mv mapnik-v3.0.9 mapnik-3.0.9 \
&& tar jcf mapnik-3.0.9.tar.bz2 mapnik-3.0.9 \
&& rm mapnik-v3.0.9.tar.bz2

COPY mapnik-3.0.9.spec /home/root/rpmbuild/SPECS/

RUN cd ~/rpmbuild/SPECS \
&& rpmbuild -ba mapnik-3.0.9.spec

