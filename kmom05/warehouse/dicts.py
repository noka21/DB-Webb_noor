"""
HEre
"""
from operator import itemgetter


def id_to_key(id_, warehouse):
    """
    here
    """
    for key, data in warehouse.items():
        if id_ == data["ids"][0]:
            return key, data


def sort_by_price(prices, warehouse):
    """
    sortera värde
    """
    # print(sorted(prices.items()))  # here send only one argument, sort the key
    #print(sorted(prices.items(), key=itemgetter(1)))
    # sorted funktion kan vi skicka två värde, med itemgetter kan vi ha value
    sorted_prices = sorted(prices.items(), key=itemgetter(1), reverse=True)
    for id_, price in sorted_prices:
        name , data = id_to_key(id_, warehouse)
        print(
            f"{name} kostart {price}, det finns {data['stock']} kvar på hyllaplatsen {data['ids'][1]}")


if __name__ == "__main__":
    prices_dic = {
        1234: 50,
        4224: 10,
        3141: 20,
        2742: 5,
    }
    warehouse_deluxe = {
        "köttfärs": {"stock": 20, "ids": (1234, "K14")},
        "grädde": {"stock": 80, "ids": (3141, "L12")},
        "krossade tomater": {"stock": 33, "ids": (4224, "E13")},
        "gul lök": {"stock": 42, "ids": (2742, "D02")}
    }
    sort_by_price(prices_dic, warehouse_deluxe)
