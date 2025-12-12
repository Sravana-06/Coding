class Solution:
    def countMentions(self, numberOfUsers, events):
        mentions = [0] * numberOfUsers
        online = [True] * numberOfUsers
        online_until = [0] * numberOfUsers
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        for e in events:
            t = int(e[1])
            for u in range(numberOfUsers):
                if not online[u] and t >= online_until[u]:
                    online[u] = True
            if e[0] == "OFFLINE":
                user = int(e[2])
                online[user] = False
                online_until[user] = t + 60
            else:
                msg = e[2].split()
                if msg == ["ALL"]:
                    for u in range(numberOfUsers):
                        mentions[u] += 1
                elif msg == ["HERE"]:
                    for u in range(numberOfUsers):
                        if online[u]:
                            mentions[u] += 1
                else:
                    for token in msg:
                        if token.startswith("id"):
                            mentions[int(token[2:])] += 1
        return mentions
