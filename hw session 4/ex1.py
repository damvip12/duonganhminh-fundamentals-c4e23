flock = [5 , 7 , 300 , 90 , 24 , 50 , 75]
print("Hello , my name is Hiep and these are my sheep sizes :" )
print(*flock , sep =", ")

print("Now my biggest sheep has size :", max(flock) , "lets shear it")
s = 8
i = flock.index(max(flock))
flock[i] = s
print("After shearing , here is my flock :" )
print(*flock , sep =", ")

print("MONTH 1:")
increased_flock = [x+50 for x in flock]
print("One month has passed , here is my flock :")
print(*increased_flock, sep =", ")

print("Now my biggest sheep has size :", max(increased_flock) , "lets shear it")
i = increased_flock.index(max(increased_flock))
increased_flock[i] = s
print("After shearing , here is my flock :" )
print(*increased_flock , sep =", ")

summary = sum(increased_flock)
print("My flock has size in total: ", summary)
print("I would get ",summary ," *2$ = ", summary*2 ,"$")
