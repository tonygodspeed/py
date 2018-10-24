#!/usr/bin/env python
# coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "FIRST_PLAY"
class MR_FIRST_PLAY(mr_base_ex):
    def __init__(self):
        mr_base_ex.__init__(self,str_act)
        self.res_type = ["s","s","s","i","i"];
        self.res_name = ["SRC","UUID","UMAC","U"];

        '''
        mt_type = [
                      {'key':'SRC',    'type':'s', 'mt':r'^.*<SRC:' + common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END},
                  ]
        '''

mr_obj = MR_FIRST_PLAY()

if __name__ == '__main__':
    #test()
    #strTest = r'00:00| [INFO]: <SRC:MUSIC_8.4.1.0_PQ|ACT:FIRST_PLAY|S:KwMV|U:22166311|N:|T:0|NA:男人花|AR:黄勇|AL:男人花|F:PQ|B:0|D:0|RID:MUSIC_6212893|S1:3094916654|S2:3289885245|FV:|PF:0|UI:|DT:0|PSRC:FROM=曲库->"男人花  黄勇"的搜索结果->结果列表(17048)|radio_src:0|NOWPLAY:songlib|SCRN:1920*1080|ENPI:000|LSRC:|ISVIP:0|VIPTY:-1|VIPLV:-1|DLY:0|MTREE:0|GS:3|FSB:0|TMM:0|TMS:0|MULTI:0|RUUIDOPEN:0|UUID:{18599E5D-599B-4614-9912-C39148C52DD3}|UUMAC:488AD21110E6|TIMESTAMP:2016-08-23 20:47:27.724|BLKTM:0|BLKCNT:0|BR:0|FMT:ape|ENDTYPE:1|CT:|CACHE:1|CACHEDSZ:37015964|CTYPE:song1|PT:11188|DUR:310|SPEED:0|FSIZE:37015964|DELAY:1778|FDMT:842|FDMP:100|FSPT:1482|BLKPOS:0|STARTSIZE:2220957|AACRESULT:0|CHANNEL_NAME:150001_01|PROD:MUSIC|VER:8.4.1.0_PQ|PLAT:WIN32|FROM:酷我音乐_8.4.1.exe|UI:|{酷我音乐_8.4.1.exe}|K:33971616|RESEND:0|U:22166311>(124.237.35.12)TM:1473134399'
    strTest = r'[7872000][act][10-11 11:13:54.368][KNF]: SRC:test|ACT:FIRST_PLAY|S:KwMV|U:7872000|N:|T:0|NA:告白气球|AR:周杰伦|AL:周杰伦的床边故事|F:HQ|B:0|D:0|RID:MUSIC_7149583|S1:2795477102|S2:206663274|FV:|PF:0|UI:|DT:0|PSRC:VER=2015;FROM=曲库->"周杰伦  "的搜索结果->结果列表(17085)|radio_src:0|NOWPLAY:search|SCRN:1920*1080|ENPI:000|LSRC:|ISVIP:0|VIPTY:-1|VIPLV:-1|DLY:1|MTREE:0|GS:0|FSB:0|TMM:0|TMS:0|MULTI:0|UUID:95DCBC384A3A410882F5925E8580CACBp+yNDnsKcDizzaFptbXy+uaO6OgVnn88MZI=|UMAC:D4BED9DE24AE|BLKTM:0|BLKCNT:0|BR:0|FMT:wma|ENDTYPE:1|CT:|CACHE:1|CACHEDSZ:3471055|CTYPE:song1|PT:1029|DUR:215|SPEED:0|FSIZE:3471055|DELAY:312|FDMT:16|FDMP:100|FSPT:47|BLKPOS:0|STARTSIZE:208263|AACRESULT:0|GreenVer:0|CHANNEL_NAME:|PROD:MUSIC|VER:|PLAT:WIN32|FROM:KwMusic8.5.0.0_BCS1111.exe|UI:|{KwMusic8.5.0.0_BCS1111.exe}|K:53456655|RESEND:0|U:7872000'
    mr_obj.LocalTest(strTest)
    pass