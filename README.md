# MiraiChat
**MiraiChat**是一个[**MCDReforged**](https://github.com/Fallen-Breath/MCDReforged)插件,通过使用[**Mirai**](https://github.com/mamoe/miral)框架来连接**Minecraft**和**QQ**

> 注意:本插件只能运行于**MCDR v1.x**,**并不兼容 MCDR v0.x!**

## 安装和使用

### 安装[Mirai-api-http](https://github.com/project-mirai/mirai-api-http)

安装[**Mirai-console-loader**](https://github.com/iTXTech/mirai-console-loader)并安装[**Mirai-api-http**](https://github.com/project-mirai/mirai-api-http)

### 安装依赖

- [graia-application-mirai](https://github.com/GraiaProject/Application)

### 安装插件

在 **[Releases](https://github.com/Railgun-wiki/MiraiChat/Releases)页面**下载最新的```MiraiChat.py```并放入```plugins/```目录中

或下载源码并放入```plugins/```目录中

### 配置

- 配置[**Mirai-console-loader**](https://github.com/iTXTech/mirai-console-loader)和[**Mirai-api-http**](https://github.com/project-mirai/mirai-api-http)

- 按照[**Mirai-console-loader**](https://github.com/iTXTech/mirai-console-loader)和[**Mirai-api-http**](https://github.com/project-mirai/mirai-api-http)的配置修改```MiraiChat.py```文件中第```47-55```行,具体请参考[**Graia Application for mirai-api-http**](https://graia-document.vercel.app/docs/guides/installation)的文档

```python
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:8080",  # 填入 httpapi 服务运行的地址
        authKey="graia-mirai-api-http-authkey",  # 填入 authKey
        account=5234120587,  # 你的机器人的 qq 号
        websocket=True  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)
```

### 使用插件

插件提供如下命令:

Minecraft 游戏中:

```!!qq [<message>]``` 发送信息至QQ群

QQ群中:

```!!mc [<message>]``` 发送信息至Minecraft

## 鸣谢

插件所用框架:

- [mamoe](github.com/mamoe)
  - [mirai](https://github.com/mamoe/mirai)
  - [mirai-console](https://github.com/mamoe/mirai-console)
  - [mirai-api-http](https://github.com/project-mirai/mirai-api-http)

- [Fallen_Breath](github.com/Fallen-Breath)
  - [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)

插件基于:

- [GraiaProject](github.com/GraiaProject)
  - [Graia Application for mirai-api-http](https://github.com/GraiaProject/Application)

插件参考:

- [zhang-anzhi](github.com/zhang-anzhi)
  - [CoolQAPI](https://github.com/zhang-anzhi/CoolQAPI)
  - [QQChat](https://github.com/zhang-anzhi/MCDReforgedPlugins/tree/master/QQChat)

## 警告

> **本插件并未在任何平台测试通过**
>
> **望大佬帮忙测试😀**

有问题请提交[Issues](https://github.com/Railgun-wiki/MiraiChat/issues)和[Pull requests](https://github.com/Railgun-wiki/MiraiChat/pulls)
