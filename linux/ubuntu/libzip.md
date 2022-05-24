# libzip 

~~~bash
#!/bin/bash
VER=$1
echo $VER
if [ -n "$VER" ]; then
    mkdir /tmp/libzip
    cd /tmp/libzip
    curl -sSLO https://libzip.org/download/libzip-$VER.tar.gz
    tar zxf libzip-$VER.tar.gz
    cd libzip-$VER/
    mkdir build
    cd build
    cmake ../
    make > /dev/null
    sudo make install
fi
~~~