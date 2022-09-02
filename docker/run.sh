#!/bin/sh

xhost +
sudo docker run \
    -it \
    --network host \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --device="/dev/dri:/dev/dri" \
    --env=DISPLAY=$DISPLAY \
    controlium
xhost -


