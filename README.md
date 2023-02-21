# [Obstacle] Control Interface Module

A GUI which allows to control the entire system parameters and LiDAR state. A visual data and module representation which colored connection links permits to get a constant overall indicator of the system correct functioning.

![interface](https://user-images.githubusercontent.com/80487132/220367992-841cc94d-d435-4f4b-b6bd-a337ed361d89.png)

## Screenshot

<details><summary>Interface in overview mode</summary>

![interface](https://user-images.githubusercontent.com/80487132/219006210-2c3af6c4-6d43-419f-b1b6-e4e7b6dadc1b.png)

</details>

<details><summary>Interface in parametrization mode</summary>

![goc](https://user-images.githubusercontent.com/80487132/219006474-95940c39-7463-43ec-a713-f6e97296df4c.png)

</details>


## Documentation
<details><summary>Installation and execution</summary>

To install dependencies, simply run the script file
```
./install.sh
```
in the program directory.
Three options are possible to start the program:
- In parametrization mode
```
sudo python3 main.py --param
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

:warning: root privileges are required

</details>
<details><summary>Docker</summary>

You can use a docker image with:

```
cd docker
./build.sh
./run.sh
```

</details>

<details><summary>General</summary>

- The more important parameters could be changed in the ```config``` JSON file.

- A manual switch between overview and parametrization mode can be made at runtime in the ```Menu``` and then ```mode``` tab.

- At system start, when all systems are initialized a small configuration step is generally necessary. For example, setting the different IP for each component have to be done either in the ```config``` file or directly on the interface.

- A file, ```wallet.txt``` file in the ```src``` folder, is responsible for listing and keeping IP addresses. Adding new one or delete old one is possible either by modifying directly the file or on the interface on the Wallet menu.

</details>

## System

Full system repository ( [link](https://github.com/nsviel/Obstacle_detection_system) )
- [ ] Data acquisition module ( [link](https://github.com/nsviel/-Obstacle-Data_acquisition_module) )
- [ ] Edge server module
  - [ ] Edge orchestrator component ( [link](https://github.com/nsviel/-Obstacle-Edge_orchestrator_component) )
  - [ ] Data processing component ( [link](https://github.com/nsviel/-Obstacle-Data_processing_component) )
  - [ ] AI component
- [x] Control interface module
