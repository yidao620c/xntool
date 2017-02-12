
## 小熊工具箱

日积月累的各种小工具

### 安装
``` bash
pip install xntool
```

### 使用帮助

#### 每天一句情话
撩女朋友专用，^_^

使用示例：
``` bash
xntool love
```

#### tail查看关键字
使用示例：
``` bash
xntool tail /var/log/web.log 'python'
```

#### 将windows换行符转换成unix换行符
使用示例：
``` bash
xntool dos2unix /var/log/web.log
```

#### 内容替换
使用示例：
``` bash
xntool replace data.txt python perl
```

#### 文件的md5值
使用示例：
``` bash
xntool md5 data.txt
```

#### 七牛存储图片上传
首先进入你的七牛主页，拿到必要配置参数，修改`xqiniu.py`这个模块中的几个配置
``` python
# 需要填写你的 Access Key 和 Secret Key
ACCESS_KEY = 'xxxxxxxxxxxxxxxx'
SECRET_KEY = 'yyyyyyyyyyyyyyyy'
# 七牛空间URL
URL_PRE = 'http://yidaospace.qiniudn.com/'
# 要上传的空间名
BUCKET_NAME = 'yidaospace'
```

使用示例：
``` bash
xntool qiniu /tmp/pics
```
上传完后会自动删除图片并且将url写入图片目录下的url.txt最后

#### mysql schema转换为excel
将mysql数据库的schema.sql文件转换为excel格式的数据库设计文件。
使用示例：
``` bash
xntool gexcel /tmp/schema.excel /tmp/schema.sql
```
其中schema.sql文件格式示例：
```
-- -----------------------贷快发二期数据库-------------------------------
-- 公共用户表
DROP TABLE IF EXISTS t_public_user;
CREATE TABLE t_public_user (
  id                BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
  user_type         INTEGER COMMENT '用户类型 1:企业用户 2:个人用户',
  account           VARCHAR(20) NOT NULL COMMENT '账号',
  password          VARCHAR(32) NOT NULL COMMENT '密码',
  created_time      DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_time      DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '公共用户表';

-- 贷款申请表
DROP TABLE IF EXISTS t_apply;
CREATE TABLE t_apply (
  id                BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
  created_time      DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_time      DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '贷款申请表';
```

#### mysql schema转换为javabean
将mysql数据库的schema.sql文件转换为javabean源文件。
使用示例：
``` bash
xntool gjavabean /tmp/pkg/ pkg; /tmp/schema.sql
```
其中schema.sql文件格式示例同上


