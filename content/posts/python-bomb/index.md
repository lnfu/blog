+++
title = 'Python 踩雷'
date = 2024-07-04T03:53:53Z
draft = false
tags = ['Python']
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

## conda 內無法使用 OpenGL 和 EGL

原本一直以為是我沒有成功安裝 OpenGL 和 EGL 相關的套件。

```sh
sudo apt-get install libegl1-mesa-dev
```

後來發現在 conda base 環境是可以跑的，`/usr/include` 也有 GL 和 EGL 的目錄，所以是 conda 的問題。

但是依然不知道為什麽我的 conda 沒辦法抓到 `/usr/include` 和 `/usr/lib` 的檔案。

查了很多資料都沒找到解法，我對 conda 也不太熟悉...

最後決定直接建立 symbolic link 到 conda env 裡面，有成功跑起來了，只是覺得這應該不是最好的解決方式。

```sh
ln -s /usr/include/EGL /home/efliao/.conda/envs/gaussian-avatars/include/EGL
ln -s /usr/include/KHR /home/efliao/.conda/envs/gaussian-avatars/include/KHR
ln -s /usr/include/GL /home/efliao/.conda/envs/gaussian-avatars/include/GL

ln -s /usr/lib/x86_64-linux-gnu/libEGL.so /home/efliao/.conda/envs/gaussian-avatars/lib/libEGL.so
ln -s /usr/lib/x86_64-linux-gnu/libGL.so /home/efliao/.conda/envs/gaussian-avatars/lib/libGL.so
```
