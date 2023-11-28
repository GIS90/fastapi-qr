> ## FastAPI-QR介绍

***FastAPI-QR***   
基于FastAPI搭建的后端APIs，达到快速开发、上线的一款后台API脚手架项目。


### 项目地址
https://github.com/GIS90/fastapi-qr.git
后台WIKI设计说明：https://github.com/GIS90/fastapi-qr/wiki


### 线上地址

```
线上地址：http://api.pygo2.top/  
```
![deploy/static/api/01基础API.png]  
![deploy/static/api/02METHOD方法.png]  
![deploy/static/api/03系统登录与登出.png]  
![deploy/static/api/04指定Router全局使用Token验证.png]  
![deploy/static/api/05文件上传.png]  
![deploy/static/api/06ERROR错误.png]  
![deploy/static/api/07Response对象类返回测试示例.png]


> ## 脚手架架构

![Image text](https://img.shields.io/badge/Language-Python-red)
![mage text](https://img.shields.io/badge/DevStructure-FastAPI-0000FF)
![mage text](https://img.shields.io/badge/DB-Mysql-green)
![mage text](https://img.shields.io/badge/Tool-Uvicorn-FFFF00)
![mage text](https://img.shields.io/badge/Tool-Supervisor-FFFF00)


### 项目架构

项目基于**python3+fastapi+mysql+uvicorn+supervisor**进行搭建的一个web服务项目，备具Restful API、JWT验证、Router开发等功能。   
主要用来做API对接，所以只保留了API接口功能，如果想使用前端模板功能，直接在deploy目录下的templates、static下写入html、js等文件即可。  
***git clone***之后修改配置即可运行，在此基础上可进行二次开发，可以前端/后台独立、也可以运用jinja2模板。

  - python 开发语言，基于python3.7
  - fastapi python语言使用的web api异步框架
  - mysql 数据库
  - uvicorn web服务与应用app之间的管理
  - supervisor 项目进程的启动、停止、重启等管理
  
项目可以运行于Linux、Windows、Macos等系统上，建议使用Centos7.5，支持性较好，默认端口54321（可以etc中的config.yaml配置中进行更改，配置有开发模式配置与线上配置，后面有详细介绍）。


> ## 运维

### 配置说明

项目配置主要有2套，位于项目的根目录etc下
  - dev 测试环境
  - prod 线上环境

每套配置文件夹下有2个配置文件：
  - config.yaml：项目的db、mail、log等项目开发用的所有配置，这里的log记录项目的log，关于项目相关的配置都可以在此文件进行配置
  - uvicorn：项目启动时所需要的IP、port、log、进程数量等配置  

supervisor: 项目进程管理的配置信息，单独一个，部署到线上  
.yaml格式的配置文件是有deploy/config.py进行解析的，如果在config.yaml配置文件中添加配置信息，需要在此文件进行解析添加，**建议添加配置默认值**。

### 环境搭建

  - Centos7.5系统服务器
  - Python3、mysql、supervisor等基础环境安装。
  - 安装好数据库之后，执行dbsql>sql.sql文件
  - git clone https://github.com/GIS90/fastapi-qr.git
  - 安装项目运行的环境：python install_env.py，建立项目独立的运行环境，安装了virtualenv、python、uvicorn、packages等操作，了解具体详情请参考install_env.py代码（如果执行遇到问题，直接用本机python环境部署requirements.txt包，详情见手工部署）
  - 更新web配置文件：etc/prod/config.yaml（线上）、etc/dev/config.yaml（测试），根据不同需求进行配置更改
  - cd 项目根目录：source .venv/bin/activate：激活项目环境
  - 启动项目
    - **_手动启动：下面有介绍_**  
    如果是测试或者开发，建议使用手动启动项目，关于dev/prod中的config.yaml配置信息详情请参考配置解析说明部分
  - 选做：安装supervisor && 项目加入supervisor进行管理，项目包含了supervisord配置文件&&项目supervisorctl配置文件
  
### 手动部署

  - pip install -r requirements.txt

此程序运行于python3，其中requirements.txt项目所需要的包，已固定版本，如果使用了***install_env.py***一键式部署，则无须单独安装包。  
一键部署需要服务器有python3环境【部署前提】。

### 手动启动

手工启动项目是为了方便调试项目，在本机、服务器简述不同的启动方式。

#### 本机
1.项目根目录app.py文件，开启server.run()  
2.安装好项目运行环境，***source .venv/bin/activate***启动项目运行python
3.执行sudo python app.py，代码目前已写入，处于注释状态  
4.通过手动启动的项目为dev开发环境配置，可在deploy/config.py中进行默认调整（mode = os.environ.get('mode') or 'dev'）  
5.如果手动启动模式开启，在gunicorn进行启动，会error: [Errno 48] Address already in use.

注意：启动项目一定要用virtualenv安装的python环境进行启动（source .venv/bin/activate）


#### 服务器

```
export mode=prod
```
剩下的操作与本机启动一致，加入mode环境变量是为了使用prod配置文件。

### 数据库

sql：dbsql>sql.sql，直接执行即可，包含创建数据库、用户、表、索引等。
常用mysql命令：
```
远程连接: mysql -h 127.0.0.1 -P 3306  -u root -p
授权: grant all on *.* to '用户名'@'%' identified by '密码';
删除授权: revoke all privileges on *.* from '用户名'@'%';
刷新: flush privileges;
查询版本: select version(),current_date;;
显示所有数据库:  show databases;
显示当前数据库包含的表: show tables;
查看数据库字符集: show variables like '%char%';
查看mysql实例的端口: show variables like 'port';
用户重命名: RENAME USER '老名'@'%' TO '新名'@'%';
锁表:  flush tables with read lock;
查看当前用户:  select user();
查看所有用户: SELECT User, Host, Password FROM mysql.user;
显示表结构和列结构的命令: desc tablename;
查看master状态: show master status;
查看slave状态: show slave status ;
查看所有的log文件: show master logs;在主服务器上执行(即查看所有binlog日志列表)
```
导出工具
```
mysqldump
```

### 工具类方法

  - install_env.py项目一键式环境部署，前提服务器上有python3、pip，直接执行这个脚本即可
  - deploy>utils>base_class.py 基类
  - deploy>utils>command.py 命令行
  - deploy>utils>decorator.py 装饰器
  - deploy>utils>enum.py 枚举
  - deploy>utils>exception.py 异常类
  - deploy>utils>logger.py 日志
  - deploy>utils>status.py **API response JSON**
  - deploy>utils>status_value.py **API response JSON message**
  - deploy>utils>utils.py 工具方法，任何Python（version：3）项目都适合使用
  - deploy>utils>watcher.py 监控打点
 
### delib封装包

  - deploy>delib>dtalk_lib.py   
    DingTalk Api class, it use to push message  
    采用单例模式的DingApi类，主要用请求dingTalk openApi来操作DingDing进行发消息等操作  
    目前，只支持机器人推送消息操作  
    类添加了is_avail对access token进行判断是否可用，如果不可用中止程序
  - deploy>delib>excel_lib.py   
    Excel表读取、写入工具  
    使用了xlrd、xlwt、openpyxl，Excel表格处理包进行开发的lib工具包
  - deploy>delib>file_lib.py   
    文件处理包(the file dealing lib)  
    静态工具包，适用于任何项目以及脚本
  - deploy>delib>http_lib.py    
    HTTP请求工具，基于requests
  - deploy>delib>image_lib.py    
    图片处理
  - deploy>delib>qywx_lib.py    
    企业微信消息通知  
    腾讯企业微信官网提供一整套WebHook API接口，内容相当丰富，可以实现内部、第三方等各种各样的功能
  - deploy>delib>store_lib.py    
    对象存储  
    使用了七牛（qiniu.com）面对对象存储，注册免费使用10G空间

    
> ## 其他

### supervisor

管理项目进程的启动、停止、重启等操作
安装：pip install supervisor
配置：
  - dev：etc/dev/supervisor_open2lisapi.conf
  - prod：etc/prod/supervisor_open2lisapi.conf

把指定环境的supervisor_open2lisapi.conf cp到/etc/supervisord.d/include/*下。  
项目root根目录下有supervisord.conf文件，用来配置supervisord，放在/etc/supervisord.d目录下。

### uvicorn

负责web项目进程、服务

安装：pip install uvicorn

如需特别项目启动信息，可以加入uvicorn.conf或者更改命令行uvicorn启动方式加入参数即可

### crontab

里面包含crontab定时任务，具体任务列表如下：
- auto_clear_logs.sh：日志清除任务
- mysql_backup_task.sh：数据库备份任务

crontab简单功能：
- crontab -e 编辑
- crontab -l 查看



> ## 联系方式

* ***Github:*** https://github.com/GIS90
* ***Email:*** gaoming971366@163.com
* ***Blog:*** http://pygo2.top
* ***WeChat:*** PyGo90


Enjoy the good life everyday！！！
