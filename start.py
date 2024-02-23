import MicAuth#微软登录模块
import launcher#启动模块
import install#安装模块
from os.path import exists 
from json import dumps
from json import loads
from sys import maxsize

def help():
    print("user:",username,"欢迎使用Jade启动器\n下面是命令帮助:\n1.启动器与游戏设置\n2.登录\n3.启动游戏\n4.安装游戏\n9.返回上一级or关闭\n0.帮助"
    "")

def help2():
    print("\n1.启动器与游戏设置\n2.登录\n3.启动游戏\n4.安装游戏\n9.返回\n0.帮助")

if __name__ == "__main__":
    if not exists("launcherOptions.json"):
        launcher_options_json = open("launcherOptions.json", "w")
        launcherOptions = {#默认启动器设置
            "game": {
                "maxMen": "1024M", #最大内存
                "mcDir": "./.minecraft", #mc根目录
                "javawPath": "", #javaw.exe的路径
                "downloadFrom": "mojang"
            },
            "user": {
                "username": "",
                "userType": "",
                "access_token": "",
                "uuid": "",
            }
        }
        launcher_options_json.write(dumps(launcherOptions))#把json写入文件
        launcher_options_json.close()
    else:
        launcher_options_json = open("launcherOptions.json", "r")#读取
        launcherOptions = loads(launcher_options_json.read())
    #用户信息
    username = launcherOptions["user"]["username"]
    userType = launcherOptions["user"]["userType"]
    access_token = launcherOptions["user"]["access_token"]
    uuid = launcherOptions["user"]["uuid"]
    #游戏信息
    maxMen = launcherOptions["game"]["maxMen"]
    mcDir = launcherOptions["game"]["mcDir"]
    javawPath = launcherOptions["game"]["javawPath"]
    downloadFrom = launcherOptions["game"]["downloadFrom"]
    #游戏信息的读取
    help()
    while True:
        #命令输入
        command = input(">>>")

        if command == "1":
            print("设置系统\n1.设置最大运行内存\n2.设置游戏根目录\n3.设置javaw.exe路径\n4.设置下载源")
            setting_command = input(">>>")
            if setting_command == "1":
                maxMen = input("\n请输入最大运行内存(MB):")
                launcherOptions["game"]["maxMen"] = maxMen
                print("最大运行内存:", maxMen, "MB")
            elif setting_command == "2":
                mcDir = input("\n请输入游戏根目录:")
                launcherOptions["game"]["mcDir"] = mcDir
                print("success")
            elif setting_command == "3":
                javawPath = input("\n请输入javaw.exe路径:")
                launcherOptions["game"]["javawPath"] = javawPath
                print("success")
            elif setting_command == "4":
                downloadFrom_1 = input("\n请输入下载源名称 1.mojang 2.BMCLAPI\n您选择：")
                if downloadFrom_1 == "1":
                    downloadFrom = "mojang"
                    launcherOptions["game"]["downloadFrom"] = downloadFrom
                elif downloadFrom_1 == "2":
                    downloadFrom = "BMCLAPI"
                    launcherOptions["game"]["downloadFrom"] = downloadFrom
                elif downloadFrom_1 != ('1' or '2'):
                    print('我丢雷各扑街，正常点好不好,我很忙的，先帮你设成mojang，要改自己改')
                    downloadFrom = "mojang"
                    launcherOptions["game"]["downloadFrom"] = downloadFrom
                print("success,game downloadFrom", downloadFrom)
            elif setting_command == "9":
                print("已返回上一级")
                help2()
                continue
            else:
                print("选择错误,已退出系统")
                help2()
                continue
        #登录
        elif command == "2":
            type = input("\n请输入登陆方式 1.离线 2.微软\n您选择：")
            if type == "1":
                userType = "Legacy"
                username = input("\n请输入用户名:")
                uuid = "{}"
                access_token = "{}"
            elif type == "2":
                userType = "mca"
                loginm = MicAuth.OAuth()
                username = loginm["username"]
                uuid = loginm["uuid"]
                access_token = loginm["access_token"]
            launcherOptions["user"]["username"] = username
            launcherOptions["user"]["uuid"] = uuid
            launcherOptions["user"]["access_token"] = access_token
            launcherOptions["user"]["userType"] = userType
            print("登录成功，您的ID是",username)

        #启动游戏
        elif command == "3":
            version = input("\n请输入要启动的版本:")
            #检测信息是否齐全
            if username == "":
                print("\n您尚未登录,请先登录")
            elif mcDir == "":
                print("\n您的游戏根目录为空")
            elif maxMen == "":
                print("\n您的最大运行内存为空")
            else:
                if exists("C:\\Program Files (x86)"):
                    i = 64
                else:
                    i = 32
                print("\n正在为您启动游戏")
                launcher.run(mcDir, version, javawPath, maxMen + "m", username, userType, uuid, access_token, i)
        #安装游戏
        elif command == "4":
            version = input("\n请输入要安装的游戏版本:")
            install.downloadVersion(version, mcDir, downloadFrom)

        elif command == "9":
            break
        elif command == "0":
            help()
        

        
        #放在循环里面，好让启动器设置及时更新
        launcher_options_json = open("launcherOptions.json", "w")#写入
        launcher_options_json.write(dumps(launcherOptions))#将修改后的信息写入json文件
        launcher_options_json.close()


