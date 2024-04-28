ICECREAMSWAP_SMART_ROUTER_ABI = """[{"inputs":[{"name":"_factoryV2","internalType":"address","type":"address"},{"name":"_deployer","internalType":"address","type":"address"},{"name":"_factoryV3","internalType":"address","type":"address"},{"name":"_positionManager","internalType":"address","type":"address"},{"name":"_stableFactory","internalType":"address","type":"address"},{"name":"_stableInfo","internalType":"address","type":"address"},{"name":"_WETH9","internalType":"address","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"indexed":true,"name":"previousOwner","internalType":"address","type":"address"},{"indexed":true,"name":"newOwner","internalType":"address","type":"address"}],"name":"OwnershipTransferred","anonymous":false,"type":"event"},{"inputs":[{"indexed":true,"name":"factory","internalType":"address","type":"address"},{"indexed":true,"name":"info","internalType":"address","type":"address"}],"name":"SetStableSwap","anonymous":false,"type":"event"},{"stateMutability":"nonpayable","type":"fallback"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[],"name":"WETH9","stateMutability":"view","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"}],"name":"approveMax","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"}],"name":"approveMaxMinusOne","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"}],"name":"approveZeroThenMax","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"}],"name":"approveZeroThenMaxMinusOne","stateMutability":"payable","type":"function"},{"outputs":[{"name":"result","internalType":"bytes","type":"bytes"}],"inputs":[{"name":"data","internalType":"bytes","type":"bytes"}],"name":"callPositionManager","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"paths","internalType":"bytes[]","type":"bytes[]"},{"name":"amounts","internalType":"uint128[]","type":"uint128[]"},{"name":"maximumTickDivergence","internalType":"uint24","type":"uint24"},{"name":"secondsAgo","internalType":"uint32","type":"uint32"}],"name":"checkOracleSlippage","stateMutability":"view","type":"function"},{"outputs":[],"inputs":[{"name":"path","internalType":"bytes","type":"bytes"},{"name":"maximumTickDivergence","internalType":"uint24","type":"uint24"},{"name":"secondsAgo","internalType":"uint32","type":"uint32"}],"name":"checkOracleSlippage","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[],"name":"deployer","stateMutability":"view","type":"function"},{"outputs":[{"name":"amountOut","internalType":"uint256","type":"uint256"}],"inputs":[{"components":[{"name":"path","internalType":"bytes","type":"bytes"},{"name":"recipient","internalType":"address","type":"address"},{"name":"amountIn","internalType":"uint256","type":"uint256"},{"name":"amountOutMinimum","internalType":"uint256","type":"uint256"}],"name":"params","internalType":"struct IV3SwapRouter.ExactInputParams","type":"tuple"}],"name":"exactInput","stateMutability":"payable","type":"function"},{"outputs":[{"name":"amountOut","internalType":"uint256","type":"uint256"}],"inputs":[{"components":[{"name":"pool","internalType":"address","type":"address"},{"name":"tokenIn","internalType":"address","type":"address"},{"name":"tokenOut","internalType":"address","type":"address"},{"name":"recipient","internalType":"address","type":"address"},{"name":"amountIn","internalType":"uint256","type":"uint256"},{"name":"amountOutMinimum","internalType":"uint256","type":"uint256"},{"name":"sqrtPriceLimitX96","internalType":"uint160","type":"uint160"}],"name":"params","internalType":"struct IV3SwapRouter.ExactInputSingleParams","type":"tuple"}],"name":"exactInputSingle","stateMutability":"payable","type":"function"},{"outputs":[{"name":"","internalType":"uint256","type":"uint256"}],"inputs":[{"name":"","internalType":"address[]","type":"address[]"},{"name":"","internalType":"uint256[]","type":"uint256[]"},{"name":"","internalType":"uint256","type":"uint256"},{"name":"","internalType":"uint256","type":"uint256"},{"name":"","internalType":"address","type":"address"}],"name":"exactInputStableSwap","stateMutability":"payable","type":"function"},{"outputs":[{"name":"amountIn","internalType":"uint256","type":"uint256"}],"inputs":[{"components":[{"name":"path","internalType":"bytes","type":"bytes"},{"name":"recipient","internalType":"address","type":"address"},{"name":"amountOut","internalType":"uint256","type":"uint256"},{"name":"amountInMaximum","internalType":"uint256","type":"uint256"}],"name":"params","internalType":"struct IV3SwapRouter.ExactOutputParams","type":"tuple"}],"name":"exactOutput","stateMutability":"payable","type":"function"},{"outputs":[{"name":"amountIn","internalType":"uint256","type":"uint256"}],"inputs":[{"components":[{"name":"pool","internalType":"address","type":"address"},{"name":"tokenIn","internalType":"address","type":"address"},{"name":"tokenOut","internalType":"address","type":"address"},{"name":"recipient","internalType":"address","type":"address"},{"name":"amountOut","internalType":"uint256","type":"uint256"},{"name":"amountInMaximum","internalType":"uint256","type":"uint256"},{"name":"sqrtPriceLimitX96","internalType":"uint160","type":"uint160"}],"name":"params","internalType":"struct IV3SwapRouter.ExactOutputSingleParams","type":"tuple"}],"name":"exactOutputSingle","stateMutability":"payable","type":"function"},{"outputs":[{"name":"","internalType":"uint256","type":"uint256"}],"inputs":[{"name":"","internalType":"address[]","type":"address[]"},{"name":"","internalType":"uint256[]","type":"uint256[]"},{"name":"","internalType":"uint256","type":"uint256"},{"name":"","internalType":"uint256","type":"uint256"},{"name":"","internalType":"address","type":"address"}],"name":"exactOutputStableSwap","stateMutability":"payable","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[],"name":"factory","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[],"name":"factoryV2","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"enum IApproveAndCall.ApprovalType","type":"uint8"}],"inputs":[{"name":"token","internalType":"address","type":"address"},{"name":"amount","internalType":"uint256","type":"uint256"}],"name":"getApprovalType","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"result","internalType":"bytes","type":"bytes"}],"inputs":[{"components":[{"name":"token0","internalType":"address","type":"address"},{"name":"token1","internalType":"address","type":"address"},{"name":"tokenId","internalType":"uint256","type":"uint256"},{"name":"amount0Min","internalType":"uint256","type":"uint256"},{"name":"amount1Min","internalType":"uint256","type":"uint256"}],"name":"params","internalType":"struct IApproveAndCall.IncreaseLiquidityParams","type":"tuple"}],"name":"increaseLiquidity","stateMutability":"payable","type":"function"},{"outputs":[{"name":"result","internalType":"bytes","type":"bytes"}],"inputs":[{"components":[{"name":"token0","internalType":"address","type":"address"},{"name":"token1","internalType":"address","type":"address"},{"name":"fee","internalType":"uint24","type":"uint24"},{"name":"tickLower","internalType":"int24","type":"int24"},{"name":"tickUpper","internalType":"int24","type":"int24"},{"name":"amount0Min","internalType":"uint256","type":"uint256"},{"name":"amount1Min","internalType":"uint256","type":"uint256"},{"name":"recipient","internalType":"address","type":"address"}],"name":"params","internalType":"struct IApproveAndCall.MintParams","type":"tuple"}],"name":"mint","stateMutability":"payable","type":"function"},{"outputs":[{"name":"","internalType":"bytes[]","type":"bytes[]"}],"inputs":[{"name":"previousBlockhash","internalType":"bytes32","type":"bytes32"},{"name":"data","internalType":"bytes[]","type":"bytes[]"}],"name":"multicall","stateMutability":"payable","type":"function"},{"outputs":[{"name":"","internalType":"bytes[]","type":"bytes[]"}],"inputs":[{"name":"deadline","internalType":"uint256","type":"uint256"},{"name":"data","internalType":"bytes[]","type":"bytes[]"}],"name":"multicall","stateMutability":"payable","type":"function"},{"outputs":[{"name":"results","internalType":"bytes[]","type":"bytes[]"}],"inputs":[{"name":"data","internalType":"bytes[]","type":"bytes[]"}],"name":"multicall","stateMutability":"payable","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[],"name":"owner","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[],"name":"positionManager","stateMutability":"view","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"},{"name":"value","internalType":"uint256","type":"uint256"}],"name":"pull","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[],"name":"refundETH","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[],"name":"renounceOwnership","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"},{"name":"value","internalType":"uint256","type":"uint256"},{"name":"deadline","internalType":"uint256","type":"uint256"},{"name":"v","internalType":"uint8","type":"uint8"},{"name":"r","internalType":"bytes32","type":"bytes32"},{"name":"s","internalType":"bytes32","type":"bytes32"}],"name":"selfPermit","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"},{"name":"nonce","internalType":"uint256","type":"uint256"},{"name":"expiry","internalType":"uint256","type":"uint256"},{"name":"v","internalType":"uint8","type":"uint8"},{"name":"r","internalType":"bytes32","type":"bytes32"},{"name":"s","internalType":"bytes32","type":"bytes32"}],"name":"selfPermitAllowed","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"},{"name":"nonce","internalType":"uint256","type":"uint256"},{"name":"expiry","internalType":"uint256","type":"uint256"},{"name":"v","internalType":"uint8","type":"uint8"},{"name":"r","internalType":"bytes32","type":"bytes32"},{"name":"s","internalType":"bytes32","type":"bytes32"}],"name":"selfPermitAllowedIfNecessary","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"},{"name":"value","internalType":"uint256","type":"uint256"},{"name":"deadline","internalType":"uint256","type":"uint256"},{"name":"v","internalType":"uint8","type":"uint8"},{"name":"r","internalType":"bytes32","type":"bytes32"},{"name":"s","internalType":"bytes32","type":"bytes32"}],"name":"selfPermitIfNecessary","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"","internalType":"address","type":"address"},{"name":"","internalType":"address","type":"address"}],"name":"setStableSwap","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[],"name":"stableSwapFactory","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[],"name":"stableSwapInfo","stateMutability":"view","type":"function"},{"outputs":[{"name":"amountOut","internalType":"uint256","type":"uint256"}],"inputs":[{"name":"amountIn","internalType":"uint256","type":"uint256"},{"name":"amountOutMin","internalType":"uint256","type":"uint256"},{"name":"path","internalType":"address[]","type":"address[]"},{"name":"to","internalType":"address","type":"address"}],"name":"swapExactTokensForTokens","stateMutability":"payable","type":"function"},{"outputs":[{"name":"amountOut","internalType":"uint256","type":"uint256"}],"inputs":[{"name":"amountIn","internalType":"uint256","type":"uint256"},{"name":"amountOutMin","internalType":"uint256","type":"uint256"},{"name":"pools","internalType":"address[]","type":"address[]"},{"name":"tokenIn","internalType":"address","type":"address"},{"name":"tokenOut","internalType":"address","type":"address"},{"name":"to","internalType":"address","type":"address"}],"name":"swapExactTokensForTokensExternal","stateMutability":"payable","type":"function"},{"outputs":[{"name":"amountIn","internalType":"uint256","type":"uint256"}],"inputs":[{"name":"amountOut","internalType":"uint256","type":"uint256"},{"name":"amountInMax","internalType":"uint256","type":"uint256"},{"name":"path","internalType":"address[]","type":"address[]"},{"name":"to","internalType":"address","type":"address"}],"name":"swapTokensForExactTokens","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"},{"name":"amountMinimum","internalType":"uint256","type":"uint256"},{"name":"recipient","internalType":"address","type":"address"}],"name":"sweepToken","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"},{"name":"amountMinimum","internalType":"uint256","type":"uint256"}],"name":"sweepToken","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"},{"name":"amountMinimum","internalType":"uint256","type":"uint256"},{"name":"feeBips","internalType":"uint256","type":"uint256"},{"name":"feeRecipient","internalType":"address","type":"address"}],"name":"sweepTokenWithFee","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"token","internalType":"address","type":"address"},{"name":"amountMinimum","internalType":"uint256","type":"uint256"},{"name":"recipient","internalType":"address","type":"address"},{"name":"feeBips","internalType":"uint256","type":"uint256"},{"name":"feeRecipient","internalType":"address","type":"address"}],"name":"sweepTokenWithFee","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"newOwner","internalType":"address","type":"address"}],"name":"transferOwnership","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"amountMinimum","internalType":"uint256","type":"uint256"},{"name":"recipient","internalType":"address","type":"address"}],"name":"unwrapWETH9","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"amountMinimum","internalType":"uint256","type":"uint256"},{"name":"recipient","internalType":"address","type":"address"},{"name":"feeBips","internalType":"uint256","type":"uint256"},{"name":"feeRecipient","internalType":"address","type":"address"}],"name":"unwrapWETH9WithFee","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"amountMinimum","internalType":"uint256","type":"uint256"},{"name":"feeBips","internalType":"uint256","type":"uint256"},{"name":"feeRecipient","internalType":"address","type":"address"}],"name":"unwrapWETH9WithFee","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"value","internalType":"uint256","type":"uint256"}],"name":"wrapETH","stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]"""
ERC20_TOKEN_ABI = """[
    {
        "constant": true,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_spender",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_from",
                "type": "address"
            },
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            },
            {
                "name": "_spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "payable": true,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    }
]
"""
WETH9_TOKEN_ABI = """[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]"""
UNISWAP_V2_POOL_ABI = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
