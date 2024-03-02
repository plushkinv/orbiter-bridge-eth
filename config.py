#то что ниже обязательно заполнить своими данными
proxy_use = 0 #  0 - не использовать, 1 - прокси без ссылки , 2 - прокси со ссылкой для смены ip
proxy_login = 'pludg74'
proxy_password = 'a2d0'
proxy_address = 'noxy.com'
proxy_port = '199'
proxy_changeIPlink = "h04"


#то что ниже желательно настроить под себя
minimal_need_balance = 0.01 # минимальный баланс на кошельке, который должен быть, чтобы начать с ним работу
bridge_all_money = False # True  если хотите перевести максимум из доступной суммы. False - будут действовать параметры ниже
ostavit_nativ = 0.002 # указывается в нативном токене сколько оставить на кошельке. Обязательно заложите сюда комиссию сети необходимую на отправку! Чтобы вывести токены с оптимизма указывайте в этом параметре хотя бы 0,0001. в остальных сетях можно от нуля.
bridge_min = 0.005  # ETH  в орбитре минимум   0.005 к этому прибавится комиссия моста 0,0015
bridge_max = 0.009  # ETH
# ["arbitrum" , "optimism", "scroll", "base", "linea", "zksyncera", "zkevm", "eth", "nova"]
networks_from = ["arbitrum" , "optimism", "scroll", "base", "linea", "zksyncera", "zkevm", "eth", "nova"]
networks_to = ["arbitrum" , "optimism", "scroll", "base", "linea", "zksyncera", "zkevm", "eth", "nova"]


#укажите паузу в работе между кошельками, минимальную и максимальную. 
#При смене каждого кошелька будет выбрано случайное число. Значения указываются в секундах
timeoutMin = 1 #минимальная 
timeoutMax = 3 #максимальная
#задержки между операциями в рамках одного кошелька
timeoutTehMin = 1 #минимальная 
timeoutTehMax = 2 #максимальная

max_gas_price = 100 #максимальная цена газа в сети эфир при которой выполняются транзакции . если будет больше то скрипт будет ждать когда цена снизится


#то что ниже можно менять только если понимаешь что делаешь
proxies = { 'all': f'http://{proxy_login}:{proxy_password}@{proxy_address}:{proxy_port}',}
if proxy_use:
    request_kwargs = {"proxies":proxies, "timeout": 120}
else:
    request_kwargs = {"timeout": 120}
gas_kef=1.2 #коэфициент допустимого расхода газа на подписание транзакций. можно выставлять от 1.3 до 2


rpc_links = {
    'eth': 'https://rpc.ankr.com/eth',
    'arbitrum': 'https://arb1.arbitrum.io/rpc',
    'optimism':  'https://rpc.ankr.com/optimism',
    'scroll':  'https://rpc.ankr.com/scroll',
    'base':  'https://rpc.ankr.com/base',
    'linea':  'https://rpc.linea.build',
    'zksyncera':  'https://rpc.ankr.com/zksync_era',
    'zkevm':  'https://rpc.ankr.com/polygon_zkevm',
    'nova':  'https://rpc.ankr.com/arbitrumnova',
}

