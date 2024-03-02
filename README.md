# Автор
PLushkin https://t.me/plushkin_blog        

**На чай с плюшками автору:**
Полигон, БСК, Арбитрум - любые токены - `0x79a266c66cf9e71Af1108728e455E0B1D311e95E`

Трон TRC-20 только USDT, остальное не доходит - `TEZG4iSmr31wWnvBixKgUN9Aax4bbgu1s3`

# Чё делает
Позволяет перегонять между сетей ETH через можно orbiter.finance  
Работает только с EVM сетями


# Настройка
Что бы избежать лищних проблем с ограничениями или блокировками, используйте ротируемые прокси
https://go.nodemaven.com/plushkinva

Промик на 2 бесплатных гигабайта FREE2G  при покупке трафика
Промик просто на 500mb без оплат и привязки карты FREE500

В настройках выбираете из каких сетей пополнить какую или какие. 
Скрипт работает в режиме ожидания, если на кошельке не достаточно токенов. Т.е. если на некоторых кошельках нет токенов для перевода, то Скрипт запишет в логах такие кошельки в файл no_money чтобы вы могли их пополнить, при этом будет ожидать их пополения, когда увидит на них токены то сделает бридж.

# Установка и запуск:

Linux/Mac - https://www.youtube.com/watch?v=8rJ-96cPFwU
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python main.py
```
Windows - https://www.youtube.com/watch?v=EqC42mnbByc
```
pip install virtualenv
virtualenv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python main.py
```


