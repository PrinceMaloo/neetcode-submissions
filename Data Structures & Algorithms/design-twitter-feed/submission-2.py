from collections import defaultdict

class Twitter:
    def __init__(self):
        self.stack = []
        self.followers = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.stack.append((userId,tweetId))
        self.followers[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for i in range(len(self.stack)-1,-1,-1):
            if len(res) == 10:
                return res
            user_id, tweet_id = self.stack[i]
            if user_id in self.followers[userId]:
                res.append(tweet_id)
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].discard(followeeId)
