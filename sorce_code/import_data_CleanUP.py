#使用魔法命令，以便后面调用

import pandas as pd #导入pandas库

DataFilePath = "./bike_data.csv" #需要分析的数据文件路径

BikeDataFrame = pd.read_csv(DataFilePath,encoding='gb2312') #建立BikeDataFrame对象访问数据

#-----初步处理-------
BikeDataFrame.drop_duplicates(subset = ['bike_id','datetime','date'],  keep = 'first' , inplace = True) #删除重复的数据
BikeDataFrame.dropna(axis = 0,inplace = True) #删除空值数据

#-----数据清洗-------
#建立转换函数
def changeTime(datetime):
    datetime = datetime.rjust(8,'0') #右对齐数据  
    hour = int(datetime[:2])         #提取小时，转换整形
    if(hour >= 24):      #对符合条件的进行取余处理
        hour = hour % 24
        datetime = str(hour).rjust(2,'0')+datetime[2:]
    #end if
    return datetime,hour #返回处理好的时间数据，增加新的小时数据
#end changeTime

#通过apply功能调用上述处理功能函数，校准时间数据格式，同时增加‘hour’列数据
BikeDataFrame['datetime'],BikeDataFrame['hour'] = zip(*BikeDataFrame.datetime.apply(changeTime)) 

#删除包含'#VALUE!'数值的数据-----------
BikeDataFrame.drop(BikeDataFrame[BikeDataFrame['temp_value']=='#VALUE!'].index,inplace=True)
#将'temp_value'类型转换为float
BikeDataFrame['temp_value'] = BikeDataFrame['temp_value'].astype('float')
