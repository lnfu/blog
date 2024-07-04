+++
title = 'Python 踩雷'
date = 2024-07-04T03:53:53Z
draft = false
+++

這一篇會紀錄我使用 Python 時遇到各種大大小小的問題。

## opencv-python 版本

opencv-python 的版本要和 Python 的版本對應。可以參考[清華大學的鏡像站](https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/opencv-python/)，cp36 指的是 Python 版本 3.6，前面的版本就是 opencv-python 的版本。

## tensorflow-gpu、CUDA、cudnn

不要想在 Windows 上面跑! (至少我遇到一堆問題...)

如果要跑舊版的 tensorflow (舊版 CUDA)，用 conda (我是用 Miniconda) 會很方便，也不需要自己安裝 CUDA 和 cudnn。

```sh
conda create -n py36 python=3.6
conda activate py36
conda install tensorflow-gpu=1.15.0
```

如果真的想不開要自己裝 CUDA 和 cudnn 的話，記得版本要和 tensorflow 對應 (參考[這個表格](https://www.tensorflow.org/install/source#gpu))。

安裝完後可以用以下程式碼來確認。

```py3
import tensorflow as tf
print(tf.config.experimental.list_physical_devices('GPU'))
```
