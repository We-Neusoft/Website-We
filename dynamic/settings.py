# 站点属性及本地化配置
SITE_ID = 1
ROOT_URLCONF = 'dynamic.urls'

LANGUAGE_CODE = 'zh-cn'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = False

# 管理员及邮件预警配置
DEFAULT_FROM_EMAIL = 'django@we.neusoft.edu.cn'
SEND_BROKEN_LINK_EMAILS = True

MANAGERS = (
    ('We', 'we@nou.com.cn'),
    ('Zhao Lei', 'zhaolei10@nou.com.cn'),
    ('Sun Fulong', 'sunfulong@nou.com.cn'),
)

# 模板加载器及相关配置
TEMPLATE_LOADERS = (
    'django_linestripper.stripper.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

STRIPPER_CLEAR_LINE = True
TEMPLATE_DIRS = (
    '/data/publish/template',
)

# 中间件
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_linestripper.stripper.StripperMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

# 缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
