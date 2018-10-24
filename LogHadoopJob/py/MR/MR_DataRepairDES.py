#!/usr/bin/env python
# coding=utf8

from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")

class MR_DATA_REPAIR_DES(mr_base):
    def __init__(self):
        mr_base.__init__(self,"","DataRepairDES")

    def InitReducer(self,value):
        print("========================"+value+"===================")
        print("type\tret")
        print("s\ts")

    def ProcessMapper(self,value):
        #print "reg ProcessMapper " + value
        words = value.split("|")
        r = ["T","RET"]
        dict = {}
        for word in words:
            if word.find(":") == -1:
                continue

            k,v = word.split(":",1)
            if len(v) > 0:
                for key in r:
                    if re.match(key,k, re.IGNORECASE):#.find(key) != -1:
                        dict[key] = v
                        r.remove(key)
                        break
            if len(r) == 0:
                break
        if len(r) == 0:
            line = dict["T"] + "\t" + dict["RET"]
            #config.appendlist(line)
            print(self.act_type + "\t" + line+"\n")

    def ProcessReducer(self,value):
        try:
            key, value = value.split('\t', 1)
            if len(value) > 0:
                print(value)
        except ValueError:
            return

mr_obj = MR_DATA_REPAIR_DES()