import logging
import logging.handlers
import os

import coloredlogs


# 获取默认 Logger 实例
root_logger = logging.getLogger()
# 创建应用程序中使用的实例
logger = logging.getLogger('App')

# 设置日志格式
fmt = '%(asctime)s - [%(name)+24s] - %(filename)+18s[line:%(lineno)5d] - %(levelname)+8s: %(message)s'
formatter = logging.Formatter(fmt)

# 创建输出到控制台的 Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 创建输出到日志文件的 Handler，按时间周期滚动
basedir = os.path.abspath(os.path.dirname(__file__))
log_dest = os.path.join(basedir, 'logs')  # 日志文件所在目录
if not os.path.isdir(log_dest):
    os.mkdir(log_dest)
filename = os.path.join(log_dest, 'app.log')
file_handler = logging.handlers.TimedRotatingFileHandler(filename,
                                                         when='midnight',
                                                         interval=1,
                                                         backupCount=7,
                                                         encoding='utf-8')
file_handler.setFormatter(formatter)

# 为实例添加 Handler
root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)

# 设置日志级别
root_logger.setLevel(logging.DEBUG)

# 当日志输出到控制台时，会带有颜色
coloredlogs.DEFAULT_FIELD_STYLES = dict(
    asctime=dict(color='green'),
    name=dict(color='blue'),
    filename=dict(color='magenta'),
    lineno=dict(color='cyan'),
    levelname=dict(color='black', bold=True),
)
coloredlogs.install(fmt=fmt, level='DEBUG', logger=root_logger)
