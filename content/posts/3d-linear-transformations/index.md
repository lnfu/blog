---
title: "三維空間中的線性變換"
date: 2024-01-12T15:09:06+08:00
draft: false
---

這個東西很基礎也很有用，但是常常一段時間沒碰就忘記了，乾脆寫個文章。

一般來說，三維空間中的線性變換可以簡單分類成: 縮放 (scale)、反射 (reflection)、旋轉 (rotation)、平移 (translation)、推移 (shear)。因此這篇文章就以這個順序來撰寫。

希望往後可以再補充更多更基礎的理論 (例如線性群)，以及應用的東西 (例如伊斯蘭的幾何造型，雖然那些都是 2D 的圖案)。


## 複習
這篇文章預設讀者已經熟悉向量的基本運算，包括內積 (dot product) 和外積 (cross product)。

內積在幾何上有一個重要的功能，就是計算投影。我們可以定義三個非常簡單直觀的基底 (base) 分別是 x, y, z 軸方向的單位向量，如此一來就能夠用這三個基底表示出三維空間中的任意向量 (計算該向量在三軸方向的投影)。

而關於外積的幾何性質，除了在方向上和兩向量所成平面垂直外，大小也兩向量所形成的平行四邊形 (或是三角形) 面積有關。

## 縮放

在 x 軸方向、y 軸方向、z 軸方向分別縮放 r, s, t 倍。

$ \begin{bmatrix} 
x\prime \newline
y\prime \newline
z\prime \end{bmatrix} = \begin{bmatrix} 
r & 0 & 0 \newline
0 & s & 0 \newline
0 & 0 & t \end{bmatrix} \begin{bmatrix} 
x \newline
y \newline
z \end{bmatrix} $

## 反射

和縮放的概念差不多，這邊以對 x 軸反射為例。

$ \begin{bmatrix} 
x\prime \newline
y\prime \newline
z\prime \end{bmatrix} = \begin{bmatrix} 
-1 & 0 & 0 \newline
0 & 1 & 0 \newline
0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 
x \newline
y \newline
z \end{bmatrix} $

## 旋轉

之後會補上一個不太嚴格的證明，這邊先給出繞 z 軸 $ \theta $ 的旋轉。

$ \begin{bmatrix} 
x\prime \newline
y\prime \newline
z\prime \end{bmatrix} = \begin{bmatrix} 
\cos(\theta) & -\sin(\theta) & 0 \newline
\sin(\theta) & \cos(\theta) & 0 \newline
0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 
x \newline
y \newline
z \end{bmatrix} $


## 平移

之後補充 homogenous coordinates 是什麼以及為什麼要用。

$ \begin{bmatrix} 
x\prime \newline
y\prime \newline
z\prime \end{bmatrix} = \begin{bmatrix} 
1 & 0 & 0 \newline
0 & 1 & 0 \newline
0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 
x \newline
y \newline
z \end{bmatrix} + \begin{bmatrix} 
a \newline
b \newline
c \end{bmatrix} $

## 推移 

之後補