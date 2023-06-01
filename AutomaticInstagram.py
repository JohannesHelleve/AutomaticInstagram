import instaloader
import config

# Get the most liked photo in Oslo in the last day
client = instaloader.Instaloader()
client.login(config.username, config.password )

post = instaloader.Post

query = '#Oslo'

results = instaloader.TopSearchResults(query, 'Oslo')

client.download_post(results)

