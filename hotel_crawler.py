from requests import get
from bs4 import BeautifulSoup


def main():
    f = open("abuja_hotels.txt", "w+")
    for i in range(2, 4):
        request_data = get(f'https://hotels.ng/hotels-in-abuja/abuja/{i}')
        soup = BeautifulSoup(request_data.text, 'lxml')
        soup = soup.find('div', {'id': 'topPicks'})
        hotel = soup.findAll('div', {'class': 'listing-hotels'})
        for items in hotel:
            hotel_name = items.find('h2', {'class': 'listing-hotels-name'})
            hotel_price = items.find(
                'p', {'class': 'listing-hotels-prices-discount'})
            hotel_address = items.find('p', {'class': 'listing-hotels-address'})
            if hotel_price:
                f.write(hotel_name.text.strip(' ') + '\n')
                f.write(hotel_price.text.strip(' ') + '\n')
                f.write(hotel_address.text.strip(' ') + '\n')
                f.write('\n')
                f.write('\n')
                print(hotel_name.text, hotel_price.text, i)
    f.close()


main()
