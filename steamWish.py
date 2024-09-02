import requests

def get_wishlist_data(steamid):
    url = f"https://store.steampowered.com/wishlist/profiles/{steamid}/wishlistdata/"
    risp = requests.get(url)
    print(risp.status_code)  # Controlla lo stato HTTP
    print(risp.text)         # Stampa il contenuto della risposta - Disordinato

    if risp.status_code == 200:
        try:
            wishlist_data = risp.json()
            return wishlist_data
        except ValErrore:
            return "La risposta non è in formato JSON."
    else:
        return f"Errore HTTP {risp.status_code}"

steamid = '76561198071394169'  # Da sostitudire con lo SteamID (non con il nome sull'URL)
                               # Per ottenere lo SteamID ho usato https://steamdb.info/calculator/
wishlist_data = get_wishlist_data(steamid)

print(wishlist_data)    # Stampa tutto
