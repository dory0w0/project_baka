import requests
anime_or_manga_name =input('enetr anime/manga name (in lowercase) ').lower()
input_type = input('(a) for anime (m) for manga ')
if input_type=='a':
    media_type='ANIME'
elif input_type=='m':
    media_type='MANGA'
else:
    print('Invalid input.')
    exit()
url = "https://graphql.anilist.co"
headers = {
    "Content-Type": "application/json"
}
query = f"""
query {{
  Media(search: "{anime_or_manga_name}", type: {media_type}) {{
    title {{
      romaji
    }}
    episodes
    chapters
    status
    genres
    averageScore
    coverImage {{
      large
    }}
        recommendations {{
      nodes {{
        mediaRecommendation {{
          title {{
            romaji
          }}
          coverImage {{
            large
          }}
        }}
        rating
      }}
    }}
  }}
}}
"""
response = requests.post(url, headers=headers, json={"query": query})
data = response.json()
media = data["data"]["Media"]
title = media['title']['romaji']
genres = media['genres']
status = media["status"]
recs = media["recommendations"]["nodes"]
averageScore = media['averageScore']
coverImage = media['coverImage']["large"]
if media_type=='ANIME':
    count = media["episodes"]
    label = 'episodes'
elif media_type == 'MANGA':
    count = media["chapters"]
    label = "chapters"
else:
    count = None
    label = 'Unknown'
    exit()
for rec in recs:
    rec_title = rec["mediaRecommendation"]["title"]["romaji"]
    rating = rec["rating"]
print("====================")
print(f"Title: {title}")
print(f"{label}: {count}")
print(f"Score: {averageScore}")
print("Genres:", ", ".join(genres))
print(f"Cover Image:{coverImage}")
print(f"Status: {status}")
print("====================")
print(f"similar: {rec_title} (Rating: {rating})")
print("====================")
