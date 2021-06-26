from instapy import InstaPy
from instapy import smart_run

insta_username = 'patrykgaweda1'
insta_password = 'YouKnowNothingJonSnow1'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=6000,
                                    max_following=3000,
                                    min_followers=30,
                                    min_following=30)
    session.set_user_interact(amount=2, randomize=True, percentage=30,
                              media='Photo')
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_comment(enabled=True, percentage=25)
    session.set_comments(
        ['Looks great @{}',
         'Getting inspired by you yoo @{}',
         'Nice shot! @{}', 'I love your profile! @{}', '@{} Love it!',
         '@{} :heart::heart:',
         'go girl :fire: :alien:',
         'you are a :gun:',
         'Love your posts @{}',
         ':raised_hands: Yes!',
         '@{}:revolving_hearts::revolving_hearts:', '@{}:fire::fire::fire:'],
        media='Photo')

    session.follow_user_followers(['chrisburkard', 'danielkordan'],
                                  amount=2, randomize=False, interact=True, sleep_delay=200)

    session.join_pods(topic='entertainment', engagement_mode='no_comments')
