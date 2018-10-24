#!/usr/bin/env python
# coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

class MR_DOWN_MUSIC(mr_base):
    def __init__(self):
        mt_type = [
                      {'key':'SRC',    'type':'s', 'mt':r'^.*<SRC:' + common_def.MT_VALUE_INVALID_POSTFIX,},
                      {'key':'RID',     'type':'s', 'mt':r'\|RID:'+common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'NONE',     'type':'i', 'mt':r'\|FINISH:0.*'},#+common_def.MT_VALUE_INVALID_POSTFIX},
                      #{'key':'UQ',     'type':'s', 'mt':r'\|UQ:'+common_def.MT_VALUE_INVALID_POSTFIX},
                      #{'key':'RQ',     'type':'s', 'mt':r'\|RQ:'+common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,"DOWN_MUSIC")

mr_obj = MR_DOWN_MUSIC()
if __name__ == '__main__':
    #test()
    strTest = r'00:00| [INFO]: <SRC:MUSIC_8.0.3.2_P2T1|ACT:DOWN_MUSIC|S:KwMusic|U:28072585|N:|UID:|NA:身骑白马|AR:徐佳莹|AL:LaLa首张创作专辑|F:mp3|RID:MUSIC_502964|S1:3608157514|S2:666972908|PSRC:VER=2015;FROM=曲库->歌手->徐佳莹->LaLa首张创作专辑|FINISH:0|ERRORCODE:5|ISVIP:0|VIPTY:-1|VIPLV:-1|UQ:HQ|RQ:HQ|DP:|DSRC:|DMOD:netsong2015|FROM:普通下载|CHANNEL_NAME:QDP2T1|PROD:MUSIC|VER:8.0.3.2_P2T1|PLAT:WIN32|FROM:kuwo_jm49.exe|UI:|{kuwo_jm49.exe}|K:75091848|RESEND:0|U:28072585>(118.100.15.118)TM:1468339199'
    mr_obj.LocalTest(strTest)
    pass