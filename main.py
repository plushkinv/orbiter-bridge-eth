import decimal
from statistics import mean
import time
from web3 import Web3
import requests
import random
from datetime import datetime
import config
import fun
from fun import *




current_datetime = datetime.now()
print(f"\n\n {current_datetime}")
print(f'============================================= Плюшкин Блог =============================================')
print(f'subscribe to : https://t.me/plushkin_blog \n============================================================================================================\n')


keys_list = []
with open("private_keys.txt", "r") as f:
    for row in f:
        private_key=row.strip()
        if private_key:
            keys_list.append(private_key)

random.shuffle(keys_list)
i=0
for private_key in keys_list:
    i+=1
    if config.proxy_use == 2:
        while True:
            try:
                requests.get(url=config.proxy_changeIPlink)
                fun.timeOut("teh")
                result = requests.get(url="https://yadreno.com/checkip/", proxies=config.proxies)
                print(f'Ваш новый IP-адрес: {result.text}')
                break
            except Exception as error:
                print(' !!! Не смог подключиться через Proxy, повторяем через 2 минуты... ! Чтобы остановить программу нажмите CTRL+C или закройте терминал')
                time.sleep(120)

    flag_no_money = 1
    try:
        web3 = Web3(Web3.HTTPProvider(config.rpc_links["eth"], request_kwargs=config.request_kwargs))
        account = web3.eth.account.from_key(private_key)
        wallet = account.address     
    except Exception as error:
       log_error(f'Ошибка подключения в ноде: {error}')       
    log(f"I-{i}: Начинаю работу с {wallet}")

    random.shuffle(config.networks_from)
    for network_from in config.networks_from:

        try:
            web3 = Web3(Web3.HTTPProvider(config.rpc_links[network_from], request_kwargs=config.request_kwargs))
            account = web3.eth.account.from_key(private_key)
            wallet = account.address    
            balance = web3.eth.get_balance(wallet)
            balance_decimal = Web3.from_wei(balance, 'ether')
        except Exception as error:
            log_error(f'Ошибка подключения в ноде: {error}')   

        if balance_decimal < config.minimal_need_balance:
            log(f"{network_from}: low balance , меньше {config.minimal_need_balance}")          
            continue    

        if config.bridge_all_money:
            amount = balance_decimal - decimal.Decimal(config.ostavit_nativ * config.gas_kef)
        else:
            amount = random.uniform(config.bridge_min,config.bridge_max)
        if balance_decimal < decimal.Decimal(amount) + decimal.Decimal(config.ostavit_nativ):
            log(f"{network_from}: low balance")          
            continue

        j=0
        while True:
            j = j+1
            network_to = random.choice(config.networks_to)            
            if(network_to != network_from):
                break
            if j>100:
                log_error_critical("не могу выбрать network_to, массив пустой? или совпадает с networks_from")
                break
    
        log(f"Выбран маршрут {network_from} -> {network_to}")
        flag_no_money = 0
        value = web3.to_wei(amount, 'ether') // 10000 * 10000 + address[network_to]['orbiter_code']

        # ожидает подходящий газ
        wait_gas_price_eth()

        try:
            address_bridges = web3.to_checksum_address("0x80c67432656d59144ceff962e8faf8926599bcf8")
            gasPrice = web3.eth.gas_price

            transaction = {
                "chainId": web3.eth.chain_id,
                'from': wallet,
                'to': address_bridges,
                'value':value,
                'gasPrice': gasPrice,
                'nonce': web3.eth.get_transaction_count(wallet),
            }
            gasLimit = int(web3.eth.estimate_gas(transaction)* config.gas_kef)
            transaction['gas'] = gasLimit
            if fun.address[network_from]['type']:
                maxPriorityFeePerGas = web3.eth.max_priority_fee
                fee_history = web3.eth.fee_history(10, 'latest', [10, 90])
                baseFee=round(mean(fee_history['baseFeePerGas']))
                maxFeePerGas = maxPriorityFeePerGas + round(baseFee * config.gas_kef)

                del transaction['gasPrice']
                transaction['maxFeePerGas'] = maxFeePerGas
                transaction['maxPriorityFeePerGas'] = maxPriorityFeePerGas



            signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
            txn_hash = web3.to_hex(web3.eth.send_raw_transaction(signed_txn.rawTransaction))
            tx_result = web3.eth.wait_for_transaction_receipt(txn_hash)

            if tx_result['status'] == 1:
                log_ok(f'bridge OK: {address[network_from]["explorer"]}{txn_hash}')
                fun.delete_private_key_from_file("private_keys", private_key)
                fun.delete_wallet_from_file("bridge_false_pk", private_key)
                fun.delete_wallet_from_file("no_money_aw", wallet)
            else:
                log_error(f'bridge false: {address[network_from]["explorer"]}{txn_hash}')
                save_wallet_to("bridge_false_pk", private_key)
                keys_list.append(private_key)
            
        


        except Exception as error:
            fun.log_error(f'bridge false: {error}')    
            save_wallet_to("bridge_false_pk", private_key)
            keys_list.append(private_key)


        break

    if(flag_no_money):
        log_error("Не достаточно нативки на кошельке")
        # save_wallet_to("no_money", private_key)
        save_wallet_to("no_money_aw", wallet)
        keys_list.append(private_key)
        fun.timeOut("teh")  
        continue

    timeOut()
    

    
log("Ну типа все, кошельки закончились!")