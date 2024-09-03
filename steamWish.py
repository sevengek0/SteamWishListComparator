import requests
import argparse
import sys
from tabulate import tabulate

def get_wishlist_data(steamid):
    wishlist_data = {}
    page = 0
    while True:
        url = f"https://store.steampowered.com/wishlist/profiles/{steamid}/wishlistdata/?p={page}"
        response = requests.get(url)

        if response.status_code == 200:
            try:
                page_data = response.json()
                if not page_data:  # Se la pagina è vuota, esci dal ciclo
                    break
                wishlist_data.update(page_data)
                page += 1
            except ValueError:
                sys.exit("La risposta non è in formato JSON.")
        else:
            sys.exit(f"Errore HTTP {response.status_code}: {response.text}")

    return wishlist_data

def print_name_and_rating(wishlist_data, order):
    table_data = []
    count = 0
    for game_id, game_info in wishlist_data.items():
        name = game_info.get('name', 'N/A')
        rating = game_info.get('reviews_percent', 'N/A')
        table_data.append([name, f"Rating: {rating}"])
        count += 1

    if order == 'ratingOrder':
        table_data.sort(key=lambda x: (x[1], x[0]), reverse=True)
    elif order == 'ratingName':
        table_data.sort(key=lambda x: x[0])  # Ordina per nome (alfabetico)

    print(tabulate(table_data, headers=["Gioco", "Rating"], tablefmt="grid"))
    print("\nTotale giochi:", count)

def print_full_data(wishlist_data):
    print(wishlist_data)

def main():
    parser = argparse.ArgumentParser(description="Scarica la wishlist di un utente Steam e stampa i dati richiesti.")
    parser.add_argument('steamid', type=str, help="SteamID dell'utente")
    parser.add_argument('-mode', type=str, choices=['simple', 'all'], required=True,
                        help="Seleziona 'simple' per stampare nome e rating, 'all' per stampare tutti i dati")
    parser.add_argument('-order', type=str, choices=['rating', 'ratin'],
                        help="Ordina i risultati: 'rating' per rating decrescente, 'rating' per ordine alfabetico")

    args = parser.parse_args()

    wishlist_data = get_wishlist_data(args.steamid)

    if args.mode == 'simple':
        print_name_and_rating(wishlist_data, args.order)
    elif args.mode == 'all':
        print_full_data(wishlist_data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Errore: Devi fornire lo SteamID e un'opzione (-mode e eventualmente -order).\n"
                 "Formato corretto: python importWishlist.py XXXXXXXXXX -mode [-order]\n"
                 "Dove XXXXXXXXXX è lo SteamID\n"
                 "Dove -mode è 'simple' per nome e rating o 'all' per tutti i dati.\n"
                 "Dove -order è 'rating' per ordinamento per rating decrescente o 'rating' per ordinamento alfabetico.")
    main()
