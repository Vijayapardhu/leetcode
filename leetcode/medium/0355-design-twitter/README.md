# Design Twitter

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the `10` most recent tweets in the user's news feed.

Implement the `Twitter` class:

- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

 

 **Example 1:** 

```
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

```

 

 **Constraints:** 

- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 104
- All the tweets have unique IDs.
- At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
- A user cannot follow himself.

## Solution

**Language:** Python  
**Runtime:** 30 ms (beats 15.85%)  
**Memory:** 28.6 MB (beats 61.27%)  
**Submitted:** 2026-10-18T14:27:40.320Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/design-twitter/)