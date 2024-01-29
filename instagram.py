import instaloader

bot = instaloader.Instaloader()

profile = instaloader.Profile.from_username(bot.context, "deven__8081")

print(type(profile))
# Login with username and password in the script
bot.login(user="Write your username", passwd="write your password")
# Interactive login on terminal
bot.interactive_login("add up your username")  # Asks for password in the terminal
# Retrieve the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Retrieve the usernames of all followees
followees = [followee.username for followee in profile.get_followees()]
print(followers)

profile = instaloader.Profile.from_username(bot.context, "ielts")

# Get all posts in a generator object
posts = profile.get_posts()

# Iterate and download
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")
