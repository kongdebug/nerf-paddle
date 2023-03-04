# NeRF-Paddle

**神经辐射场 (Neural Radiance Field, NERF)**是发表在ECCV 2020上的谷歌和伯克利大学的研究，只需要**少量的静态图像**，就能通过[NeRF]([http://www.matthewtancik.com/nerf])生成**多视角的逼真3D效果**，提供的训练权重渲染效果如下所示：
![](https://user-images.githubusercontent.com/7057863/78472232-cf374a00-7769-11ea-8871-0bc710951839.gif)
![](https://user-images.githubusercontent.com/7057863/78472235-d1010d80-7769-11ea-9be9-51365180e063.gif)


本项目是Paddle版本的NeRF，目前支持`blander`与`LIIF`两种数据格式的训练，其中在`NeRF_Synthetic`数据集上训练**达到论文精度**，训练与渲染速度与torch版本相差不大，较原论文快1.3倍。代码参考了torch版本的NeRF仓库[nerf-pytorch](https://github.com/yenchenlin/nerf-pytorch)，感谢其开源为本项目的建设提供便利

## 1. 安装

你可以根据如下步骤安装`NeRF-Paddle`:
- [PaddlePaddle安装](https://www.paddlepaddle.org.cn/install/quick)
    - 版本要求：PaddlePaddle>=2.2.0, Python>=3.7
- NeRF-Paddle安装，通过以下命令

```
git clone https://github.com/kongdebug/nerf-paddle
cd nerf-paddle
pip install -r requirements.txt
```
## 2. 数据集准备

[NeRF_Synthetic](https://aistudio.baidu.com/aistudio/datasetdetail/136816)数据集已上传至AI Studio, 同时也为快速入门准备了2个场景的示例数据集[NeRF_example](https://aistudio.baidu.com/aistudio/datasetdetail/136989)。新建`data`文件夹，将数据集下载并解压后放于该文件夹下，准备好的数据组织形式如下：

```
nerf-paddle/data
├── nerf_llff_data
│   └── fern
└── nerf_synthetic
    └── lego
```

## 3. 快速开始

### 3.1 训练Lego数据

- 运行以下命令行，对低解析度的`Lego`数据进行训练

```
python run_nerf.py --config configs/lego.txt
```
- 在训练了200k iterations (大概7.5小时)之后，训练结果如下所示：

![](https://ai-studio-static-online.cdn.bcebos.com/eafc2ee397574bf0bc1975c782652a653b77e70371804f6795fbe76bab4127f4)

### 3.2 训练Fern数据

- 运行以下命令行，对低解析度的、真实场景的`Fern`数据进行训练

```
python run_nerf.py --config configs/fern.txt
```

- 在训练了200k iterations (大概5.5小时)之后，训练结果如下所示：

| rgb | disp|
|---|---|
|![](https://ai-studio-static-online.cdn.bcebos.com/f1273af09f3f432f9bf28b6a38d687ed4c929012f89148749663d0ea68a734c5) | ![](https://ai-studio-static-online.cdn.bcebos.com/ca7290f35085460fb323de6703b57134b533e6a9a11546caaef7f62fdb62ec6c) |

**注** ：更详细与便利的使用教程已在[AI Studio](https://aistudio.baidu.com/aistudio/projectdetail/3792428)上发布，fork该项目即可快速体验

## 4. 复现精度

- 使用本项目对`NeRF_Synthetic`数据集进行训练，配置文件在`paper_configs`文件夹下，得到的PSNR结果如下表所示， 平均PSNR相对论文提高了0.54dB

|Framework | Chair | Drums | Ficus | Hotdog | Lego | Materials | Mic | Ship | Avg PSNR |
|--- | --- |--- |--- | --- |--- |--- | --- | --- | --- |
| Paper-Tensorflow  |33.00|25.01|30.13|36.18|32.54|29.62|32.91|28.65| 31.01|
| Ours-Paddle | 32.78 | 26.11| 30.62| 36.54 |33.19 |30.24 | 33.11 |29.80| 31.55 |

- 以上模型训练的日志文件已上传至[百度云](https://pan.baidu.com/s/1SAxiI9UvmTR3IignkTRKVg)，提取码：l7qs 。使用vdl查看日志运行以下命令，可将 `{DATASET}` 替换为 `ship` | `hotdog` | `ficus` | `mic` | `lego` | 等：

```
python visualize_log.py --log_dir nerf_log/{DATASET}_summaries
```

- 由于正在建设Paddle官方的渲染库，预训练权重暂不开源，等NeRF合入该仓库之后再给出对应权重



