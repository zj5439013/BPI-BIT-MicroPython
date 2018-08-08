# **BpiBit MicroPython**

## **使用说明书**

[TOC]

### 1. 固件开发介绍

&emsp;&emsp;基于标准 MicroPython 官方环境适配，无需重新烧写固件，即可在 BpiBit 编写 Python 代码直接控制硬件外设，快速的验证与实现你所期望的功能。

&emsp;&emsp;与官方不同的是，本固件移除了串口 Python 命令行（Shell）交互，取而代之的是通过 WebDAV 的方式访问或开发 Python代码，并在本目录下提供如下列表功能，此外还提供软固件扩充功能，以支持浏览器网页端在线编程。

- [烧写与修复工具](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/HowToFlash)

- [调试与管理工具](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/Tools)

- [趣味编程等案例](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/HowToCode)

- [浏览器在线编程](https://github.com/junhuanchen/BPI-BIT-MpyOnlineEditor)

&emsp;&emsp;接下来将介绍如何在 BpiBit 的 MicroPython 进行开发。

### 2. 开发环境介绍

#### 1. 尝试烧写一个固件吧

##### 烧写固件教程

&emsp;&emsp;请到此处[烧写固件教程](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/HowToFlash)学习与尝试对应平台的烧写方式，千万别迷路了，要记得回来喔。

#### 2. 学会打印调试信息吧

##### 1. 查看 BpiBit 的运行情况
		
&emsp;&emsp;将板子上电后一会可以发现它会滚动显示四个字符，和 板子的 MAC 地址后两个字节相关，假设板子显示为`88C2`，那么板子默认会自动连接名称为 bit88c2 的 WIFI AP 热点，在没有 WIFI 热点的时候，它也会建立一个热点，名称为 bit88c2 的热点，这个值将会给板子用作标识、访问的功能用途。

&emsp;&emsp;接着我们将通过任意一种串口调试工具即可查看其输出的工作信息。

&emsp;&emsp;到此处查看[获取 BitBpi 串口输出信息](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/Tools#1-获取-bitbpi-串口输出信息)章节中学习如何使用串口调试工具，相关软件同理。

&emsp;&emsp;在不远的未来将提供浏览器在线调试器。

##### 2. 访问 BpiBit 的存储空间

&emsp;&emsp;若是未配网过的板子可以在板子启动前多按几次按键 A 后即可进入配网模式，接着到[辅助 BitBpi 连接附近WIFI](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/Tools#2-辅助-bitbpi-连接附近wifi)如何帮助 BpiBit 连接到与您同处一个 WIFI 环境下的编程环境，从而通过 WebDAV 的形式访问它。

&emsp;&emsp;并且它支持 Windows、Linux、Android、Web Browser、Mac、IOS 等平台的访问。

&emsp;&emsp;假设你已经知道它的名称和地址信息了，那你就可以通过学习这章节来访问它了，请点击[访问 BitBpi 编辑文件教程](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/Tools#3-访问-bitbpi-编辑文件教程)。

&emsp;&emsp;对应的工具也已打包存放到Tools目录，但不一定是最新的，为求最新版本的用户可以自行到对应网站去获取，均已提供工具名称以及来源。 

- [访问 BitBpi 编辑文件教程](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/Tools#3-访问-bitbpi-编辑文件教程)

&emsp;&emsp;想知道更多使用方法？请到 Tools 目录下查看对应工具的使用说明吧。

##### 3. 可以做什么，不可以做什么？

&emsp;&emsp;有些 WebDAV 客户端实现存在差异，当你发现有些 WebDAV 编辑卡死的情况，请不要担心是板子的问题，这类情况多是 WebDAV 协议处理不兼容，但对于 Tools 提供的工具，是允许您直接在编辑的。

&emsp;&emsp;在这样小小板子里，是没有关机的概念的，在访问它内部文件的过程中，请尽量不要突然重启或断电，这极其容易导致内部文件损坏或丢失甚至是无法编辑，如果遇到了这样的情况，请到 [修复固件教程](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/HowToFlash#出现问题) 查看如何修复它即可。


#### 3. 最后开始你的编程之旅吧

&emsp;&emsp;是时候开始学习 [趣味编程等案例](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/HowToCode)  了。

### 3. 特殊功能介绍*

&emsp;&emsp;当固件烧写以后，针对 BpiBit 板子提供了如下两个特殊模式。

#### SmartConfig（A键）

&emsp;&emsp;开机期间前 2 秒按一次 A键 后松开将进入该模式，在该模式下需通过 EspTouch 或 SmartConfig 等软件进行配网，通过配网工具即可帮助 BpiBit 板子连接 WIFI ，其中对应的 Android 版程序的软件已在 Tools 目录下提供，也可以另外在 Google Store 获取，而 IOS 版本则需要自行在 AppStore 里搜索 SmartConfig 下载获得。

- 通过手机来[辅助 BitBpi 连接附近WIFI](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/Tools#2-辅助-bitbpi-连接附近wifi)后即可访问文件。

#### Safe Mode（B键）

&emsp;&emsp;开机期间前 2 秒按一次 B键 后松开将进入该模式，再按一次即可退出该模式，当 Python 程序的 system.py 写死循环后就无法执行 WebDAV 的服务了，这会导致无法访问固件空间的意外情况，因此在设计上预留了外部按键，从而允许用户通过按住 B键 保持 WebDAV 服务的运行直至松开之前都可以继续编辑代码文件。

### Q & A

​	Q：There is a problem?

​	A：New issue or @me. QQ 741380738 Or WeChat Junhuanchen.
