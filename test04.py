from tornado import httpclient, ioloop

from async_retry import async_retry
from logger import logger


@async_retry()
async def async_call_api(request, **kwargs):
    """支持异步重试功能"""
    httpclient.AsyncHTTPClient.configure(None, max_clients=1000)
    http_client = httpclient.AsyncHTTPClient()
    resp = await http_client.fetch(request, **kwargs)
    return resp


async def main():
    url = 'http://127.0.0.1:5000/api/ping'  # 假设这是 Flask 后端接口服务，先关闭它

    try:
        resp = await async_call_api(url, method='GET', connect_timeout=5, request_timeout=60)
    except Exception as e:
        logger.error('Failed to get response from url({0}), exception: {1}'.format(url, e))
    else:
        if resp.status_code == 200:
            logger.info('Succeed to get response({0}) from url({1})'.format(resp, url))
        else:
            logger.error('Failed to get response from url({0}), status code: {1}'.format(url, resp.status_code))


if __name__ == '__main__':
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)
