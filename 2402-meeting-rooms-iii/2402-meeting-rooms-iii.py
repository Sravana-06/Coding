import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()
        
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        busy_rooms = [] 
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                finish, room = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (finish + duration, room))
            
            count[room] += 1
        
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
