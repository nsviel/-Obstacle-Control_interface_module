#!/bin/sh

xhost + >/dev/null
sudo docker run \
    -it \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --device="/dev/dri:/dev/dri" \
    --env=DISPLAY=$DISPLAY \
    -p 321:321 \
    -p 322:322 \
    controlium
xhost - >/dev/null
