import sys
sys.path.append('../')

from samsungtv import SamsungTV

tv = SamsungTV('192.168.xxx.xxx')
tv.power() # this will return a token on the command line


#tv = SamsungTV('192.168.xxx.xxx', 'YYYYYYY') # using the token from above
