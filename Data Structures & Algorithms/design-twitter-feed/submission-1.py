class Twitter:

    def __init__(self):
        self.tweets = deque([])
        self.usersFollow = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft((userId, tweetId))       

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        length = 10
        # print(self.tweets)
        for tweet in self.tweets:
            if tweet[0] in self.usersFollow[userId] or tweet[0] == userId:
                ans.append(tweet[1])
                length -= 1
            if length == 0:
                return ans
        # print(ans, 'ajit')
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.usersFollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usersFollow[followerId].discard(followeeId)
        
