import requests
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
    elif order == 'nameOrder':
        table_data.sort(key=lambda x: x[0])  # Ordina per nome (alfabetico)

    if table_data:
        print(tabulate(table_data, headers=["Gioco", "Rating"], tablefmt="grid"))
    else:
        print("Nessun dato disponibile da stampare.")
    print("\nTotale giochi:", count)


def print_full_data(wishlist_data):
    if wishlist_data:
        print(wishlist_data)
    else:
        print("Nessun dato disponibile da stampare.")


def main():
    steamid = input("Inserisci ID Steam: ").strip()

    while True:
        mode = input("Vuoi tutto o semplice (nome+rating)? (scegli t/s) (default s): ").strip().lower()
        if mode in ['t', 's', '']:
            if mode == 's' or mode == '':
                mode = 'simple'
            else:
                mode = 'all'
            break
        else:
            print("Opzione non valida. Per favore scegli 'n' per tutto o 's' per semplice.")

    while True:
        order = input("Vuoi ordinato per nome o rating (n/r)? (default r): ").strip().lower()
        if order in ['n', 'r', '']:
            if order == 'r' or order == '':
                order = 'ratingOrder'
            else:
                order = 'nameOrder'
            break
        else:
            print("Opzione non valida. Per favore scegli 'n' per nome o 'r' per rating.")

    wishlist_data = get_wishlist_data(steamid)

    if mode == 'simple':
        print_name_and_rating(wishlist_data, order)
    elif mode == 'all':
        print_full_data(wishlist_data)


if __name__ == "__main__":
    main()
