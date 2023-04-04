#!/bin/sh

xhost + >/dev/null
sudo docker run \
    --network host \
    -it \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="/media/aeter/lidar_ssd:/app/lidar_ssd" \
    --device="/dev/dri:/dev/dri" \
    --env=DISPLAY=$DISPLAY \
    -p 321:321 \
    -p 322:322 \
    interface
xhost - >/dev/null
