import requests
import argparse
import sys
from tabulate import tabulate


def get_wishlist_data(steamid):
    url = f"https://store.steampowered.com/wishlist/profiles/{steamid}/wishlistdata/"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            wishlist_data = response.json()
            return wishlist_data
        except ValueError:
            sys.exit("La risposta non è in formato JSON.")
    else:
        sys.exit(f"Errore HTTP {response.status_code}: {response.text}")


def print_name_and_rating(wishlist_data, order):
    # Prepara i dati
    table_data = []
    for game_id, game_info in wishlist_data.items():
        name = game_info.get('name', 'N/A')
        rating = game_info.get('reviews_percent', 'N/A')
        table_data.append([name, f"Rating: {rating}"])

    # Ordina i dati
    if order == 'a':
        table_data.sort(key=lambda x: x[0])  # Ordina per nome (alfabetico)
    elif order == 'r':
        table_data.sort(key=lambda x: (x[1], x[0]), reverse=True)  # Ordina per rating (decrescente)

    # Stampa la tabella
    print(tabulate(table_data, headers=["Gioco", "Rating"], tablefmt="grid"))


def print_full_data(wishlist_data):
    print(wishlist_data)


def main():
    parser = argparse.ArgumentParser(description="Scarica la wishlist di un utente Steam e stampa i dati richiesti.")
    parser.add_argument('steamid', type=str, help="SteamID dell'utente")
    parser.add_argument('-N', type=str, choices=['n', 'a'], required=True,
                        help="Seleziona 'n' per stampare nome e rating, 'a' per stampare tutti i dati")
    parser.add_argument('-O', type=str, choices=['a', 'r'],
                        help="Ordina i risultati: 'a' per ordine alfabetico, 'r' per ordine per rating (decrescente)")

    args = parser.parse_args()

    # Recupera la wishlist
    wishlist_data = get_wishlist_data(args.steamid)

    # Stampa i dati secondo l'opzione scelta
    if args.N == 'n':
        print_name_and_rating(wishlist_data, args.O)
    elif args.N == 'a':
        print_full_data(wishlist_data)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Errore: Devi fornire lo SteamID e un'opzione (-n o -a).\n"
                 "Formato corretto: python importWishlist.py XXXXXXXXXX -N [-O]\n"
                 "Dove XXXXXXXXXX è lo SteamID\n"
                 "Dove -N è 'n' per nome e rating o 'a' per tutti i dati.\n"
                 "Dove -O è 'a' per ordinamento alfabetico o 'r' per ordinamento per rating (decrescente).")
    main()
