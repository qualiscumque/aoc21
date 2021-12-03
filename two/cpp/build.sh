#!/bin/bash
rm -fr build && mkdir build
pushd build
cmake ..
make
./two_a
popd
