import inputfile as input
increment = 1
starter = 0
total_safe = 0
tol_count = 0
for record in input.sampleinput:
    saftey = 1
    track = []    
    for step in record:
        try:
            dif  = step-record[increment]
        except:
            pass
        increment= increment+1
        track.append(dif)
        if 1 <= dif <= 3 or -1 >= dif >=-3:
            saftey = saftey*1   
        else:
            tol_count = tol_count+1
    if all(val< 0 for val in track) or all(val> 0 for val in track):
        if tol_count <=1:
            saftey = saftey*1
        else:
            saftey = saftey*0
    else:
        tol_count = tol_count+1
        if tol_count <=1:
            pass
        else:
            saftey = saftey*0
    print(f"{track} saftey = {saftey} tol_count = {tol_count}")
    total_safe = total_safe+saftey
    increment =1
    tol_count = 0
    track = []
print(total_safe)
    
  