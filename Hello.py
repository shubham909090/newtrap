def main():
    pass
    
from fyers_api import fyersModel
from fyers_api import accessToken
import os
import datetime
import pytz
import requests

import streamlit as st




st.title('My trap trading program')

client_id = st.text_input("Client ID", "Q55X3K2LKQ-100")
secret_key = st.text_input("Secret Key", "1CB3H0D61U")
redirect_uri = st.text_input("Redirect URI", "https://koolcart.in")


def get_access_token():
    if not os.path.exists("access_token.txt"):

        session=accessToken.SessionModel(client_id=client_id1,secret_key=secret_key1,redirect_uri=redirect_uri1,response_type="code", grant_type="authorization_code")
        response = session.generate_authcode()
        print("login url :", response)
        st.write("Login URL: ", response)
        auth_code = st.text_input("Enter auth code:")
        session.set_token(auth_code)
        access_token = session.generate_token()["access_token"]
        with open("access_token.txt","w") as f:
            f.write(access_token)
    else:
        with open("access_token.txt","r") as f:
            access_token=f.read()

    return access_token

fyers = fyersModel.FyersModel(client_id=client_id, token=get_access_token(),log_path="")


# Get the current date in IST
current_date = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).date()

# Create a datetime object for 9:15:00 AM of the current day in IST
target_time = datetime.datetime.combine(current_date, datetime.time(9, 20, 0))

# Convert the datetime object to epoch time
epoch_time = int(target_time.timestamp())



data = {
    'symbols': 'NSE:APOLLOHOSP-EQ,NSE:RELIANCE-EQ,NSE:ASIANPAINT-EQ,NSE:AXISBANK-EQ,NSE:BAJAJ-AUTO-EQ,NSE:BAJFINANCE-EQ,NSE:BAJAJFINSV-EQ,NSE:BPCL-EQ,NSE:BHARTIARTL-EQ,NSE:CIPLA-EQ,NSE:DIVISLAB-EQ,NSE:DRREDDY-EQ,NSE:EICHERMOT-EQ,NSE:HCLTECH-EQ,NSE:HDFCBANK-EQ,NSE:HDFCLIFE-EQ,NSE:HEROMOTOCO-EQ,NSE:HINDALCO-EQ,NSE:HINDUNILVR-EQ,NSE:ICICIBANK-EQ,NSE:ITC-EQ,NSE:INDUSINDBK-EQ,NSE:INFY-EQ,NSE:JSWSTEEL-EQ,NSE:KOTAKBANK-EQ,NSE:LT-EQ,NSE:M&M-EQ,NSE:MARUTI-EQ,NSE:SBILIFE-EQ,NSE:SBIN-EQ,NSE:SUNPHARMA-EQ,NSE:TCS-EQ,NSE:TATACONSUM-EQ,NSE:TATAMOTORS-EQ,NSE:TATASTEEL-EQ,NSE:TECHM-EQ,NSE:TITAN-EQ,NSE:UPL-EQ,NSE:ULTRACEMCO-EQ,NSE:WIPRO-EQ'
}


symbols = {'NSE:APOLLOHOSP-EQ': {'dhigh': None, 'dlow': None, 'lp': None},'NSE:RELIANCE-EQ': {'dhigh': None, 'dlow': None, 'lp': None},'NSE:ASIANPAINT-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:AXISBANK-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:BAJAJ-AUTO-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:BAJFINANCE-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:BAJAJFINSV-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:BPCL-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:BHARTIARTL-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:CIPLA-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:DIVISLAB-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:DRREDDY-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:EICHERMOT-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:HCLTECH-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:HDFCBANK-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:HDFCLIFE-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:HEROMOTOCO-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:HINDALCO-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:HINDUNILVR-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:ICICIBANK-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:ITC-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:INDUSINDBK-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:INFY-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:JSWSTEEL-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:KOTAKBANK-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:LT-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:M&M-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:MARUTI-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:SBILIFE-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:SUNPHARMA-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:TCS-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:TATACONSUM-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:TATAMOTORS-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:TATASTEEL-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:TECHM-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:TITAN-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:UPL-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:ULTRACEMCO-EQ': {'dhigh': None, 'dlow': None, 'lp': None}, 'NSE:WIPRO-EQ': {'dhigh': None, 'dlow': None, 'lp': None}}

trade_taken_symbols = set()
crossed_dlow_symbols = set()
symbol_sent=set()

# Telegram Bot API token and chat ID
telegram_token = '6157727579:AAF3SW7-IXO6Tiba-yvYGDtDz0K_7_LWd8c'
telegram_chat_id = '857279506'
telegram_chat_id2='580005518'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    params = {
        'chat_id': telegram_chat_id,
        'text': message
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print('Failed to send Telegram message')

def send_telegram_message_varun(message):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    params = {
        'chat_id': telegram_chat_id2,
        'text': message
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print('Failed to send Telegram message')

if 'running' not in st.session_state:
   st.session_state.running = False

if st.button('Stop', key='stop_button'):
        st.session_state.running = False

if st.button('Start', key='start_button'):
        st.session_state.running = True

while st.session_state.running:
    #check for the curront time in epoch
    current_time = int(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).timestamp())
    # if curront time is = to trigger time go ahead
    if current_time >= epoch_time:
        #take data from fyers
        mydata = fyers.quotes(data=data)
        for symbol in symbols:
            
            if symbol in trade_taken_symbols:
                #loop skiped if it's not found in the set()
                continue
            #if symbol dlow and dhigh are empty, then take the value from fyers data and put it, but this will only happen 1 time as, condition is "if none"
            if symbols[symbol]['dlow'] is None and symbols[symbol]['dhigh'] is None:
                for item in mydata.get('d', []):
                    if item['n'] == symbol:
                        symbols[symbol]['dhigh'] = item['v']['high_price']
                        symbols[symbol]['dlow'] = item['v']['low_price']
                        break
                    
            #takeing ltp value continuasly from fyers
            for item in mydata.get('d', []):
                if item['n'] == symbol:
                    symbols[symbol]['lp'] = item['v']['lp']

                    newhigh = item['v']['high_price']

                    #check if the ltp is lower than day low, and if soo, add that to the crossed below set
                    if symbols[symbol]['lp'] < symbols[symbol]['dlow'] and newhigh == symbols[symbol]['dhigh']:
                        #print(f"{symbols[symbol]['lp']} < {symbols[symbol]['dlow']} and {newhigh} == {symbols[symbol]['dhigh']}")
                        crossed_dlow_symbols.add(symbol)
                        if symbol not in symbol_sent:
                            send_telegram_message_varun(f"Crossed below 5 min trap: {symbol}")
                            symbol_sent.add(symbol)
                        break
                    # trade taken, but here above loop already told us that ltp is now below the low anymore and above condition will be skipped and this will be exicuted
                    if symbol in crossed_dlow_symbols and symbols[symbol]['lp'] > symbols[symbol]['dhigh'] and (symbols[symbol]['dhigh']-symbols[symbol]['dlow'])<=(symbols[symbol]['lp']*1/100):
                        
                        send_telegram_message(f"BUY Trade taken for symbol from trap buying: {symbol}")
                        datas = {
                                "symbol":symbol,
                                "qty":int(200/(float(symbols[symbol]['dhigh'])-float(symbols[symbol]['dlow']))),
                                "type":2,
                                "side":1,
                                "productType":"CO",
                                "limitPrice":0,
                                "stopPrice":0,
                                "validity":"DAY",
                                "disclosedQty":0,
                                "offlineOrder":"False",
                                "stopLoss":float(symbols[symbol]['dlow'])
                               }
                        response = fyers.place_order(data=datas)
                        print(response)
                        st.write(response)
                        if response['code'] != 200:
                            print(response)
                            st.write(response)
                        trade_taken_symbols.add(symbol)
                        break
            # if symbol is traded already then it won't be traded again
            if symbol in trade_taken_symbols:
                break
        # Check if all symbols have taken trade
        if set(symbols.keys()) == trade_taken_symbols:
            break
