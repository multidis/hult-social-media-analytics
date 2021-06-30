## Check Twitter API credentials in config-file.
import tweepy as tw
import config_twitter

auth = tw.OAuthHandler(config_twitter.consumer_key, config_twitter.consumer_secret)
auth.set_access_token(config_twitter.access_token, config_twitter.access_token_secret)

api = tw.API(auth, wait_on_rate_limit=True)

# returns False if credentials could not be verified
# https://docs.tweepy.org/en/stable/api.html#API.verify_credentials
user = api.verify_credentials()
if not user:
    print("Credentials could not be verified: Please check config.py")
else:
    print("Credentials verified successfully")
