# [Obstacle] Control Interface Module

![Interface](https://user-images.githubusercontent.com/80487132/217883239-aec3fff5-06af-4fdc-b33b-e7b8296382a5.png)

## Summary

Simply run the script file
```
./install.sh
```
In the program directory.

Three options are possible to start the program
- In development mode
```
sudo python3 main.py --dev
```
- In demo mode
```
sudo python3 main.py --demo
```
- In demo fullscreen
```
sudo python3 main.py --fullscreen
```

Or you can start directly in development mode by the command
```
./run.sh
```

Otherwise, you can use the docker image
```
cd docker
./build.sh
./run.sh
```

The more important parameters could be changed in the ```config``` JSON file
