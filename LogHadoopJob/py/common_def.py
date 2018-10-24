import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
WORD_COUNT="wc_"

IS_LINUX_FILE = False#True

#valid data followed
MT_VALUE_VALID_POSTFIX = '([^\|]*)\|'
#invalid data followed
MT_VALUE_INVALID_POSTFIX = '([^\|]*).*?'
MT_VALUE_U = r'\|U:([0-9]*)'
MT_VALUE_END = r'.*?$'
#get data between k1 and k2.
#k1,k2 must exist
def MT_VALUE_BETWEEN(k1,k2):
	return k1 + r':[^\|]*(.*)\|' + k2 + '.*?'

def MT_VALUE_BEFORE(key):
	return r'(.*)\|' + key + '.*?'