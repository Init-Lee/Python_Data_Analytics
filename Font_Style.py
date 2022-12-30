#写入魔法命令，设定图表样式

import matplotlib.pyplot as plt
import platform
    
sys = platform.system().lower()#获取系统类型
if(sys == 'win32'): #判定系统类型
  plt.rcParams['font.sans-serif'] = ['SimHei'] #windows os下支持中文，用于正常显示中文标签
else:
  plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] #mac os 下显示中文 二选一 两行代码
#end if
plt.rcParams['font.size'] = 18 #调整字体大小
#以上-------字体格式代码，根据运行环境自行调整------------------------------
