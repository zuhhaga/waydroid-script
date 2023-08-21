import requests
import requests_file
from os.path import isfile, realpath

class CacheHTTPAdapter(requests.adapters.HTTPAdapter):
    """The Base Transport Adapter"""
    
    def __init__(
        self,
        cachemap, hooks,
        pool_connections=requests.adapters.DEFAULT_POOLSIZE,
        pool_maxsize=requests.adapters.DEFAULT_POOLSIZE,
        max_retries=requests.adapters.DEFAULT_RETRIES,
        pool_block=requests.adapters.DEFAULT_POOLBLOCK
    ):
        
        if None == cachemap: cachemap={}
        if None == hooks: hooks={}
        self.cachemap = cachemap
        k=[]
        f_h = hooks.get('cache_found', k)
        nf_h = hooks.get('cache_not_found', k)
        if (callable(f_h)): f_h = (f_h,)
        if (callable(nf_h)): nf_h = (nf_h,)
        
        self.cache_found = f_h
        self.cache_not_found = nf_h
        self.adapter = requests_file.FileAdapter()
        super().__init__(
            pool_connections,
            pool_maxsize,
            max_retries,
            pool_block
        )
    def send(
        self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None
    ):
        path=request.url
        dr=self.cachemap
        path=dr.get(path)
        if None != path:
            k = realpath(path)
            b = isfile(k)
        else:
            b = False
        if not b:
            for i in self.cache_not_found:
                i(request, path)
            return super().send(request, stream, timeout, verify, cert, proxies)
        else:
            for i in self.cache_found:
                i(request, path)
            req=requests.Request(
                method=request.method,
                url='file://'+k,
                headers=request.headers,
                hooks=request.hooks
            )
            return self.adapter.send(req.prepare())

    def close(self):
        self.adapter.close()
        return super().close()


def Session(cachemap=None, hooks=None,
        pool_connections=requests.adapters.DEFAULT_POOLSIZE,
        pool_maxsize=requests.adapters.DEFAULT_POOLSIZE,
        max_retries=requests.adapters.DEFAULT_RETRIES,
        pool_block=requests.adapters.DEFAULT_POOLBLOCK
    ):
    adapter=CacheHTTPAdapter(
            cachemap,
            hooks,
            pool_connections,
            pool_maxsize,
            max_retries,
            pool_block
    )
    req = requests.Session()
    req.cachemap=cachemap
    req.cachehooks=hooks
    req.mount('http://',  adapter)
    req.mount('https://', adapter)
    return req

def cache_found_report_hook(request, path):
    print('Found cache for', request.url, 'at', path)
    
def cache_not_found_report_hook(request, path):
    print('Not found cache for', request.url, 'at', path)

debug_hooks={
'cache_found': [cache_found_report_hook],
'cache_not_found': [cache_not_found_report_hook]
}

def default():
    from cache import data
    return Session(data.url_cache, debug_hooks)

