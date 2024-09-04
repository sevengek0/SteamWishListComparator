def compare_wishlists(wishlist_data1, wishlist_data2):
    common_games = {}

    for game_id, game_info1 in wishlist_data1.items():
        if game_id in wishlist_data2:
            game_info2 = wishlist_data2[game_id]
            common_games[game_id] = {
                'name': game_info1.get('name', 'N/A'),
                'rating_user1': game_info1.get('reviews_percent', 'N/A'),
                'release_string': game_info1.get('release_string', 'N/A'),
            }

    return common_games


def print_comparison(common_games, username1, username2):
    from tabulate import tabulate

    table_data = []
    for game_id, game_info in common_games.items():
        name = game_info['name']
        rating_user1 = game_info['rating_user1']
        release_string = game_info['release_string']

        table_data.append([name, rating_user1, release_string])
        table_data.sort(key=lambda x: (x[1], x[0]), reverse=True) # ordina per rating

    if table_data:
        print(tabulate(table_data, headers=[f"Giochi [{username1} x {username2}]", "Rating", "Data di Uscita"], tablefmt="presto"))
    else:
        print("Nessun gioco in comune trovato.")
