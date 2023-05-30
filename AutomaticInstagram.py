import instaloader
import config

# Get the most liked photo in Oslo in the last day
client = instaloader.Instaloader()
client.login(config.username, config.password )

post = instaloader.Post

for post in instaloader.Hashtag.from_name(client.context, 'Oslo').get_posts():
    # post is an instance of instaloader.Post
    client.download_post(post, target='#Oslo')