import pandas as pd

k1 = pd.read_csv("complete.csv")
k2 = pd.read_csv("^BSESN.csv")
k3 = pd.DataFrame(k2)
k3["cases"] = 0


def get_match(k1,k3):
    for i in range(k3.shape[0]):
        for q in range(k1.shape[0]):
            if k1["Date"][q] == k3["Date"][i]:
                return(i)
            

c2 = get_match(k1,k3)

prev = k1["Date"][0]
count = 0
for j in range(1,k1.shape[0]):
    if  prev  ==  k1["Date"][j] :
        count = count +1
    else:
        prev = k1["Date"][j]
        c2 = c2 + 1
        k3["cases"][c2] = count
        #print(count)

#k3.to_csv("output1.csv")
print(k3)

print(k3.corr(method = 'kendall'))