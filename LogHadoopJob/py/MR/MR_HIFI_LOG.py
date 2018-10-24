#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "HIFI_LOG"
class MR_HIFI_LOG(mr_base_ex):
    def __init__(self):
        mr_base_ex.__init__(self,str_act)
        self.res_type = ["s","s","i","i","i"];
        self.res_name = ["SRC","TYPE","CDID","FINISH","U"];
        self.res_spec_str = "S:KwMusic";

mr_obj = MR_HIFI_LOG()

if __name__ == '__main__':
    #test_str = r'49:06| [INFO]: <SRC:MUSIC_8.5.2.0_BCS16|ACT:HIFI_LOG|S:KwMusic|TYPE:ENTER_HIFI_DOWNLOAD_PAGE|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8cs_20161208.exe}|K:546529252|RESEND:0|U:92204504>(60.181.172.98)TM:1481611747'
    test_str = r'53:12| [INFO]: <SRC:MUSIC_8.5.2.0_BCS16|ACT:HIFI_LOG|S:KwMusic|TYPE:CDDownResult|U:92204504|N:1481611558780weixin|UID:336267682|NA:ALR Jordan-Bass & Drums|AR:Various Artists|AL:ALR Jordan-Bass & Drums|F:FLAC|CDID:3075|PAY:0|S1:|S2:|PSRC:|FINISH:1|ERRORCODE:|ISVIP:0|VIPTY:-1|VIPLV:-1|UQ:UQ|RQ:UQ|DP:|DSRC:|DMOD:|FROM:|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.5.2.0_BCS16|PLAT:WIN32|FROM:kwmusic2016_web_1_bcs_20161208.exe|UI:336267682|{kwmusic2016_web_1_bcs_20161208.exe}|K:546529252|RESEND:0|U:92204504>(60.181.172.98)TM:1481611994'

    mr_obj.LocalTest(test_str)
    pass
