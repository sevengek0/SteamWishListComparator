import requests
import sys
from tabulate import tabulate


def get_wishlist_data(steamid):
    wishlist_data = {}
    page = 0
    typeid = "profiles"

    url = f"https://store.steampowered.com/wishlist/{typeid}/{steamid}/wishlistdata/?p={page}"
    response = requests.get(url)
    if response.status_code != 200:
        typeid = "id"

    while True:
        url = f"https://store.steampowered.com/wishlist/{typeid}/{steamid}/wishlistdata/?p={page}"
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
        rel_str = game_info.get('release_string', 'N/A')
        rel_val_str = game_info.get('release_date', None)

        if rel_val_str is None:
            rel_val = 0  # Assegna un valore di default se rel_val_str è None
        else:
            try:
                # Converte rel_val_str in intero
                rel_val = int(rel_val_str)
                # print(f"{count} {rel_val}" )
            except ValueError:
                # Se non può essere convertito, assegna valore default 0
                rel_val = 0

        table_data.append([f"{name}", f"Rating: {rating}", f"{rel_str}", f"int: {rel_val}"])
        count += 1

    if order == 'ratingOrder':
        table_data.sort(key=lambda x: (x[1], x[3]), reverse=True)
    elif order == 'nameOrder':
        table_data.sort(key=lambda x: x[0])  # Ordina per nome (alfabetico)
    elif order == 'releaseOrder':
        table_data.sort(key=lambda x: (x[3], x[2]), reverse=False)      # Ordina per data di release DataVal(int) e per rel_str

    # Rimuovi la colonna DataVal (ultimo elemento) dopo l'ordinamento
    table_data = [row[:-1] for row in table_data]

    if table_data:

        print(tabulate(table_data, headers=["Gioco", "Rating", "Data"], tablefmt="grid"))
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
        order = input("Vuoi ordinato per nome, rating o data (n/r/d)? (default r): ").strip().lower()
        if order in ['n', 'r', 'd', '']:
            if order == 'r' or order == '':
                order = 'ratingOrder'
            elif order == 'n':
                order = 'nameOrder'
            else:
                order = 'releaseOrder'
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
