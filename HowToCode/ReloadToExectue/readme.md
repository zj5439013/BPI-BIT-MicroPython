# 自动重载代码软固件

这是一个允许用户在限定的 index.py 文件里编写代码并自动重载的 Python 代码固件。

# 简单来说

保存 index.py 时会重新执行代码，帮助用户更快的测试硬件外设接口。

# 注意事项
1. 请确保 `while Thread[0]: # Replace while True:` 否则将会出现多线程执行情况。
2. 如果期望Python代码稳定执行，请修改SYSTEM.PY的while 0 == Button.value():将其运行模式的切换改变为按键触发
3. Python运行时间与time.sleep(0.1)有关，建议不要修改此处，否则WebDav执行间隔过长将超时导致操作失败。
4. while 0 == Button.value() 中的 0 代表执行WebDAV服务，反之 1 代表默认执行Python，WebDAV将无法响应，因此此时需按住按键暂时保持WebDAV的运行直到文件上传完毕
5. 会存在一些无法撤销的情况，如果说，开启了某个硬件功能，但没有关上，这会导致下一次的修改运行后出错，因为重载执行并不是重启系统。
