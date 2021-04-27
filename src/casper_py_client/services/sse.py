from urllib.parse import urlunsplit
from sseclient import SSEClient
import json
import pprint

class EventService:
    SSE_PATH = '/events'
    API_SCHEME = 'http'
    def __init__(self, ip, port):
        api_url = urlunsplit((EventService.API_SCHEME, f'{ip}:{port}', EventService.SSE_PATH, '', ''))
        self.messages = SSEClient(api_url)

    def print_stream(self):
        # The first message sent by the server to any new subscriber will be the API version.
        # All subsequent ones will be JSON-encoded events
        m1 = next(self.messages)
        if m1:
            print(f'connected, {m1}')
        for msg in self.messages:
            print(msg.id)
            pprint.pprint(json.loads(msg.data))
            #print(msg.dump())
