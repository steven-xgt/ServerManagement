workPath="D:\HaiheWeb\Web\HaiheWebTest\ImgLibraries"             #文件管理器工作路径
visitDay = 1             #资源监控 前端默认显示的时间范围，单位：天
ResState = True          #默认开启资源监控
ResSaveDay = 30          #默认资源监控保存时间
ResInv = 180             #默认资源监控的纪录周期，单位：秒
port = 5000              #面板默认启动端口
username = 'admin'       #默认登陆账号
password = 'admin'      #默认密码
NATPenetration = None    #是否开启内网穿透,让运行本服务的无外网IP的设备,可在外网访问,不需要此服务时填写None,需要时,更改此项为运行提供穿透的服务端的IP,如'192.168.1.94'
#开启穿透服务需要将位于本项目的server.zip,解压后单独放在有外网IP的电脑中运行其中的index.py,运行前切记根据需要修改server/config.py
#内网穿透后,该外网IP请访问服务端查看
#首次打开内网穿透功能,会向服务端注册一个绑定端口的的请求,
#首次运行可能会出现“远程计算机积极拒绝连接”之类的错误，请忽略，5-10秒后程序会自动连接上去
NATPenetrationPort = 7440  #仅在内网穿透服务启动时有效,为连接内网穿透的服务器的开放端口