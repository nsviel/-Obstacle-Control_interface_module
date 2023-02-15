# [Obstacle] Control Interface Module

### Interface in overview mode - System overview
![interface](https://user-images.githubusercontent.com/80487132/219006210-2c3af6c4-6d43-419f-b1b6-e4e7b6dadc1b.png)

### Interface in parametrization mode - Full system administration

![goc](https://user-images.githubusercontent.com/80487132/219006474-95940c39-7463-43ec-a713-f6e97296df4c.png)


## Installation and execution

<details><summary> ___ Installation ___ </summary>

Simply run the script file
```
./install.sh
```
In the program directory.

</details>
<details><summary> ___ Execution ___ </summary>

Three options are possible to start the program
- In parametrization mode
```
sudo python3 main.py --dev
```
- In overview mode
```
sudo python3 main.py --overview
```
- In overview and fullscreen mode
```
sudo python3 main.py --fullscreen
```

Or you can start directly in parametrization mode by the command
```
./run.sh
```

Otherwise, you can use the docker image
```
cd docker
./build.sh
./run.sh
```
</details>

The more important parameters could be changed in the ```config``` JSON file.

A manual switch between overview and parametrization mode can be made at runtime in the ```Menu``` and then ```mode``` onglet.
