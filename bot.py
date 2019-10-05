import os
from decouple import config
import twitter

# Initialize client
api_client = twitter.Api(
	consumer_key=config('CONSUMER_KEY'),
	consumer_secret=config('CONSUMER_SECRET'),
	access_token_key=config('ACCESS_TOKEN_KEY'),
	access_token_secret=config('ACCESS_TOKEN_SECRET')
)

# Checking credentials out
#print(api_client.VerifyCredentials())

# posting a twit
""" result = api_client.GetFollowers()
first_ten = result[:10]
 """
""" print(result[0]
for f in result_ten:
    print(f)
 """

# publica un twiter(texto)
#result = api_client.PostUpdate("I am trolling Glileos's account. Xoco was here.")   
#print(result)


#publica twitter con imagen
image_path = os.path.abspath('image.jpg')
result = api_client.PostUpdate(
    "I am trolling Glileos's account. Xoco was here again.", 
    media=image_path
    )   