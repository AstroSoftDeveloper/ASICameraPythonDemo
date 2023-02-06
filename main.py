# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from asidemo import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init() # 相机初始化
    setExpValue(1300) # 设置曝光时间 单位us
    setGainValue(250) # 设置增益
    buffer = getFrame() # 获取帧
    closeCamera() # 关闭相机
    img = np.asarray(buffer) # 图像数据转换
    img = img.reshape(2080, 3096) # reshape分辨率，width*height必须与bufferSize一致，否则报错
    cv2.imshow('img', img) # opencv显示图像
    cv2.waitKey()
    input("Press <enter>")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
