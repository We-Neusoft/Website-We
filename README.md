# We-Cloud维云技术小组

[We-Cloud维云技术小组](http://we.neusoft.edu.cn)（以下简称本小组）是[大连东软信息学院](http://www.neusoft.edu.cn/)由网络中心提供硬件、网络资源及技术支持，由学生组建的技术小组，运行于学院校园网，为广大校园网师生提供优质的网络服务。

## 目录结构

本目录即为 Django 项目根目录，各子目录说明如下：

* `apis`：开放平台接口应用：
  * `oauth`：OAuth 2.0登录认证；
  * `qrcode_we`：QR码。
* `apps`：We小组站点应用：
  * `dreamspark`：DreamSpark站点；
  * `file`：云盘站点；
  * `mirror`：开源镜像站站点；
  * `www`：首页站点。
* `common`：内、外网通用访问请求；
* `libs`：通用函数库；
* `we`：项目配置文件，通用静态文件、模板，以及中间件、后端组件。

## 使用说明

### 运行环境

* Python 2.7.x
* Django 1.6+

### 配置说明

1. 下载该目录中的全部文件；
2. 安装`requirements.txt`所列组件；
3. 在`we`目录中创建`settings.py`配置文件，同步数据库；
4. 启动`Django`服务器即可。

*注意：我们在`we`目录中存放了一份本小组正在使用的配置文件样本`settings.py.sample`，并将敏感信息使用`WE_CLOUD`进行了替换。*

- - -

感谢大连东软信息学院网络中心提供本小组所有硬件及网络资源。
