
xn toolkit
==========

xntool has many convenient tools, use ``xntool --help`` to show more examples.


install
-------

usage:

.. code-block:: bash

    pip install xntool


Wiki
----


show honey words
++++++++++++++++

usage:

.. code-block:: bash

    xntool love


tail like
+++++++++

usage:

.. code-block:: bash

    xntool tail /var/log/web.log 'python'


convert Windows' CRLF into Unix's LF
++++++++++++++++++++++++++++++++++++

usage:

.. code-block:: bash

    xntool dos2unix /var/log/web.log


replace text in file
++++++++++++++++++++

usage:

.. code-block:: bash

    xntool replace data.txt python perl


evaluate file's md5
+++++++++++++++++++
usage:

.. code-block:: bash

    xntool md5 data.txt


upload picture to qiniu
+++++++++++++++++++++++

first login <http://www.qiniu.com/>, get your configuration and modify ``/usr/etc/xntool/xntool.conf`` :

.. code-block:: bash

    #  Access Key and Secret Key
    ACCESS_KEY = 'xxxxxxxxxxxxxxxx'
    SECRET_KEY = 'yyyyyyyyyyyyyyyy'
    # your URL
    URL_PRE = 'http://yidaospace.qiniudn.com/'
    # your bucket name
    BUCKET_NAME = 'yidaospace'


usage:

.. code-block:: bash

    xntool qiniu /tmp/pics

you can fetch the urls of uploaded pictures in ``url.txt``

More
++++

for more, please use ``xntool --help`` ...

Resources
+++++++++

* `GitHub repository <https://github.com/yidao620c/xntool>`_
* `Python User Guide <https://www.python.org/doc/>`_
