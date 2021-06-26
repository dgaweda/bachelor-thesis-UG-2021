from instagram.domain.instagramFunctions import InstagramFunctions


class InstagramInstance:
    def configureSession(session, maxFollowers, minFollowers, maxFollowing, minFollowing):
        session.set_relationship_bounds(enabled=True,
                                        max_followers=maxFollowers,
                                        min_followers=minFollowers,
                                        max_following=maxFollowing,
                                        min_following=minFollowing)

    # Follow activity
    def followByLocation(session, location):
        InstagramFunctions.followByLocation(session, location)

    def followByTags(session, tagList):
        InstagramFunctions.followByTags(session, tagList)

    # Like activity
    def likePhotosByTags(session, tagList, probability):
        InstagramFunctions.likePhotosByTags(session, tagList, probability)

    def likeVideosByTags(session, tagList, probability):
        InstagramFunctions.likeVideosByTags(session, tagList, probability)

    def unfollowNonFollowers(session, amount, unfollowDelay):
        InstagramFunctions.unfollowNonFollowers(session, amount,
                                                unfollowDelay)

    def unfollowNewFollowers(session, amount, unfollowDelay):
        InstagramFunctions.unfollowNewFollowers(session, amount,
                                                unfollowDelay)

    def setPods(session, topic, mode):
        InstagramFunctions.setPods(session, topic, mode)
