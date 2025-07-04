import requests

anime_or_manga_name = input('enetr anime/manga name (in lowercase) ').lower()
input_type = input('(a) for anime (m) for manga ')
if input_type == 'a':
    media_type = 'ANIME'
elif input_type == 'm':
    media_type = 'MANGA'
else:
    print('Invalid input.')
    exit()

url = "https://graphql.anilist.co"
headers = {
    "Content-Type": "application/json"
}
query = f"""
query {{
  Media(search: "{anime_or_manga_name}", type: {media_type})
  {{
    title {{romaji}}
    description
    episodes
    chapters
    status
    genres
    averageScore
    coverImage{{large}}
    recommendations {{nodes {{mediaRecommendation {{title {{romaji}}coverImage {{large}}}}
    rating}}}}
  }}
}}
"""
response = requests.post(url, headers=headers, json={"query": query})
data = response.json()
media = data["data"]["Media"]
title = media['title']['romaji']
genres = media['genres']
description = media['description']
status = media["status"]
recs = media["recommendations"]["nodes"]
averageScore = media['averageScore']
coverImage = media['coverImage']["large"]

if media_type == 'ANIME':
    count = media["episodes"]
    label = 'episodes'
elif media_type == 'MANGA':
    count = media["chapters"]
    label = "chapters"
else:
    count = None
    label = 'Unknown'
    exit()

print("====================")
print(f"Title: {title}")
print(description)
print(f"{label}: {count}")
print(f"Score: {averageScore}")
print("Genres:", ", ".join(genres))
print(f"Cover Image: {coverImage}")
print(f"Status: {status}")
print("====================")
for rec_index in range(3):
    rec = recs[rec_index]
    rec_title = rec["mediaRecommendation"]["title"]["romaji"]
    rating = rec["rating"]
    rec_image = rec["mediaRecommendation"]["coverImage"]["large"]
    print(f"similar: {rec_title} (Rating: {rating}) image: {rec_image}")
print("====================")

#updated ver :)
#any rec stands for recommendation
#i hate myself