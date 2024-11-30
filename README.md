# MAGF-ID : Multiple and Gyro Free Inertial Dataset 
Here, you can find the dataset and code of the paper MAGF-ID : Multiple and Gyro Free Inertial Dataset

## Abstract

An inertial navigation system (INS) utilizes three orthogonal accelerometers and gyroscopes to determine platform position, velocity, and orientation. Inertial sensors can be found on various platforms such as vehicles, drones, and smartphones. They are used in numerous applications such as robotics, health, and the internet of things. Recent research explores the integration of data-driven methods with INS, highlighting significant progress and innovations, improving accuracy and efficiency. Despite the growing interest in this field and the availability of INS datasets, no datasets are available for the gyro-free INS (GFINS) and the multiple inertial measurement unit (MIMU). To fill this gap and to stimulate further research in this field, we designed and recorded GFINS and MIMU datasets using 54 inertial sensors grouped in nine inertial measurement units. These sensors can be used to define and evaluate different types of MIMU and GFINS architectures. The inertial sensors were arranged in three different sensor configurations and mounted on a mobile robot and a passenger car. For each configuration, four different dynamics were recorded, resulting in $115$ trajectories. In total, the dataset contains $35$ hours of inertial data and corresponding ground truth trajectories.

## Sensors Used

* Xsens DOTs - a low-cost IMU sensors. Eight to nine used in each experiment to produce the raw data.
* Inertial Labs MRU-P - a high-end IMU sensor that was used to record the GT.
* GNSS-RTK - an accurate positioning solution connected to the MRU-P that is licensed with the TerraStar-C Pro system.

## Platforms
* ROSbot XL - mobile robot by Hussarion company, it dimentions are 332 × 325 × 133.5 mm [L × W × H].
* Car - a private Ford Fiesta

<img src='https://github.com/ansfl/MAGF-ID/assets/101524872/39d797d1-f48b-4454-9e5e-ee677bcd5a4f' width='245'>
<img src='https://github.com/ansfl/MAGF-ID/assets/101524872/5cad46f7-841e-4d31-934d-65f928c6eb44' width='500'>


## Update 25/03/24
*Data and code will be available soon.*

If you find the paper, dataset or code helpful in your research, please cite our paper:
```
@article{yampolsky2024multiple,
  title={Multiple and Gyro-Free Inertial Datasets},
  author={Yampolsky, Zeev and Stolero, Yair and Pri-Hadash, Nitsan and Solodar, Dan and Massas, Shira and Savin, Itai and Klein, Itzik},
  journal={Scientific Data},
  volume={11},
  number={1},
  pages={1080},
  year={2024},
  publisher={Nature Publishing Group UK London}
}
```
