import instaloader
import config

# Get the most liked photo in Oslo in the last day
client = instaloader.Instaloader()
client.login(config.username, config.password )

# Set the rate controller to sleep for 1 second between requests
client.set_rate_controller(instaloader.RateController(sleep_time=1))

# Get the most liked photo in Oslo in the last day
photos = client.get_geotagged_media("59.912898,10.752222", max_likes=1)

# Download the photo
photo = photos[0]
client.download_photo(photo, "most_liked_photo_in_oslo.jpg")