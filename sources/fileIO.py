# -*- coding: utf-8 -*-

# 发送文件
#Android
# driver.push_file('/sdcard/element.png', source_path='D:\works\element.png')
#
# # 获取手机文件
# png = driver.pull_file('/sdcard/element.png')
# with open('element.png', 'wb') as png1:
#     png1.write(base64.b64decode(png))
#
# # 获取手机文件夹，导出的是zip文件
# folder = driver.pull_folder('/sdcard/test')
# with open('test.zip', 'wb') as folder1:
#     folder1.write(base64.b64decode(folder))
#
# # iOS
# # 需要安装 ifuse
# # > brew install ifuse 或者 > brew cask install osxfuse 或者 自行搜索安装方式
#
# driver.push_file('/Documents/xx/element.png', source_path='D:\works\element.png')
#
# # 向 App 沙盒中发送文件
# # iOS 8.3 之后需要应用开启 UIFileSharingEnabled 权限不然会报错
# bundleId = 'cn.xxx.xxx' # APP名字
# driver.push_file('@{bundleId}/Documents/xx/element.png'.format(bundleId=bundleId), source_path='D:\works\element.png')

