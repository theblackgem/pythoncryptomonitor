import requests
from time import sleep
import bs4
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook=input('Please enter your webhook here: ')

instock=False
def log_discord(title, message, field1_name, field1_value, footer, icon_url, webhook):
    url = f'{webhook}'
    webhook = DiscordWebhook(url=url)
    em = DiscordEmbed(title=title, description=message, color='86')
    em.add_embed_field(name=field1_name, value=field1_value, inline=True)
    em.set_footer(text=footer, icon_url=icon_url)
    webhook.add_embed(em)
    response = webhook.execute()

def log_discord2(title, message, field1_name, field1_value, footer, icon_url, webhook):
    url = f'{webhook}'
    webhook = DiscordWebhook(url=url)
    em = DiscordEmbed(title=title, description=message, color='0')
    em.add_embed_field(name=field1_name, value=field1_value, inline=True)
    em.set_footer(text=footer, icon_url=icon_url)
    webhook.add_embed(em)
    response = webhook.execute()

def log_discord3(title, message, field1_name, field1_value, footer, icon_url, webhook):
    url = f'{webhook}'
    webhook = DiscordWebhook(url=url)
    em = DiscordEmbed(title=title, description=message, color='16749824')
    em.add_embed_field(name=field1_name, value=field1_value, inline=True)
    em.set_footer(text=footer, icon_url=icon_url)
    webhook.add_embed(em)
    response = webhook.execute()

url = "https://www.coindesk.com/price/litecoin"

payload={}
headers = {
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

while True:

    response = requests.request("GET", url, headers=headers, data=payload)

    if "Bitcoin" in response.text:
        soup = BeautifulSoup(response.text, "lxml")
        price = soup.find(attrs = {"class": "price-large"})
        log_discord('LTC Price:' , f'{price.text}' ,  'Next update in:' , '10 minutes' , 'LTC Prices by BlackGemOG' , 'https://cryptologos.cc/logos/litecoin-ltc-logo.png' , webhook)
        print(f'LTC is {price.text}')

        url2 = "https://www.coindesk.com/price/bitcoin"

        payload={}
        headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }


        response1 = requests.request("GET", url2, headers=headers, data=payload)

        if "Bitcoin" in response1.text:
            soup = BeautifulSoup(response1.text, "lxml")
            price1 = soup.find(attrs = {"class": "price-large"})
            log_discord2('BTC Price:' , f'{price1.text}' ,  'Next update in:' , '10 minutes' , 'BTC Prices by BlackGemOG' , 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/BTC_Logo.svg/2000px-BTC_Logo.svg.png' , webhook)
            print(f'BTC is {price1.text}')

            url3 = "https://www.coindesk.com/price/ethereum"

            payload={}
            headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
            }

            response2 = requests.request("GET", url3, headers=headers, data=payload)

            if "Bitcoin" in response2.text:
                soup = BeautifulSoup(response2.text, "lxml")
                price3 = soup.find(attrs = {"class": "price-large"})
                log_discord3('ETH Price:' , f'{price3.text}' ,  'Next update in:' , '10 minutes' , 'ETH Prices by BlackGemOG' , 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Ethereum_logo_2014.svg/628px-Ethereum_logo_2014.svg.png' , webhook)
                print(f'ETH is {price3.text}')
                print('Next check in 10 minutes.')
                sleep(600)
