def distance (v0, t, a):
    return v0*t+(1/2)*a*t**2
v0 = 0
t = int(input("how much time is spent on the road? (m/s):"))
a = int(input("what's the acceleration of your car? (m/s^2):"))
d = int(input("how much is the distance you want? (m):"))
limit = 80
dur = 0
dist = 0
count = 0
sym = "*"
while dur <= t:
    dist = distance(v0, dur, a)
    count = dist / 10
    print("Duration: "+ str(dur) + " Distance:" + int(count)*sym)
    dur += 1

max = v0 + a * t

if max >= limit:
    print("The person went over the speed limit. (Max speed was " + str(max) + "m/s)")
else:
    print("The person did not go over the speed limit. (Max speed was " + str(max) + "m/s)")
if d>= dist:
    print("The person reached the destination. (Reached " + str(dist) + " m)")
else:
    print("The person did not reach the destination. (Reached " + str(dist) + "m)")
