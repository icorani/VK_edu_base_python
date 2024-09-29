from typing import List, Dict
import heapq


class Twitter:

    def __init__(self):
        self.friends_of_user = {}
        self.cur = 0
        self.timeline = []

    def post_tweet(self, user_id: int, tweet_id: int):
        heapq.heappush(self.timeline, [-self.cur, tweet_id, user_id])
        self.cur += 1

    def get_news_feed(self, user_id) -> List[int]:
        result = list()
        n = 0
        user_timeline = self.timeline[:]
        while user_timeline and n < 10:
            top_tweet = heapq.heappop(user_timeline)
            if (
                top_tweet[2] == user_id
                or user_id in self.friends_of_user
                and top_tweet[2] in self.friends_of_user[user_id]
            ):
                result.append(top_tweet[1])
                n += 1
        return result

    def follow(self, follower_id: int, followee_id: int):
        if follower_id not in self.friends_of_user:
            self.friends_of_user[follower_id] = set()
        self.friends_of_user[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int):
        if (
            follower_id in self.friends_of_user
            and followee_id in self.friends_of_user[follower_id]
        ):
            self.friends_of_user[follower_id].remove(followee_id)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
