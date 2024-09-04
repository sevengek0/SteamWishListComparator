def compare_wishlists(wishlist_data1, wishlist_data2):
    common_games = {}

    for game_id, game_info1 in wishlist_data1.items():
        if game_id in wishlist_data2:
            game_info2 = wishlist_data2[game_id]
            common_games[game_id] = {
                'name': game_info1.get('name', 'N/A'),
                'rating_user1': game_info1.get('reviews_percent', 'N/A'),
                'rating_user2': game_info2.get('reviews_percent', 'N/A'),
                'release_string': game_info1.get('release_string', 'N/A'),
            }

    return common_games


def print_comparison(common_games):
    from tabulate import tabulate

    table_data = []
    for game_id, game_info in common_games.items():
        name = game_info['name']
        rating_user1 = game_info['rating_user1']
        rating_user2 = game_info['rating_user2']
        release_string = game_info['release_string']

        table_data.append([name, rating_user1, rating_user2, release_string])

    if table_data:
        print(tabulate(table_data, headers=["Gioco", "Rating Utente 1", "Rating Utente 2", "Data di Uscita"], tablefmt="grid"))
    else:
        print("Nessun gioco in comune trovato.")
