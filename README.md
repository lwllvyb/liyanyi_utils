
## build pip package

```
python setup.py bdist_egg     # 生成类似 xxx-0.0.1-py2.7.egg，支持 easy_install 
python setup.py sdist         # 生成类似 xxx-0.0.1.tar.gz，支持 pip
```

## install package

easy_install xxx-0.0.1-py2.7.egg

## example


```python

import logging
from liyanyi_utils.utils import new_logger

logger = new_logger("weixin_server.log", "weixin_server")
logger.setLevel(logging.INFO)

```