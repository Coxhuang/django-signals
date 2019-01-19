

# django信号量

## #0 Blog

```
https://mp.csdn.net/mdeditor/86558817#
```

## #1 环境

```
python3.6
django==2.0.7
```

## #2 需求
- 老板要求,每次数据库迁移时,变量a自增
- 老板要求,每次数据库D有新的数据添加进去时,变量b自增
- ... ...

## #3 设置
### #3.1 新建一个django项目
### #3.2 配置文件
### #3.2.1 目录结构

```
.
├── app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── signal.py # 新增文件
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── signals
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates
```

### #3.2.2 修改./app/apps.py

```
from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        import app.signal # signal.py路径
```
### #3.2.3 修改./app/__init__.py

```
default_app_config = 'app.apps.AppConfig' # apps.py文件中类名
```
### #3.2.4 新增./app/signal.py


```
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db.backends.signals import connection_created
from django.db.models.signals import pre_migrate, post_migrate
from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception
from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate
from django.test.signals import setting_changed
from django.test.signals import template_rendered
from django.db.backends.signals import connection_created

@receiver(post_migrate)
def callback_post_migrate(sender, **kwargs):
    print("这里是--post_migrate--")
    return None

```

### #3.3 效果

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190120005020392.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NveGh1YW5n,size_16,color_FFFFFF,t_70)

## #4 其他触发机制

**Model signals**

```
pre_init                    # django的modal执行其构造方法前，自动触发
post_init                   # django的modal执行其构造方法后，自动触发
pre_save                    # django的modal对象保存前，自动触发
post_save                   # django的modal对象保存后，自动触发
pre_delete                  # django的modal对象删除前，自动触发
post_delete                 # django的modal对象删除后，自动触发
m2m_changed                 # django的modal中使用m2m字段操作第三张表（add,remove,clear）前后，自动触发
class_prepared              # 程序启动时，检测已注册的app中modal类，对于每一个类，自动触发
```

**Management signals**

```
pre_migrate                 # 执行migrate命令前，自动触发
post_migrate                # 执行migrate命令后，自动触发
```

**Request/response signals**

```
request_started             # 请求到来前，自动触发
request_finished            # 请求结束后，自动触发
got_request_exception       # 请求异常后，自动触发
```

**Test signals**

```
setting_changed             # 使用test测试修改配置文件时，自动触发
template_rendered           # 使用test测试渲染模板时，自动触发
```


**Database Wrappers**

```
connection_created          # 创建数据库连接时，自动触发
```




**导入**
```
from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception
from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate
from django.test.signals import setting_changed
from django.test.signals import template_rendered
from django.db.backends.signals import connection_created

@receiver(post_migrate)
def callback_post_migrate(sender, **kwargs):
    print("这里是--post_migrate--")
    return None
```



