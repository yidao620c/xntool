
## xn toolkit

many convenient tools, use `xntool help` to show more examples.

### install
``` bash
pip install xntool
```

### Wiki

#### show honey words

usage:
``` bash
xntool love
```

#### tail like
usage:
``` bash
xntool tail /var/log/web.log 'python'
```

#### convert Windows' CRLF into Unix's LF
usage:
``` bash
xntool dos2unix /var/log/web.log
```

#### replace text in file
usage:
``` bash
xntool replace data.txt python perl
```

#### evaluate file's md5
usage:
``` bash
xntool md5 data.txt
```

#### upload picture to qiniu
first login <http://www.qiniu.com/>, get your configuration and modify `/etc/xntool/xntool.conf` :
```
#  Access Key and Secret Key
ACCESS_KEY = 'xxxxxxxxxxxxxxxx'
SECRET_KEY = 'yyyyyyyyyyyyyyyy'
# your URL
URL_PRE = 'http://yidaospace.qiniudn.com/'
# your bucket name
BUCKET_NAME = 'yidaospace'
```

usage:
``` bash
xntool qiniu /tmp/pics
```
you can fetch the urls of uploaded pictures in `url.txt`

for more, please use `xntool help` ...

