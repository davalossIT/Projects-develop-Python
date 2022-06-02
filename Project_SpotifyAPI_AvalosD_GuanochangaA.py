import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials

#Credenciales 
client_ID ="cbce6bcb341c48b5a37da3aafb438331"
client_secret ="2900424a6dff459aa9cf8e59455e4a3c"


#Autenticación
spotipy= spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_ID, client_secret=client_secret))
# # # # # # # # # # # # # # # # # # # # # # # # # # 
# TODO: Búsqueda de Songs con "rock" 
# # # # # # # # # # # # # # # # # # # # # # # # # # 
results=  spotipy.search(q="rock", limit=50, type="track", market="BR")
resultsdef2= spotipy.search(q="pop", limit=10, type="track", market="EC")
resultsdef3= spotipy.search(q="country", limit=5, type="track", market="CA")



print('Keys for results')
print(results.keys()),"\n"

print('Key for results ["Tracks"]:')
print(results["tracks"].keys(), "\n")

print('Keys for results["tracks"]["items"]')
print(results["tracks"]["items"][0].keys(), "\n")

print('Keys for results["tracks"]["items"][0]["artists"][0]:')
print(results["tracks"]["items"][0]["artists"][0].keys(),"\n")

print("""                                                                                                                                                        
  _   _   _   _   _   _   _   _   _     _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ 
( C | O | N | S | U | L | T | A | S ) ( A | P | I )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ 
  _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ 
( S | P | O | T | I | F | Y )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
      """)

print("\n")

def obtain_Tn_IdT_An_IdA():
  
    print("_______________________La 1ª Funcion Obtiene e imprime los siguientes campos:_________________________ ")
    print(">>Nombre del Track<<"+ "       >>Identificador id Track<<"+  "    >>Nombre del artista <<"+"    >>Identificador id Artista<<")
    for item in results["tracks"]["items"]:
        track_name=item["name"]
        track_id=item["id"]
        
        
        artist_name=item["artists"][0]["name"]
        artist_id=item["artists"][0]["id"]
        
        if len(track_name)>=40:
            track_name=track_name[:37]
            track_name+= "....."
        
        print("{:40s} - {} - {:20s} - {}".format(track_name,track_id,artist_name,artist_id))
        

obtain_Tn_IdT_An_IdA()

print("\n")
#######################################?##########################################################################################

def obtain_Tn_PT_Tnum_Texp():
  
    print("_____________________La 2ª Funcion Obtiene e imprime los siguientes campos:___________________________ ")
    print(">>Nombre del Track<<"+ "       >>Popularidad Track<<"+  "    >>Numero del track<<"+"    >>Tipo de Track[Explicit]<<")

    for item in resultsdef2["tracks"]["items"]:
        track_name=item["name"]
        track_popularity=item["popularity"]
        track_number=item["track_number"]
        track_explicit=["explicit"]
        

        if len(track_name)>=30:
            track_name=track_name[:25]
            track_name+= "ªªªªªªªªª"
        
              
        print("{:40} / {} / {:20} / {}".format(track_name,track_popularity,track_number,track_explicit))
        
obtain_Tn_PT_Tnum_Texp()

print("\n")
#######################################!##########################################################################################

def obtain_Tn_DT_UE_UP():
  
    print("_____________________La 3ª Funcion Obtiene e imprime los siguientes campos:___________________________ ")
    print(">>Nombre del Track<<"+ "       >>Duración Track ms<<"+  "    >>Tipo Track<<"+"    >>Track URI<<")

    for item in resultsdef3["tracks"]["items"]:
        track_name=item["name"]
        track_duration_ms=item["duration_ms"]
        track_type=item["type"]
        track_uri=item["uri"]
            
              
        print("{:40} | {} | {:20} | {} ".format(track_name,track_duration_ms,track_type,track_uri))
        
obtain_Tn_DT_UE_UP()

#######################################TODO##########################################################################################
#######################################TODO##########################################################################################



artist_Id="1dfeR4HaWDbWqFHLkxsg1d"
resultsforArtist=spotipy.artist_top_tracks(artist_Id)

print('Keys for results ["tracks"][0]:')
print(resultsforArtist["tracks"][0].keys(),"\n")

print('Keys for results ["tracks"][0]["album"]:')
print(resultsforArtist["tracks"][0]["album"].keys(),"\n")


def artistEspecific():
    for track in resultsforArtist['tracks'][:10]:
        track_name=track['name']
        album_name=track['album']['name']
        
        if len(track_name) >=40:
            track_name=track_name[:37]
            track_name+="·········"
        
        print("{:40} | {:20s}".format(track_name,album_name))
    
artistEspecific()

print("\n")

def MethodResquestSpotifyApi():
  
  
  CLIENT_ID = '2b4d51ad477d4b10a22e5c1d3267338f'
  CLIENT_SECRET = '13ee1754564b440880f1a36adfc5325d'

  AUTH_URL = 'https://accounts.spotify.com/api/token'

  # POST
  auth_response = requests.post(AUTH_URL, {
      'grant_type': 'client_credentials',
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET,
  })

  # convert the response to JSON
  auth_response_data = auth_response.json()

  # save the access token
  access_token = auth_response_data['access_token']

  headers = {
      'Authorization': 'Bearer {token}'.format(token=access_token)
  }

  # base URL of all Spotify API endpoints
  BASE_URL = 'https://api.spotify.com/v1/'

  # Track ID from the URI
  track_id = '6y0igZArWVi6Iz0rj35c1Y'

  # actual GET request with proper header
  r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
  r = r.json()
  r
  {'acousticness': 0.446,
  'analysis_url': 'https://api.spotify.com/v1/audio-analysis/6y0igZArWVi6Iz0rj35c1Y',
  'danceability': 0.54,
  'duration_ms': 234910,
  'energy': 0.59,
  'id': '6y0igZArWVi6Iz0rj35c1Y',
  'instrumentalness': 0,
  'key': 0,
  'liveness': 0.14,
  'loudness': -4.359,
  'mode': 1,
  'speechiness': 0.0528,
  'tempo': 119.878,
  'time_signature': 4,
  'track_href': 'https://api.spotify.com/v1/tracks/6y0igZArWVi6Iz0rj35c1Y',
  'type': 'audio_features',
  'uri': 'spotify:track:6y0igZArWVi6Iz0rj35c1Y',
  'valence': 0.267}

  artist_id = '36QJpDe2go2KgaRleHCDTp'

  # pull all artists albums
  r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', 
                  headers=headers, 
                  params={'include_groups': 'album', 'limit': 50})
  d = r.json()
  artist_id = '36QJpDe2go2KgaRleHCDTp'

  artist_id = '36QJpDe2go2KgaRleHCDTp'

  # pull all artists albums
  r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', 
                  headers=headers, 
                  params={'include_groups': 'album', 'limit': 50})
  d = r.json()

  # pull all artists albums
  r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', 
                  headers=headers, 
                  params={'include_groups': 'album', 'limit': 50})
  d = r.json()

  for album in d['items']:
      print(album['name'], ' --- ', album['release_date'])
      
      
MethodResquestSpotifyApi()