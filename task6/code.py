def check_time_overlap(start1, end1, start2, end2):
    return max(start1, start2) < min(end1, end2)

def validate_timetable(schedule):
    conflicts = []
    total_courses = len(schedule)
    
    for i in range(total_courses):
        for j in range(i + 1, total_courses):
            course1, day1, start1, end1, room1 = schedule[i]
            course2, day2, start2, end2, room2 = schedule[j]
            
            if day1 == day2:
                if check_time_overlap(start1, end1, start2, end2):
                    if room1 == room2:
                        conflicts.append(f"Room Conflict: '{room1}' is double-booked by {course1} and {course2} on {day1}.")
                    conflicts.append(f"Time Overlap: {course1} and {course2} overlap on {day1}.")
                    
    return conflicts

sample_schedule = [
    ("Mathematics", "Monday", 9, 11, "Room 101"),
    ("Physics", "Monday", 10, 12, "Room 102"),
    ("Chemistry", "Monday", 10, 12, "Room 101"),
    ("English", "Tuesday", 13, 15, "Room 103")
]

validation_results = validate_timetable(sample_schedule)
for conflict in validation_results:
    print(conflict)
