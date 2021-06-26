import logging
from enum import Enum

from instapy import InstaPy, smart_run


class InstagramFunctions:
    def __init__(self, username, password):
        self.session = InstaPy(username=username,
                               password=password,
                               headless_browser=False)

    def startMachine(self, location, tagList, likeProbability, videPropability, followingNames, unfolowAmount=100,
                     unfollowDelay=100, comments=["nice picture", "you look amazing"], mode='normal',
                     topic="entertainment"):
        with smart_run(self.session):

            logging.debug(location, tagList, likeProbability, videPropability, followingNames, unfolowAmount,
                          unfollowDelay, comments)
            if (comments != ''):
                logging.debug("comments")
                logging.debug(comments)
                self.session.set_do_comment(enabled=True, percentage=80)
                self.session.set_comments(comments)
                self.session.set_delimit_commenting(enabled=True, max_comments=200, min_comments=0)

            if (location == ''):
                self.session.follow_by_locations(location, amount=2)
            if (tagList != ''):
                self.session.follow_user_followers(followingNames, amount=2)

            if (tagList != '' and likeProbability != ''):
                logging.debug("likeByTags")
                logging.debug(likeProbability)
                logging.debug(tagList)
                self.session.set_user_interact(randomize=True, percentage=likeProbability)
                self.session.like_by_tags(tagList, amount=2)

            if (unfolowAmount != '' and unfollowDelay != ''):
                logging.debug("unfollowDelay")
                logging.debug(unfolowAmount)
                logging.debug(unfollowDelay)
                self.session.unfollow_users(amount=unfolowAmount,
                                            allFollowing=True,
                                            style="FIFO",
                                            unfollow_after=unfollowDelay,
                                            sleep_delay=60)
                self.session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                                       style="FIFO",
                                       unfollow_after=12 * 60 * 60, sleep_delay=601)


# engagement_mode: Desided engagement mode for your posts.
# There are four levels of engagement modes 'no_comments', 'light', 'normal' and 'heavy'(normal by default).
# Setting engagement_mode to 'no_comments' makes you receive zero comments on your posts from pod members,
# 'light' encourages approximately 10% of pod members to comment on your post,
# similarly it's around 30% and 90% for 'normal'
# 'heavy' modes respectively.
# Note: Liking, following or any other kind of engagements doesn't follow these modes.

class podstMode(Enum):
    noComment = 'no_comment'
    heavy = 'heavy'
    light = 'light'
    normal = 'normal'

# engagement_mode: Desided engagement mode for your posts.
# There are four levels of engagement modes 'no_comments', 'light', 'normal' and 'heavy'(normal by default).
# Setting engagement_mode to 'no_comments' makes you receive zero comments on your posts from pod members,
# 'light' encourages approximately 10% of pod members to comment on your post,
# similarly it's around 30% and 90% for 'normal'
# 'heavy' modes respectively.
# Note: Liking, following or any other kind of engagements doesn't follow these modes.

class podstMode(Enum):
    noComment = 'no_comment'
    heavy = 'heavy'
    light = 'light'
    normal = 'normal'