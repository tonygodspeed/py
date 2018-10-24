#!/usr/bin/env python
# coding=utf8

from MR_BASE import *
import check_valid
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "UUIDGEN"
class MR_UUIDGEN(mr_base_ex):
    def __init__(self):
        mr_base_ex.__init__(self,str_act)
        self.res_type = ["s","s","s","s","s","s","i","i"];
        self.res_name = ["SRC","RMAC","OLDU","GENU","UUID","UMAC","U",];#{'SRC':'','Type','','U':""};
        self.res_spec_str = "S:KwMusic";


mr_obj = MR_UUIDGEN()
if __name__ == '__main__':
    #test()
    #strTest = r'[7872000][act][10-11 11:13:49.020][KNF]: SRC:test|ACT:UUIDGEN|S:KwMusic|RMAC:D4BED9DE24AE|OLDU:7872000|GENU:0|UUID:95DCBC384A3A410882F5925E8580CACBp+yNDnsKcDizzaFptbXy+uaO6OgVnn88MZI=|UMAC:D4BED9DE24AE|CHANNEL_NAME:|PROD:MUSIC|VER:|PLAT:WIN32|FROM:KwMusic8.5.0.0_BCS1111.exe|UI:|{KwMusic8.5.0.0_BCS1111.exe}|K:53456655|RESEND:0|U:7872000'
    strTest = r'[7872000][act][10-11 11:13:44.735][KNF]: 2%09<SRC:test|ACT:AppStart|S:KwMusic|Num:2691|Exit:1|Type:manual|STARTTM:218|OSV:6.1.7601 Service Pack 1[Windows 7 Ultimate]|CPU:3292*4|MEM:8104|FREEMEM:904|MUSICAPP:|SYSSTARTTIME:926984663|FULLINITTIME:2277|STARTSRC:|GreenVer:0|UUID:E807E5486ECE462F83775690B4C078AD2jfUfl/+dx+yT2WnhPVAnOr7u16TnBg8|UMAC:D8CB8A68A2AC|CHANNEL_NAME:|PROD:MUSIC|VER:|PLAT:WIN32|FROM:KwMusic8.5.0.0_BCS1111.exe|UI:|{KwMusic8.5.0.0_BCS1111.exe}|K:53456655|RESEND:0|U:7872000>'
    mr_obj.LocalTest(strTest)
    pass