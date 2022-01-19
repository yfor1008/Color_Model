# YUV

YUV颜色空间是一个大家族, 常用的有:
- YUV: PAL模拟信号
- YIQ: NTSC模拟信号, IO由UV旋转33°得到
- YCbCr: 数字信号, 是计算机系统应用最广泛的成员, 一般讲的YUV大多是指YCbCr

## YUV标准

YUV标准如下, 详见: [https://en.wikipedia.org/wiki/YUV](https://en.wikipedia.org/wiki/YUV):

- BT.601: 用于标准清晰度电视(Standard Definition Television, SDTV)
- BT.709: 用于高清晰度电视(High Definition Television, HDTV)

YCbCr标准如下, 详见: [https://en.wikipedia.org/wiki/YCbCr](https://en.wikipedia.org/wiki/YCbCr):
- BT.601: 用于标准清晰度电视(Standard Definition Television, SDTV)
- BT.709: 用于高清晰度电视(High Definition Television, HDTV)
- BT.2020: 用于超高清晰度电视(Ultra-High-Definition Television, UHDTV)

## 转换公式

### RGB与YUV相互转换

通用转换公式为:

$$
Y = W_RR + W_GG + W_BB \\

U = U_{max} \frac{B - Y}{1 - W_B} \\

V = V_{max} \frac{R - Y}{1 - W_R}
$$
其中, $U_{max}=0.436$, $V_{max}=0.615$, $W_R+W_G+W_B=1$, 针对不同的标准, 系数不同, 具体的:
- BT.601: $W_R=0.299$, $W_B=0.114$
- BT.709: $W_R=0.2126$, $W_B=0.0722$

BT.601计算后, 具体的转换公式为, 详见: [https://www.cnblogs.com/huxiaopeng/p/5653257.html](https://www.cnblogs.com/huxiaopeng/p/5653257.html):

![RGB_YUV-601](https://gitee.com/yfor1008/pictures/raw/master/RGB_YUV-601.png)

![YUV_RGB-601](https://gitee.com/yfor1008/pictures/raw/master/YUV_RGB-601.png)

### RGB与YCbCr相互转换
计算机中通常使用的是YCbCr, BT.601是使用最广泛的. 转换公式如下:

![RGB_YCbCr-601](https://gitee.com/yfor1008/pictures/raw/master/RGB_YCbCr-601.png)

![YCbCr_RGB-601](https://gitee.com/yfor1008/pictures/raw/master/YCbCr_RGB-601.png)

**JPEG转换公式与BT.601不同, 是在BT.601上的改善, 目前仅在JPEG上使用**. 转换公式如下所示:

![RGB_YCbCr-jpeg](https://gitee.com/yfor1008/pictures/raw/master/RGB_YCbCr-jpeg.png)

BT.709转换公式如下:

![RGB_YCbCr-709](https://gitee.com/yfor1008/pictures/raw/master/RGB_YCbCr-709.png)

## 采样方式

YUV的采样方式是通过U/V与Y的采样频率的比例来表示, 表示为A:B:C, 如YUV422表示Y的采样频率为4, U/V的采样频率都为2.

这里的采样频率是指, 在一行的连续4个数据中, 采集的数据个数, 如YUV444, 表示一行4个连续数据中, 每个颜色通道的采集个数都为4.

常用的采样方式有:
- YUV444: 完全采样, 表示色度没有下采样, 即每行4个数据都采集了;
- YUV422: 水平采样为2:1, 垂直没有下采样, 即每行4个数据中, Y采集了4个数据, UV分别都采集了2个数据;
- YUV420: 水平采样为2:1, 垂直采样为2:1, 即当前行的4个数据中, Y采集了4个数据, U采集了2个数据, V采集了0个数据; 下一行, 更改成了YUV402, 即Y采集了4个数据, U采集了0个数据, V采集了2个数据;
- YUV411: 水平采样为4:1, 垂直没有下采样, 即每行4个数据, Y采集了4个数据, U采集了1个数据, V采集了1个数据, 这种方式不太常用.



## 存储方式

一般有2种方式:
- packed模式: Y/U/V交错排列
- planar模式: Y/U/V分开单独排列, 如先排列Y再排列U, 然后排列V等