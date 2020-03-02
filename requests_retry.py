import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,  # 重试 3 次时，总耗时 1.8 = 0 + 0.6 + 1.2 秒
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        method_whitelist=frozenset(['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS'])  # urllib3 默认对除 GET 以外的方法，不设置自动重试功能，所以要主动添加白名单
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session
