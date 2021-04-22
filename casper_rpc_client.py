from urllib.parse import urlunsplit
import logging
from logging.config import dictConfig

from jsonrpcclient.clients.http_client import HTTPClient
from jsonrpcclient.requests import Request
from jsonrpcclient.exceptions import JsonRpcClientError

from casper_logging import log_config


class CasperRPCClient:
    RPCS_PATH = '/rpc'
    API_SCHEME = 'http'
    ENABLE_LOG = True
    RAISE_FOR_STATUS = False
    def __init__(self, node_address):
        if CasperRPCClient.ENABLE_LOG:
            dictConfig(log_config)
        api_url = urlunsplit((CasperRPCClient.API_SCHEME, node_address, CasperRPCClient.RPCS_PATH, '', ''))
        self.client = HTTPClient(api_url)

    def send_request(self, request, raise_for_status=RAISE_FOR_STATUS):
        try:
            response = self.client.send(request)
        except JsonRpcClientError as e:
            if raise_for_status:
                raise
            return e.response
        
        return response.data

    def info_get_peers(self):
        request = Request('info_get_peers')
        response = self.send_request(request)
        return response
    
    def chain_get_block(self, block_hash=None):
        request = Request('chain_get_block', block_hash = block_hash)
        response = self.send_request(request)
        return response

    def info_get_status(self):
        request = Request('info_get_status')
        response = self.send_request(request)
        return response
    
    def info_get_deploy(self, deploy_hash=None):
        request = Request('info_get_deploy', deploy_hash = deploy_hash)
        response = self.send_request(request)
        return response

if __name__ == '__main__':
    node_address = '104.131.104.36:40102'
    print(f"################# communicating with {node_address}")
    my_casper_client = CasperRPCClient('104.131.104.36:40102')
    print(f"################# calling /rpc/info_get_peers")
    print(my_casper_client.info_get_peers().ok)
    print()
    print(f"################# calling /rpc/info_get_status")
    print(my_casper_client.info_get_status().ok)
    print()
    print(f"################# calling /rpc/chain_get_block")
    print(my_casper_client.chain_get_block().ok)
    print()
    print(f"################# calling /rpc/chain_get_block with a parameter")
    print(my_casper_client.chain_get_block("5c057122da06a44b54e41987f884ad2f8d1b71d5b2d41774aec68b674df043e5").ok)
    print()
    print(f"################# calling /rpc/info_get_deploy")
    print(my_casper_client.info_get_deploy("5c057122da06a44b54e41987f884ad2f8d1b71d5b2d41774aec68b674df043e5").ok)
    print()
