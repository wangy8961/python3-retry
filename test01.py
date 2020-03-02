import requests

from logger import logger


def main():
    url = 'http://127.0.0.1:5000/api/ping'  # 假设这是 Flask 后端接口服务，先关闭它

    try:
        resp = requests.get(url)
    except Exception as e:
        logger.error('Unable to establish connection with url({0}), exception: {1}'.format(url, e))
    else:
        resp_json = resp.json()
        if resp.status_code == 200:
            logger.info('Succeed to get response({0}) from url({1})'.format(resp_json, url))
        else:
            logger.error('Failed to get response from url({0}), status code: {1}'.format(url, resp.status_code))


if __name__ == '__main__':
    main()
