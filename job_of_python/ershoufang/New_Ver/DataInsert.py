#coding=utf-8
import json
import DataBase_Connect


def Insert_Data(dbconn,di):
    id_=1
    cursor=dbconn.cursor()

    for dir in di:
        cursor.execute('insert into the_second_house_final_f_t values(' + str(id_) + ',"' + dir['小区名称'] + '","' + dir['小区地点'] + '","' + dir['总价'] + '","' + dir['单价'] + '","' + dir['房屋户型'] + '","' + dir['所在楼层'] + '","' + dir['建筑面积'] + '","' + dir['户型结构'] + '","' + dir['套内面积'] + '","' + dir['建筑类型'] + '","' + dir['房屋朝向'] + '","' + dir['建筑结构'] + '","' +dir['装修情况'] + '","' + dir['梯户比例'] + '","' + dir['配备电梯'] + '","' + dir['产权年限'] + '","' + dir['建筑年代'] + '","' +str(dir['坐标']['lng']) + '","'+ str(dir['坐标']['lat'])+ '","' +str(dir['地铁距离'])+ '","' + str(dir['政府距离']) + '")' )
        dbconn.commit()
        print("------------------------导入"+dir['小区名称']+"成功----------------------")
        id_+=1

    cursor.close()
    dbconn.close()










