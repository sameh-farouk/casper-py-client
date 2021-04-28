# casper-py-client (WIP)
The purpose of the client is to help users interact with the Casper block-chain

## installation:
after clone the project
    1 - run `poetry install`
    2 - run `poetry shell`

## usage:
after cd into `src` directory you can run the client using `python3 casper_py_client` and it will give you hint about the available commands.

## examples:
- `python3 casper_py_client get-state-root-hash 104.131.104.36 40102`
- `python3 casper_py_client get-state-root-hash 104.131.104.36 40102 --block-hash 5835e228d53be2e81515a8a71e01456ed16eb598dc5fa5aab61689ab520c9e9a`
- `python3 casper_py_client get-balance 104.131.104.36 40102 --purse-uref uref-1591be7b2d40adb7a691a27743b4a2a29b4d2b189e61ccf1caaaac88cdaaed19-007`
