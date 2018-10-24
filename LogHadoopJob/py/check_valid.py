import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import binascii;
import base64
import struct

SRC_KEY_MAP={
	'MUSIC_8.5.0.0_BCS48':'2016101811244647',#'2016101811240464',

}

def KwBase64_encode(strData,d_len,strKey):
    i = 0
    res = ""
    while i < d_len:
        j = 0
        while (i < d_len and j < len(strKey)):
            r = ord(list(strData)[i]) ^ ord(list(strKey)[j])
            i = i + 1
            j = j + 1
            res = res + chr(r)
    res = base64.b64encode(res)
    return res

def check_valid(src,value,mac):
	if src not in SRC_KEY_MAP:
		return "0";
	else:
		#print(SRC_KEY_MAP[src]);
		default_key = "2016101018370581"
		default_value = "E807E5486ECE462F83775690B4C078AD2jfUfl/+dx+yT2WnhPVAnOr7u16TnBg8"
		default_mac = "D8CB8A68A2AC"
		if mac == default_mac and value == default_value:
			return "1";
		else:
			default_key = SRC_KEY_MAP[src];
			guid = value[0:32]
			encode_value = value[32:];
			v = guid + mac;
			v = binascii.a2b_hex(v)
			checksum = 0;
			i = 0;
			while i < 22:
				checksum += ord(v[i]);
				i += 1;

			checksum = checksum & 0xFFFF
			bytes = struct.pack('h',checksum);
			v = v +bytes;
			ret = KwBase64_encode(v,24,default_key);
			if ret == encode_value:
				return "1";
			else:
				return "0";