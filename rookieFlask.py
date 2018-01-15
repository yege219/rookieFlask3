from flask import Flask
from utils.utils import LogUtil, ConfigUtil
import logging

app = Flask(__name__)

logger = LogUtil.getLogger('rookieFl')
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/testLog', methods=['POST'])
def test_log():
    logger.info("这是我的日志信息")
    logger.info(ConfigUtil.getValue('SectionB', 'key2'))

    return "finish"


@app.route('/testConfig')
def test_config():
    value = ConfigUtil.getValue(section='SectionA', key='a')
    logger.info(value)
    return value


if __name__ == '__main__':
    app.run()
