#!/usr/bin/env python
# coding=utf8

from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")


class MR_REGDLL(mr_base):
    def __init__(self):
        mr_base.__init__(self, "", "REGDLL")

    def InitReducer(self,value):
        print("========================"+value+"===================")
        print("mac\tsrcid\tSuccess\tret\tsubRet\terr\textend")
        print("s\ts\ti\ti\ti\ts\ts")

    def ProcessMapper(self,value):
        #print "reg ProcessMapper " + value
        words = value.split("|")
        r = ["mac","srcid","Success","ret", "subRet", "err"]
        dict = {}

        mc = r'^.*<SRC:.*err:[^\|]*\|(.*)\|bUpd:.*$'
        m = re.match(mc,value)
        if m:
            dict["extend"] = m.group(1)

        if "extend" not in dict or len(dict["extend"]) == 0:
            dict["extend"] = "-1"

        for word in words:
            if word.find(":") == -1:
                continue

            k,v = word.split(":",1)
            #if len(v) > 0:
            for key in r:
                if re.match(key,k, re.IGNORECASE):#.find(key) != -1:
                    if len(v) == 0:
                        v = "0"
                    dict[key] = v
                    r.remove(key)
                    break
            if len(r) == 0:
                break

        while len(r)>0:
            if(r[0] == "subRet" or r[0] == "err"):
                dict[r[0]] = "-1"
                r.pop(0)
            else:
                break

        if len(r) == 0:
            line = dict["mac"] + "\t" + dict["srcid"] + "\t" + dict["Success"] + "\t" + dict["ret"] + "\t" + dict["subRet"] + "\t" + dict["err"] + "\t" + dict["extend"]
            #config.appendlist(line)
            print(self.act_type + "\t" + line+"\n")

    def ProcessReducer(self,value):
        try:
            key, value = value.split('\t', 1)
            if len(value) > 0:
                print(value)
        except ValueError:
            return

mr_obj = MR_REGDLL()

if __name__ == '__main__':
    mr_obj.LocalTest(r'<SRC:|ACT:REGDLL|Success:1|ret:0|subRet:0|TEST:1|OS:6.1.7601|Admin:1|X64:1|UAC:0|TOOLVER:1.3.1.8|srcid:MUSIC8120BCS46|err:||bUpd:0|S:|PROD:KWSHELLEXT|VER:|PLAT:WIN32|FROM:|GID:|CIN:|MAC:4487FC6A6907|X64:1|UAC:0|ADMIN:1|OS:6.1.7601|MN:rundll32.exe|INT:1970-01-01|{}|U:>(115.202.189.199)TM:1461985629')
    pass