import fire
from casper_py_client.services import sse, rpcs
class Casper_Client:
    def get_state_root_hash(self, ip, port, block_hash=None):
        """Obtain the latest global state hash or the global state hash for specifc block.

        Args:
            ip (string): node ip
            port (int): node port
            block_hash (string, optional): hash of the block of interest. if None the hash of latest block will be used. Defaults to None.
        
        Returns:
            Dict: global state hash.
        """
        rpc_client = rpcs.JsonRPCService(ip, port)
        block = rpc_client.get_block_latest().result.get('block')
        if not block_hash:
            block_hash = block.get(hash)
        state_root_hash = rpc_client.get_state_root_hash(block_hash).result.get('state_root_hash')
        return state_root_hash

    def get_balance(self, ip, port, purse_uref):
        """Retrieve the token balance in the purse.

        Args:
            ip (string): node ip
            port (int): node port
            purse (string): purse uref

        Returns:
            Dict: The balance in motes (the unit that makes up the Casper token).
        """
        rpc_client = rpcs.JsonRPCService(ip, port)
        state_root_hash = self.get_state_root_hash(ip, port)
        balance_value = rpc_client.get_balance(state_root_hash, purse_uref).result.get('balance_value')
        return balance_value

if __name__ == '__main__':
    fire.Fire(Casper_Client)