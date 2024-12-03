import inputfile as input
increment = 1
starter = 0
total_safe = 0
for record in input.inputfile:
    # print(record)
    saftey = 1
    track = []
    for step in record:
        try:
            # print(f"step {step}")
            # print(f"recordincrement-1 =  {record[increment]}")
            dif  = step-record[increment]
        except:
            pass
        increment= increment+1
        # print(dif)
        track.append(dif)
        
        if 1 <= dif <= 3 or -1 >= dif >=-3:
            saftey = saftey*1   
        elif dif == 0:
            saftey= saftey*0
        else:
            saftey= saftey*0
    if all(val< 0 for val in track) or all(val> 0 for val in track):
        pass
        # print("true")
    else:
        saftey = saftey*0
    #     print("false")
    # print(f"{record} {saftey}")
    # print(track)
    total_safe = total_safe+saftey
    increment =1
    track = []
print(total_safe)
    
        
