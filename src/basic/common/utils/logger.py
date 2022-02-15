# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : logger工具
# @Time  : 2021/10/22 21:22


import logging.handlers

log = None


class Logger:

    def __init__(self, all_log_file=None, warn_log_file=None, error_log_file=None):
        self.logger = logging.getLogger('my_log')
        self.logger.setLevel(logging.INFO)

        fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d] - %(message)s")

        # 控制台输出
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(fmt)
        self.logger.addHandler(console_handler)

        # all.log 输出
        if not all_log_file:
            all_log_file = '../../all.log'

        all_log_handler = logging.FileHandler(all_log_file, mode='w')
        all_log_handler.setLevel(logging.INFO)
        all_log_handler.setFormatter(fmt)
        self.logger.addHandler(all_log_handler)

        # warn.log 输出
        if warn_log_file:
            warn_log_handler = logging.FileHandler(warn_log_file, mode='w')
            warn_log_handler.setLevel(logging.WARN)
            warn_log_handler.setFormatter(fmt)
            self.logger.addHandler(warn_log_handler)

        # error.log 输出
        if error_log_file:
            error_log_handler = logging.FileHandler(error_log_file, mode='w')
            error_log_handler.setLevel(logging.ERROR)
            error_log_handler.setFormatter(fmt)
            self.logger.addHandler(error_log_handler)


def set_logger():
    global log
    if not log:
        logger = Logger('../../all.log')
        log = logger.logger


if __name__ == '__main__':
    set_logger()
    log.info('xxxxxxxxxxxxxxxx')
    log.warning('wwwwwwwwwwwwwwww')
    log.error('eeeeeeeeeeeeeeeeee')
