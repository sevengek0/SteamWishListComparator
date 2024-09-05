from wishlist import get_wishlist_data, print_name_and_rating, print_full_data
from comparison import compare_wishlists, print_comparison

def main():

    utentiN = {}
    wishlistData = {}
    count = 0

    utentiN[count] = input("Inserisci ID Steam dell'utente 1: ").strip()
    compare_mode = input("Vuoi confrontare con un altri utenti? (s/n) (default n): ").strip().lower()

    if compare_mode == 's':

        ripeti = True

        while (ripeti):
            count += 1

            inputstr = input(f"Inserisci ID Steam dell'utente {count+1}: ").strip()

            if inputstr != '':
                utentiN[count] = inputstr
            else:
                ripeti = False

        count = 0
        for u in utentiN.values():

            wishlistData[count] = get_wishlist_data(u)
            count += 1

        common_games = compare_wishlists(wishlistData)

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

        #wishlist_data = get_wishlist_data(utentiN.)

        if mode == 'simple':
            print_name_and_rating(wishlist_data, order)
        elif mode == 'all':
            print_full_data(wishlist_data)


if __name__ == "__main__":
    main()
