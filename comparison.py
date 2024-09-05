
def compare_wishlists(wishlists_data):
    common_games = {}

    # Itera attraverso tutte le wishlist
    for single_wishlist_data in wishlists_data.values():
        for game_id, game_info in single_wishlist_data.items():
            # Se il gioco è già presente, incrementa il contatore dei giocatori
            if game_id in common_games:
                common_games[game_id]['players_count'] += 1
            else:
                # Se il gioco non è presente, inizializza il contatore a 1
                common_games[game_id] = {
                    'name': game_info.get('name', 'N/A'),
                    'rating': game_info.get('reviews_percent', 'N/A'),
                    'release_string': game_info.get('release_string', 'N/A'),
                    'players_count': 1  # Numero di giocatori che hanno il gioco nella wishlist
                }

    # Filtra i giochi che sono nella wishlist di più di un giocatore
    common_games = {game_id: info for game_id, info in common_games.items() if info['players_count'] > 1}

    return common_games


def print_comparison(common_games):
    from tabulate import tabulate

    table_data = []
    for game_id, game_info in common_games.items():
        name = game_info['name']
        rating = game_info['rating']
        release_string = game_info['release_string']
        players_count = game_info['players_count']

        table_data.append([name, rating, release_string, players_count])
        table_data.sort(key=lambda x: (x[3], x[1]), reverse= True)  # ordina per condivisione e rating

    if table_data:
        print(tabulate(table_data, headers=[f"Gioco", "Rating", "Uscita", "in x wishlist "], tablefmt="presto"))
    else:
        print("Nessun gioco in comune trovato.")
