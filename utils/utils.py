import configparser
import os
import logging

# 项目根路径
rootPath = os.path.join(os.path.dirname(__file__), os.path.pardir)


class ConfigUtil:
    def __init__(self):
        pass

    @staticmethod
    def getValue(section, key):
        config = configparser.ConfigParser()
        config.read(rootPath + '/config/rookie.config', encoding='utf-8')

        value = config.get(section, key)
        return value


class LogUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_logger(log_name):
        """
        获取一个log对象
        :return:logger
        """
        # 获取一个logger对象
        logger = logging.getLogger()
        # 设置日志级别为DEBUG级
        logger.setLevel(logging.DEBUG)
        # 创建一个控制台输出handler
        stream_handler = logging.StreamHandler()
        # 创建一个文件handler
        file_handler = logging.FileHandler(rootPath + '/log/' + log_name + '.log')
        # 为两种handler设置输入格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        # 为logger添加handler
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

        return logger
