#Calculate the exact Time after the meeting 
hour = int(input("Starting time of the Meeting (hours): "))
mins = int(input("Starting time of the Meeting (minutes): "))
dura = int(input("Event duration (minutes): "))
# Calculate hours excluding minutes.
hourA = (hour + ((mins + dura)//60)) % 24
# Calculated minutes 
minB = (mins + dura)%60
#hourB = hourA % 24
print(hourA,":",minB)
