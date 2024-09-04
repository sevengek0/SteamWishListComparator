from wishlist import get_wishlist_data, print_name_and_rating, print_full_data
from comparison import compare_wishlists, print_comparison

def main():
    steamid1 = input("Inserisci ID Steam dell'utente 1: ").strip()
    compare_mode = input("Vuoi confrontare con un altro utente? (s/n) (default n): ").strip().lower()

    if compare_mode == 's':
        steamid2 = input("Inserisci ID Steam dell'utente 2: ").strip()

        wishlist_data1 = get_wishlist_data(steamid1)
        wishlist_data2 = get_wishlist_data(steamid2)

        common_games = compare_wishlists(wishlist_data1, wishlist_data2)
        print_comparison(common_games)
    else:
        while True:
            mode = input("Vuoi tutto o semplice (nome+rating)? (scegli t/s) (default s): ").strip().lower()
            if mode in ['t', 's', '']:
                mode = 'simple' if mode in ['s', ''] else 'all'
                break
            else:
                print("Opzione non valida. Per favore scegli 't' per tutto o 's' per semplice.")

        while True:
            order = input("Vuoi ordinato per nome, rating o data (n/r/d)? (default r): ").strip().lower()
            if order in ['n', 'r', 'd', '']:
                order = 'ratingOrder' if order in ['r', ''] else 'nameOrder' if order == 'n' else 'releaseOrder'
                break
            else:
                print("Opzione non valida. Per favore scegli 'n' per nome o 'r' per rating.")

        wishlist_data = get_wishlist_data(steamid1)

        if mode == 'simple':
            print_name_and_rating(wishlist_data, order)
        elif mode == 'all':
            print_full_data(wishlist_data)


if __name__ == "__main__":
    main()
