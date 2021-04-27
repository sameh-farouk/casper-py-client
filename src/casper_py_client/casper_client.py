from services import rpcs, sse

if __name__ == '__main__':
    node_ip = '104.131.104.36' # a node from local test network on DigitalOcean
    node_rpc_port = '40102'
    node_sse_port = '60101'
    # node_address = '178.238.235.196' # public node (Casper testnet)
    # node_rpc_port = '7777'
    print(f"################# communicating with {node_ip}:{node_rpc_port}")
    my_casper_client = rpcs.JsonRPCService(node_ip, node_rpc_port)
    print(f"################# calling /rpc/info_get_peers")
    print(my_casper_client.get_peers().ok)
    print()
    print(f"################# calling /rpc/info_get_status")
    print(my_casper_client.get_status().ok)
    print()
    print(f"################# calling /rpc/chain_get_block_latest")
    print(my_casper_client.get_block_latest().ok)
    print()
    print(f"################# calling /rpc/chain_get_block_by_hash")
    print(my_casper_client.get_block_by_hash(block_hash="c2c9dca3d275cda7801bb606abb3afe0da11afcade8b455239989278dbf09b0d").ok)
    print()
    print(f"################# calling /rpc/chain_get_block_by_height")
    print(my_casper_client.get_block_by_height(block_height=58754).ok)
    print()
    print(f"################# calling /rpc/info_get_deploy")
    print(my_casper_client.get_deploy("5c057122da06a44b54e41987f884ad2f8d1b71d5b2d41774aec68b674df043e5").ok)
    print()
    print(f"################# calling /rpc/state_get_auction_info")
    print(my_casper_client.get_auction_info().ok)
    print()
    print(f"################# calling /rpc/state_get_balance")
    print(my_casper_client.get_balance(state_root_hash = "21f8dee66391b978a537db4e3b45036ed0ef420e8d99d178f408fde4deffc109", purse_uref = "uref-1591be7b2d40adb7a691a27743b4a2a29b4d2b189e61ccf1caaaac88cdaaed19-007").ok)
    print()
    print(f"################# calling /rpc/chain_get_state_root_hash")
    print(my_casper_client.get_state_root_hash(block_hash="c2c9dca3d275cda7801bb606abb3afe0da11afcade8b455239989278dbf09b0d").ok)
    print()
    my_casper_client = sse.EventService(node_ip, node_sse_port)
    my_casper_client.print_stream()
