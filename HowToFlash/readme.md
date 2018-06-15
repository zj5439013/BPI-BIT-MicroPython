# **BpiBit MicroPython**

## **烧写与调试**

### 如何烧写？

#### 1. 在 Windows 下运行此目录下提供的程序

- 运行 AutoFlashSafe(或Fast).exe 程序会自动查找最新插入的串口并将同一目录下的`fimware.bin`文件烧写至芯片当中。

- AutoErase.exe 程序可以将固件擦除，如果此前有其他固件存在，或遇到了不可解决的问题，均可通过该修复工具重置板子后烧写固件。

- 上述程序经由相关 Python 脚本与`Pyinstller X86`模块打包而成。

#### 2. 在 Linux 中使用 Shell 执行以下代码烧写

``` Shell
sudo esptool.py --chip esp32 --port COM3 --baud 1152000 write_flash -z --flash_mode dio --flash_freq 40m 0x1000 firmware.bin
```

- 在此之前需用户安装 python2.7 与安装其依赖项 esptool ，例如`pip install esptool`。

- esptool.py 是 ESP 芯片系列的烧写脚本工具。

- `--chip esp32` 指esp32芯片。

- `--port COM3` 指烧写端口，COM3是Windows环境下的串口命名，在Linux下则是/dev/ttyUSB0。

- `--baud 1152000`，如果出现烧写错误，可以下调到460800，这会导致烧写的速度下降。

- `firmware.bin`，指烧写文件的位置，如果没有路径则默认是同一目录下。

- 其他保持不变，如果有疑问向我们可以提出。

#### 3. 在 Python 语言解释器环境当中执行烧写

- [AutoFlash.py](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/blob/master/HowToFlash/AutoFlash.py) 分别为Fast和Safe，即为快速烧写和安全烧写，除了烧写速度以外没有区别，可在Py代码中查阅得知。

- [AutoErase.py](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/blob/master/HowToFlash/AutoErase.py) 是指擦除当前硬件的固件，当遇到无法解决的问题时候，可以尝试擦除。

# 烧写之后？

- 烧写之后，如果烧写成功会如下图，否则会退出。

- ![SmartConfig](FlashFinish.jpg)

- 烧写成功以后请到 [趣味编程等案例](https://github.com/junhuanchen/BPI-BIT-MpyDevelop/tree/master/Code) 下获取 对应的 Python 开发示例代码。

# 出现问题？

- 当不知道怎么解决的时候，请直接提交问题给我们进行解决。

- 如果没人提供解决方案，您也可以自己使用修复工具后重新烧写固件。

- 修复工具执行成功之后结果的如下图。

- ![SmartConfig](RepairFinish.jpg)
