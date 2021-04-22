from urllib.parse import urlunsplit
from sseclient import SSEClient
import json
import pprint

class CasperSSEClient:
    SSE_PATH = '/events'
    API_SCHEME = 'http'
    def __init__(self, node_address):
        api_url = urlunsplit((CasperSSEClient.API_SCHEME, node_address, CasperSSEClient.SSE_PATH, '', ''))
        self.messages = SSEClient(api_url)


if __name__ == '__main__':
    my_casper_client = CasperSSEClient('104.131.104.36:60101')
    m1 = next(my_casper_client.messages)
    if m1:
        print(f'connected, {m1}')
    for msg in my_casper_client.messages:
        print(msg.id)
        pprint.pprint(json.loads(msg.data))
        #print(msg.dump())