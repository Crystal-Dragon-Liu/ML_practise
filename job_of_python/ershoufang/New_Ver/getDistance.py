import Get_Distance
import Get_Subway_latlng

def getdistance(l_list,lng,lat):
    r1=100000000000
    #print(len(l_list))
    for l in l_list:
        #lat1, lng1, lat2, lng2
        r2=Get_Distance.getDistance(l[0],l[1],lng,lat)

        if r2<r1:
            r1=r2

    return r1
#l=Get_Subway_latlng.get_subway_site()
#d=getdistance(l,118.40225421339426,31.997475222184268)
#print(d)

