import requests
from config import Config
from .models import Quotes

quotes_api = Config.QUOTES_API

def get_Quotes():
  random_quote = requests.get(quotes_api)
  new_quote = random_quote.json()
  author = new_quote.get("author")
  quote = new_quote.get("quote")
  permalink = new_quote.get("permalink")
  quote_item = Quotes(author,quote,permalink)
  return quote_item