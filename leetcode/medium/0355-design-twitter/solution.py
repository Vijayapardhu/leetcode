from collections import defaultdict, deque
import heapq

class Twitter:

    def __init__(self):
        # Maps userId to a set of followed userIds
        self.following = defaultdict(set)
        # Maps userId to a list of (timestamp, tweetId) tuples
        self.tweets = defaultdict(list)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Use a global timer to maintain insertion order for heap sorting
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # Include own tweets in feed
        users = self.following[userId] | {userId}
        # Max-heap to retrieve the 10 most recent tweets efficiently
        min_heap = []
        
        for user in users:
            for timestamp, tweetId in self.tweets[user][-10:]:
                heapq.heappush(min_heap, (-timestamp, tweetId))
        
        res = []
        while min_heap and len(res) < 10:
            res.append(heapq.heappop(min_heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)