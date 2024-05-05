import os
from dotenv import load_dotenv
from unusualwhales.client import AuthenticatedClient
from unusualwhales.models import OffLitPriceLevel
from unusualwhales.api.stock import get_volume_by_price_level

load_dotenv('.env')
UW_API_TOKEN = os.environ.get("UW_API_TOKEN", None)

def main():

    client = AuthenticatedClient(base_url="https://api.unusualwhales.com", token=UW_API_TOKEN)
    with client as client:
        data: list[OffLitPriceLevel] = get_volume_by_price_level.sync(client=client, ticker="AAPL", date="2024-05-03")

    print(data)


if __name__ == '__main__':
    main()
