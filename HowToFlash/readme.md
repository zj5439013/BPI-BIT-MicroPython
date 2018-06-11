# **BpiBit MicroPython**



## **使用说明书**



### 1. 固件介绍

​	基于标准MicroPython官方环境适配，无需重新烧写固件，即可在BpiBit编写Python代码直接控制硬件外设，快速的验证与实现你所期望的功能。

​	此外移除了串口Python命令行交互，取而代之的是通过WebDav的方式访问或编辑Python代码，WebDav相关工具也已在Tools目录下提供。

### 2. 功能介绍

​	当Mpy固件烧写以后，针对BpiBit板子提供了上电时按住A键（35）或B键（34）将启动如下两个特殊模式。

- #### SmartConfig（B键）

	如果是第一次启动，默认上电就会进入该模式，因为没有WIFI配置文件，在该模式下需通过EspTouch软件进行配网，即可连接BpiBit模块，Android版本程序的软件已在Tools目录下提供。

- #### SafeMode（A键）

	当python程序的SYSTEM.PY写了死循环后就无法执行WebDav的服务了，所以避免意外情况，允许用户通过按住B键保持WebDav服务的运行直至松开。

### 3. 编程环境介绍

​	接下来介绍一下编写Py代码的标准环境以及Bpibit的Python运行环境。

#### 标准编程环境

​	第一次使用固件的时候，BpiBit系统会默认生成两个文件，分别为 BOOT.PY 与 SYSTEM.PY。BOOT.PY仅在上电前运行一次，而SYSTEM.PY将会反复循环运行。

​	SYSTEM.PY文件默认内容为`# This File ill Loop Execute`，而BOOT.PY会有一行注释 `# This file is executed on every boot (including wake-boot from deepsleep)`表示该文件会在上电时执行一次。

#### 如何通过SmartConfig获得BpiBit的IP地址？

 1. 启动按住B键即可进入SmartConfig（或第一次启动）

    串口将输出如下信息在最底部：

    - ​	![SmartConfig](https://github.com/yelvlab/BPI-BIT/raw/master/Code/MicroPython/ReadMe/SmartConfig.png)

 2. 此处以Android的EspTouch软件为例

    在软件中的对应框输入当前手机所在的WIFI信息，软件将向BpiBit告知该WIFI信息，辅助其连接。

    如下图：

    - ![EspTouchConfig](https://github.com/yelvlab/BPI-BIT/raw/master/Code/MicroPython/ReadMe/EspTouchConfig.png)

 3. 点击唯一的按钮，稍等一会将会出现下图结果，如果没有就重试。

    - ![EspTouchResult](https://github.com/yelvlab/BPI-BIT/raw/master/Code/MicroPython/ReadMe/EspTouchResult.png)

 4. 这样就可以知道BpiBit已经连接上WIFI了，并且其IP地址为192.168.1.40，这个值将会提供给访问WebDav空间。

#### 如何连接到BpiBit的WebDav空间？

​	假如已经配网(SmartConfig)成功后得知BpiBit所在网络下的IP后，可以直接访问浏览器查看板子根目录下的所有文件，如下截图。

- ![ListWebDav](https://github.com/yelvlab/BPI-BIT/raw/master/Code/MicroPython/ReadMe/ListWebDav.png)

​	以下提供推荐的WebDav访问工具与方式。

​		Windows、Linux、Android、Brower等环境的WebDav访问。

​	只需要使用对应平台上的某一类可以直接访问WebDav的软件即可，比如WebDrive、Cyberduck 等，更多可以点击查看[MoreSoftWare](https://en.wikipedia.org/wiki/Comparison_of_WebDAV_software)

​	以WebDrive为例，打开软件后按如下步骤。

 1. 如图点击New

    - ![NewWebDavConnect](https://github.com/yelvlab/BPI-BIT/raw/master/Code/MicroPython/ReadMe/NewWebDavConnect.png)

 2. 再按如下图选取WebDAV，BpiBit的WebDav使用HTTP。

    - ![SelectWebDAV](https://github.com/yelvlab/BPI-BIT/raw/master/Code/MicroPython/ReadMe/SelectWebDAV.png)

 3. 此时输入刚才获得的IP地址，例如：192.168.1.40。

    - ![ConnectWebDav](https://github.com/yelvlab/BPI-BIT/raw/master/Code/MicroPython/ReadMe/ConnectWebDav.png)

 4. 此时即可建立完成，如图，默认即可，建议关闭访问时连接或验证的选项，也就是默认选项，此时软件已经添加了该项，双击打开即可以得到BpiBit的文件目录。

    - ![FinlishWebDav](https://github.com/yelvlab/BPI-BIT/raw/master/Code/MicroPython/ReadMe/FinlishWebDav.png)

 5. 其他WebDav工具也如上流程所示。

    ​

#### 如何为BpiBit编写Python程序运行？

​	比如说在SYSTEM.PY写入如下代码：

```python
print("hello bpibit!")
```

​	则串口将会反复输出以下信息。

- ![HelloBpibit](https://github.com/yelvlab/BPI-BIT/raw/master/Code/MicroPython/ReadMe/HelloBpibit.png)

​	这就是运行Python的第一步。

#### 更好用的编程环境

​	虽然前面已经可以编写Python并执行了，但这样并不是我真正想要的。

​	因此可将Python环境分为开发环境和生产环境。

- #### 生产环境

	在生产环境下，自己编写的Py代码不会被系统的其他服务打断，也就是在标准编程环境中将SYSTEM.PY写死循环即可，同时WebDav服务将不会被执行，也就无法在Python运行时修改Python代码了。

- #### 开发环境

	在开发环境下，当然是希望编写代码后保存，即时运行程序，最好还可以边写边运行Python程序，以及程序的随时停止和运行，所以提供了本目录下的三个文件，分别为BOOT.PY、SYSTEM.PY、INDEX.PY。

	BOOT.PY 会提供给系统一个线程检查INDEX.PY的文件大小变动的情况从而执行INDEX.PY代码，所以仅需在INDEX.PY文件里直接写代码运行即可（确保文件大小变动即可）。
		
	注意，当在INDEX.PY中写了死循环后，上文中提及的重载文件时将会启动多个线程，因为目前线程库还没有外部停止接口，所以前一个线程的死循环，会与新线程的死循环交错其中，如果你不希望看到信息混乱输出的话，重启一下就好了。
		
	代码如下：

```python
import time
import _thread
import sys
import uos

def thread_check():
	index_size = 0
	while(True):
		size = uos.stat('index.py')[6]
		if(size != index_size):
			print("File Update Now Reload...")
			_thread.start_new_thread(thread_main, ())
			index_size = size
		time.sleep(0.5)
		
def thread_main():
	file = open('index.py', "r")  
	code = file.read()
	file.close()  
	exec(code)

if __name__ == "__main__":
	ThreadFileCheck = _thread.start_new_thread(thread_check, ())
    
```

​	除了以上功能，对此还提供了可以控制Py代码的执行或停止的功能，在SYSTEM.PY文件中，通过检测某一个按键（例如：A键）来决定是否执行程序，默认设计成按住A键就执行代码，松开停止执行，返回到代码处继续修改，修改后更新，再按住A键继续执行，当然你也可以反过来，只需要将代码中的`0 == RUN.value()`修改成`1 == RUN.value()`就变成，按住时可以修改Python代码，松开继续执行。

​	其代码如下：

```python
from machine import Pin
import time

RUN = Pin(35, Pin.IN)

while 0 == RUN.value():
	time.sleep(0.5)
```

​	至此提供一个INDEX.PY例子。

```


while True:
	print("Micro Python And WebDav For bpibit")

	#print("Juwan test")

'''
from machine import Pin
import time

LED0 = Pin(14, Pin.OUT)
LED1 = Pin(13, Pin.OUT)

while True:
	LED0.value(1) # 高电平 亮灯
	LED1.value(0) # 低电平 熄灯
	time.sleep(0.1) # 延时休息一下
	LED0.value(0) # 低电平 熄灯
	LED1.value(1) # 高电平 亮灯
	time.sleep(0.1) # 再延时休息一下
'''
	
```

​	可以看到，按住时，执行`print`，松开后停止输出。



#### 相关教程与学习资料

​	以下相关教程与资源可以帮助你在Bpibit上了解和学习Python。

1. 软件相关应用
   - 如何用Python验算加密算法
   - 如何用Python爬取网络数据
   - 如何用Python自动登陆网站
2. 硬件相关应用
   - 播放音乐和变化呼吸灯代码[Juwan的BpiBit自用](https://github.com/yelvlab/BPI-BIT/tree/master/Code/MicroPython/JuwanBit)
   - 如何使得两灯交错闪缩
   - 如何使用超声波测距
   - 如何获取外界温度
   - 如何控制开关当生物靠近时
3. 官方文档资料
   1. [USE MICROPYTHON ONLINE](http://www.micropython.org/unicorn)
   2. [MicroPython](http://docs.micropython.org/en/latest/esp8266/)
   3. [StudyPython](http://www.runoob.com/python/python-intro.html)

#### Q & A

​	Q：有问题可以找谁？

​	A：@yelvlab and Don‘t @junhuanchen, please. XD.
