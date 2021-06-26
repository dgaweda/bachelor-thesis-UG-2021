import unittest

from instapy import InstaPy, smart_run

from instagram.external.instagramInstance import InstagramInstance

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.session = InstaPy(username="patrykgaweda1",
                          password="YouKnowNothingJonSnow1",
                          headless_browser=False)

        self.donLikeTags = ['sad','mad','bad' , 'depression']

        self.comments = [
            u'What a  shot! :heart_eyes: What do '
            u'you think of my  shot?',
            u'What an amazing shot! :heart_eyes: LOL nice',
            u'What an amazing shot! :heart_eyes: What do '
            u'you think of my recent shot?'
            u'What an amazing shot! :heart_eyes: I think ']

        self.my_hashtags = ['patryk', 'amator_kwasnych_jablek', 'pasion']

        self.my_locations = ['sopot', 'gdynia', 'Zalesie']

        self.ignore_list = ['zalesie', 'cyclist', 'raw']

        self.instagram =  InstagramFunctions(username,password)
    def testBaseInstapyCommentWithDecentRatio(self):
            with smart_run(self.session):
                self.session.set_dont_like(self.donLikeTags)
                self.session.set_do_follow(enabled=True, percentage=40, times=1)
                self.session.set_do_comment(enabled=True, percentage=20)
                self.session.set_comments(self.comments)

    def testBaseInstapyCommentWithFullRation(self):
        with smart_run(self.session):
            self.session.set_dont_like(self.donLikeTags)
            self.session.set_do_follow(enabled=True, percentage=100, times=1)
            self.session.set_do_comment(enabled=True, percentage=100)
            self.session.set_comments(self.comments)

        
    def testOurCodeCommentWithFullRation(self):
        with smart_run(self.session):
            self.session.set_dont_like(self.donLikeTags)
            self.session.set_do_follow(enabled=True, percentage=100, times=1)
            self.session.set_do_comment(enabled=True, percentage=100)
            instagram.startMachine(self.my_locations, self.my_hashtags, 100,
                                   100, self.my_hashtags,
                                   1, 10, self.comments)


    def testHybidlikePhotosByTags(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            instagram.startMachine(self.my_locations, self.my_hashtags, 10,
                                   10, self.my_hashtags,
                                   1, 10, self.comments)
    def testHybidlikeVideosByTags(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            instagram.startMachine(self.my_locations, self.my_hashtags, 0,
                                   100, self.my_hashtags,
                                   1, 10, self.comments)
    def testHybidfollowByTags(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            instagram.startMachine(self.my_locations, self.my_hashtags, 100,
                                   100, self.my_hashtags,
                                   1, 10, self.comments)
    def testHybidfollowByLocation(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            instagram.startMachine(self.my_locations, self.my_hashtags, 50,
                                   50, self.my_hashtags,
                                   1, 10, self.comments)

    def testHybidunfollowNewFollowers(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            instagram.startMachine(self.my_locations, self.my_hashtags, 0,
                                   0, self.my_hashtags,
                                   10, 10, self.comments)

    def testHybidunfollowNonFollowers(self):
        with smart_run(self.session):
            self.session.set_ignore_if_contains(self.ignore_list)
            self.session.set_user_interact(amount=2, randomize=True, percentage=60)
            self.session.set_do_follow(enabled=True, percentage=40)
            self.session.set_do_like(enabled=True, percentage=80)
            instagram.startMachine(self.my_locations, self.my_hashtags, 100,
                                   100, self.my_hashtags,
                                   1, 1, self.comments)


    def testOurCodelikePhotosByTags(self):
        with smart_run(self.session):
            instagram.startMachine(self.my_locations, self.my_hashtags, 100,
                                   100, self.my_hashtags,
                                   1, 10, self.comments)

    def testOurCodelikeVideosByTags(self):
        with smart_run(self.session):
            instagram.startMachine(self.my_locations, self.my_hashtags, 0,
                                   100, self.my_hashtags,
                                   1, 10, self.comments)

    def testOurCodefollowByTags(self):
        with smart_run(self.session):
            instagram.startMachine(self.my_locations, self.my_hashtags, 100,
                                   0, self.my_hashtags,
                                   1, 10, self.comments)

    def testOurCodefollowByLocation(self):
        with smart_run(self.session):
            instagram.startMachine(["Gdansk","Berlin","Warsaw"], self.my_hashtags, 100,
                                   100, self.my_hashtags,
                                   1, 10, self.comments)

    def testOurCodeunfollowNewFollowers(self):
        with smart_run(self.session):
            instagram.startMachine(self.my_locations, self.my_hashtags, 100,
                                   100, self.my_hashtags,
                                   1, 1, self.comments)

    def testOurCodeunfollowNonFollowers(self):
        with smart_run(self.session):
            instagram.startMachine(self.my_locations, self.my_hashtags, 100,
                                   100, self.my_hashtags,
                                   1, 0, self.comments)

if __name__ == '__main__':
    unittest.main()