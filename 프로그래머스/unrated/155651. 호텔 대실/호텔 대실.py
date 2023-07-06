def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x:x[0])
    rooms = []
    rooms.append([int(val) for val in book_time[0][1].split(":")])
    
    for i in range(1,len(book_time)):
        tmp = [int(val) for val in book_time[i][0].split(':') ]
        start_h = tmp[0]
        start_m = tmp[1]
        rooms.sort(key=lambda x:(x[0],x[1]))
        for j in range(len(rooms)):
            room_h = rooms[j][0]
            room_m = rooms[j][1] + 10
            if room_m >= 60:
                room_m = room_m - 60
                room_h += 1
            if (room_h < start_h) or (room_h == start_h and room_m <= start_m):
                rooms[j] = [int(val) for val in book_time[i][1].split(':') ]
                break
        else:
            rooms.append([int(val) for val in book_time[i][1].split(':') ])    
            
                
    return len(rooms)