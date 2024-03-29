# 项目：hook_xstl.py
# 时间：2024-03-29 17:47:12
# 运行环境：python3.10.x
import sys
PYTHON_VERSION = ".".join(str(i) for i in sys.version_info[:2])
if PYTHON_VERSION != "3.10":
  print(f"【你的青龙python版本为{PYTHON_VERSION},请使用python3.10.x运行此脚本】")
  exit()
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64(b'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\n')))
except KeyboardInterrupt:
	exit()