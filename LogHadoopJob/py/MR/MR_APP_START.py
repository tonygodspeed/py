#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")
condition = os.environ.get('condition')

str_act = "AppStart"
class MR_APP_START(mr_base):
    def __init__(self):
        mt_type = [
                      {'key':'SRC',    'type':'s',  'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'NONE',     'type':'s',  'mt':r'PROD:kwplayer.*PLAT:ar.*'},
                      {'key':'U',      'type':'i',  'mt':r'U:' + common_def.MT_VALUE_VALID_POSTFIX},
                      {'key':'IMEI',   'type':'s',  'mt':r'IMEI:' + common_def.MT_VALUE_INVALID_POSTFIX}, #maybe invalid value
                      {'key':'DEV',    'type':'s',  'mt':r'DEV:' + common_def.MT_VALUE_VALID_POSTFIX},
                      {'key':'OSV',    'type':'s',  'mt':r'OSV:' + common_def.MT_VALUE_INVALID_POSTFIX + "$"},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_APP_START()

if __name__ == '__main__':
    strTest = r'<SRC:kwplayer_ar_7.8.1.0|ACT:PLAY_MUSIC|PROD:kwplayer|VER:7.8.1.0|PLAT:ar|FROM:kwplayer_ar_7.8.1.0_kwltc.apk|OLDFROM:kwplayer_ar_7.8.1.0_kwltc.apk|{kwplayer_ar_7.8.1.0_kwltc.apk}|ERR:PLAY_MUSIC|SUBERR:0|UI:0|UDID:|DEVID:866002023516809|U:50642862|IMEI:866002023516809|MACADDR:38:bc:1a:b8:23:75|UUID:|DEV:Meizu MX4 Pro mx4pro|OSV:4.4.4|NE:WIFI|NE_TYPE:WIFI|WIFI_ONLY:false|CT:2016/05/24 14:16:59.554 +0800|CIP:111.207.202.7|PU:50642862|DEP:1|MEM:3017580544|OFFLN:0|UNICOMFLOW:0|PROJECT:0|LOC:40.001871;116.390014|GPS:40.001871;116.390014|DBG:0|ABGROUP:|NONE:守护家|AR:TFBOYS|AL:守护家|RID:7095180|DUR:225|T:0|CTYPE:song0|PT:0|DELAY:3373|BLKTM:0|BLKCNT:0|BR:0|FMT:null|CACHE:1|LSRC:播放队列|PSRC:乐库->今日精华->5月24日最新单曲-<PID_1082685104;SEC_-1;POS_-1;DIGEST_8>(20160524)|FISIZE:0|SPEED:0|ENDTYPE:1|MEM:3017580544|LISTENSAVE:false>'
    mr_obj.LocalTest(strTest)
    pass
