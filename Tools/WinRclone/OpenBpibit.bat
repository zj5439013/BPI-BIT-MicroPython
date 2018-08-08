
goto note

Windows 系统下需要安装 winfsp （已提供）
在同目录下的 rclone.conf 中设置如下信息

[bite13d]
type = webdav
url = http://bite13d.local
vendor = other
user = 
pass = 

[bite13d_ip]
type = webdav
url = http://192.168.1.214
vendor = other
user = 
pass = 


针对自己的板子只需修改 [bite13d] 和 url = http://bite13d.local ( http://192.168.X.XXX ) 的 bite13d 改成自己的板子名称或 IP 地址。

:note

rclone mount bite13d: k: --cache-dir \BpiBitTemp --vfs-cache-mode full --config rclone.conf

rclone mount bite13d_ip: k: --cache-dir \BpiBitTemp --vfs-cache-mode full --config rclone.conf

pause
