# [Obstacle] Control Interface Module

A GUI which allows to control the entire system parameters and LiDAR state. A visual data and module representation which colored connection links permits to get a constant overall indicator of the system correct functioning.

![interface](https://user-images.githubusercontent.com/80487132/220367992-841cc94d-d435-4f4b-b6bd-a337ed361d89.png)

## Documentation
<details><summary>Installation and execution</summary>

To install dependencies, simply run the script file
```
./install.sh
```
in the program directory.
To start the program:
```
sudo python3 main.py
```
Or
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
