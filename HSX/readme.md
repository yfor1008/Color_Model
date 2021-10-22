# HSX

HSX 颜色空间包含: HSI, HSL, HSV, 这三者比较类似, 这里仅介绍HSV.

## HSV 颜色空间

RGB 色彩空间不能很好地服务于对我们对于颜色的感知和我们在日常生活中谈论它的方式. 例如, 如果我们考虑重新粉刷客厅的墙壁, 我们通常会考虑它应该是什么颜色, 我们想要它有多亮, 以及它应该是柔和的还是生动的.

HSV 是一种直观的颜色空间: H(Hue), 色调(色度), 描述了颜色的深浅及在色谱中的位置; S(Saturation), 饱和度, 描述了相对于白色色调的纯度; V(Value), 明度, 描述了颜色的明亮程度. 如下图所示:

![HSV](readme.assets/HSV.gif)

- H: 用角度度量, 取值范围[0, 360], 从红色开始按逆时针方向计算, 红色为0°, 绿色为120°, 蓝色为240°; 红色, 绿色, 蓝色都是描述色调的词;
- S: 取值范围[0, 100], 值越大, 颜色越饱和(颜色越纯), 颜色深且艳; 如全红色且无白色的颜色完全饱和, 如果在红色中添加一些白色, 结果会变得更加柔和, 颜色会从红色变为粉红色. 色调仍然是红色的, 但它已经变得不那么饱和;
- V: 取值范围[0, 100], 值越大, 越亮; 白天看到一辆红色的车, 它的颜色看起来很亮, 但在晚上时可以看到, 汽车是红色的, 但它看起来更暗, 因为环境照明反射到眼睛的光线较少, 光线较少意味着颜色看起来更暗;

## HSV 与 RGB

如下图所示为 HSV 颜色空间示意图:

![hsv](readme.assets/hsv.jpg)

图中黑白所组成线即为 RGB 立方体中的中轴, 为亮度V, 圆环为色点H, 半径为饱和度S.

### 恒定亮度平面

垂直于 RGB 立方体中轴平面的所有的颜色的亮度都是一样的, 称为恒定亮度平面, 如下图所示为 RGB 颜色空间不同亮度的恒定亮度平面:

![Constant-Brightness](readme.assets/Constant-Brightness.gif)

### 恒定饱和度圆锥面

以 RGB 立方体中轴为中心圆锥面的所有颜色的饱和度都是一样的, 称为恒定饱和度圆锥面, 如下图所示为 RGB 颜色空间不同饱和度的恒定饱和度圆锥面:

![Constant-Saturation](readme.assets/Constant-Saturation.gif)

### 恒定色度平面

RGB 立方体上任意一点与中轴构成的三角面上的所有颜色的色度都是一样的, 称为恒定色度平面, 注意仅为这个三角形内部, 如下图所示为 RGB 颜色空间不同色度的恒定色度平面:

![Constant-Hue](readme.assets/Constant-Hue.gif)

### 相互转换公式

转换公式如下:

- RGB to HSV, RGB 和 HSV 取值范围都在[0, 1]

$$
C_{max} = max(R, G, B) \\
C_{min} = min(R, G, B) \\
\Delta = C_{max} - C_{min}\\

H = \begin{cases} 
0, & \Delta = 0  \\
\\
\frac{G-B}{\Delta}+0, & C_{max} = R \\
\\
\frac{B-R}{\Delta}+2, & C_{max} = G \\
\\
\frac{R-G}{\Delta}+4, & C_{max} = B \\
\end{cases} \\
H = \frac{H}{6} \\
H = 1 + H, if H < 0 \\
\\
S = \begin{cases} 
0, & C_{max} = 0 \\
\frac{\Delta}{C_{max}}, & C_{max} \ne 0
\end{cases} \\
\\
V = C_{max}
$$

- HSV to RGB, RGB 和 HSV 取值范围都在[0, 1]

$$
H = H * 6 \\
I = floor(H), F = H - I \\
M = V * (1 - S), N = V * (1 - S * F), K = V * (1 - S * (1 - F)) \\
if I = 0, (R, G, B) = (V, K, M) \\
if I = 1, (R, G, B) = (N, V, M) \\
if I = 2, (R, G, B) = (M, V, K) \\
if I = 3, (R, G, B) = (M, N, V) \\
if I = 4, (R, G, B) = (K, M, V) \\
if I = 5, (R, G, B) = (V, M, N) \\
$$

## 主要应用

图像处理, 如图像增强等, 基于此, 很多图像编辑工具都使用了这个颜色空间.



## 参考

1. http://tinf2.vub.ac.be/~dvermeir/manuals/gimp/Grokking-the-GIMP-v1.0/node49.html

