from urllib.parse import urlunsplit
from logging.config import dictConfig

from jsonrpcclient.clients.http_client import HTTPClient
from jsonrpcclient.requests import Request
from jsonrpcclient.exceptions import JsonRpcClientError

from .logging_conf import log_config

class JsonRPCService:
    RPCS_PATH = '/rpc'
    API_SCHEME = 'http'
    ENABLE_LOG = False
    RAISE_FOR_STATUS = False
    def __init__(self, ip, port):
        if JsonRPCService.ENABLE_LOG:
            dictConfig(log_config)
        api_url = urlunsplit((JsonRPCService.API_SCHEME, f'{ip}:{port}', JsonRPCService.RPCS_PATH, '', ''))
        self.client = HTTPClient(api_url)

    def send_request(self, request, raise_for_status=RAISE_FOR_STATUS):
        try:
            response = self.client.send(request)
        except JsonRpcClientError as e:
            if raise_for_status:
                raise
            return e.response
        
        return response.data

    def get_peers(self):
        request = Request('info_get_peers')
        response = self.send_request(request)
        return response
    
    def get_block_latest(self):
        request = Request('chain_get_block')
        response = self.send_request(request)
        return response

    def get_block_by_hash(self, block_hash):
        request = Request('chain_get_block', block_identifier = {
          'Hash': block_hash
        })
        response = self.send_request(request)
        return response

    def get_block_by_height(self, block_height):
        request = Request('chain_get_block', block_identifier = {
          'Height': block_height
        })
        response = self.send_request(request)
        return response

    def get_status(self):
        request = Request('info_get_status')
        response = self.send_request(request)
        return response
    
    def get_deploy(self, deploy_hash=None):
        request = Request('info_get_deploy', deploy_hash = deploy_hash) # need to test with real deploy hash
        response = self.send_request(request)
        return response
    
    def get_auction_info(self):
        request = Request('state_get_auction_info')
        response = self.send_request(request)
        return response

    # TODO: we need to be able to send the params with correct structure 
    # def get_item(self, account_hash, block_hash='null', path=[]):
    #     #request = Request('state_get_item', block_hash=block_hash, key=account_hash, path=path)
    #     json_request = '{"jsonrpc": "2.0", "method": "state_get_item", "id": 1, "params": [null, "account-hash-f2cb51ad800ce98648565db515d2231cfd2cf5aedff9f0035785eb7e7338784e"]}'
    #     response = self.send_request(json_request)
    #     return response
    
    def get_balance(self, state_root_hash, purse_uref):
        request = Request('state_get_balance', state_root_hash=state_root_hash, purse_uref=purse_uref)
        response = self.send_request(request)
        return response

    def get_state_root_hash(self, block_hash):
        request = Request('chain_get_state_root_hash', block_hash=block_hash)
        response = self.send_request(request)
        return response
