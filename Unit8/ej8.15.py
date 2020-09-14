import random
freq=[0]*11
N=int(input("How many experiments? "))
for i in range(N):
    s=random.randint(1,6)+random.randint(1,6)
    freq[s-2]+=1
freq=[el/N for el in freq]
theo=[1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]
err=[100*abs(f-t)/t for f,t in zip(freq,theo)]


print("For 2 dice, the probability of getting n eyes is:")
print("n   exp. prob.  theo. prob.    %error")
for i in range(11):
    print("%-2i %8.4f    %8.4f        %-8.3f "%(i+2,freq[i],theo[i],err[i]))
