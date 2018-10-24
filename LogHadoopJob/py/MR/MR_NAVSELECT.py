#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "NAVSELECT"
class MR_NAVSELECT(mr_base_ex):
    def __init__(self):
        mr_base_ex.__init__(self,str_act)
        self.res_type = ["s","i","s","s","s","i"];
        self.res_name = ["SRC","CLICK","GROUP","LIST","DISPLAY","U"];
        self.res_spec_str = "S:KwMusic";

mr_obj = MR_NAVSELECT()

if __name__ == '__main__':
    test_str = r'01:10| [INFO]: <SRC:MUSIC_8.6.0.0_BCS48|ACT:NAVSELECT|S:KwMusic|CLICK:1|GROUP:#nav-root|LIST:catalog-more|DISPLAY:更多|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.6.0.0_BCS48|PLAT:WIN32|FROM:kwmusic2016_web_1_bcs_20170104.exe|UI:|{kwmusic2016_web_1_bcs_20170104.exe}|K:375027138|RESEND:0|U:50645286>(171.222.82.144)TM:1483545672'

    mr_obj.LocalTest(test_str)
    pass
