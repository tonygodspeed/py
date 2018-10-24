#!/usr/bin/env python
# coding=utf8

from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "AppStart"
class MR_APPSTART(mr_base_ex):
    def __init__(self):
        mr_base_ex.__init__(self,str_act)
        self.res_type = ["s","s","s","s","i","i","s","s","s","s","i","i","i","i","i"];
        self.res_name = ["SRC","Type","OSV","CPU","MEM","FREEMEM","STARTSRC","UUID","UMAC","SKINTYPE","SKINID","SONGWP","STARTPAGEWP","U",];#{'SRC':'','Type','','U':""};
        self.res_spec_str = "S:KwMusic";

        '''
        mt_type = [
                      {'key':'SRC',    'type':'s', 'mt':r'^.*<SRC:' + common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'NONE',     'type':'s',  'mt':r'S:KwMusic.*?'},
                      {'key':'Type','type':'s', 'mt':r'Type:'+common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END},
                  ]
        '''


mr_obj = MR_APPSTART()
if __name__ == '__main__':
    #test()
    #strTest = r'00:00| [INFO]: <SRC:MUSIC_8.5.0.0_PQ3|ACT:AppStart|S:KwMusic|Num:10623|Exit:1|Type:auto|STARTTM:125|OSV:5.1.2600 Service Pack 3[Microsoft Windows XP]|CPU:2394*2|MEM:2985|FREEMEM:2034|MUSICAPP:|SYSSTARTTIME:167859|FULLINITTIME:56422|STARTSRC:xxx|GreenVer:0|CHANNEL_NAME:160004_01|PROD:MUSIC|VER:8.5.0.0_PQ3|PLAT:WIN32|FROM:KwMusicSetup_360.exe|UI:|{KwMusicSetup_360.exe}|K:41980548|RESEND:0|U:7591476>(122.156.50.245)TM:1476720003'
    strTest = r'07:00| [INFO]: <SRC:MUSIC_8.7.0.0_BCS17|ACT:AppStart|S:KwMusic|Num:10163|Exit:1|Type:manual|STARTTM:655|OSV:6.1.7601 Service Pack 1[Windows 7 Ultimate]|CPU:3292*4|MEM:8104|FREEMEM:2350|MUSICAPP:|SYSSTARTTIME:241135300|FULLINITTIME:3432|STARTSRC:|GreenVer:0|UUID:E807E5486ECE462F83775690B4C078AD2jfUfl/+dx+yT2WnhPVAnOr7u16TnBg8|UMAC:D8CB8A68A2AC|SKINTYPE:BKSKIN|SKINID:1|SONGWP:1|STARTPAGEWP:1|CHANNEL_NAME:|PROD:MUSIC|VER:8.7.0.0_BCS17|PLAT:WIN32|FROM:KwMusic8.6.0.0_BCS35.exe|UI:|{KwMusic8.6.0.0_BCS35.exe}|K:565844836|RESEND:0|U:7872000>(111.207.202.9)TM:1483081633'
    mr_obj.LocalTest(strTest)
    pass