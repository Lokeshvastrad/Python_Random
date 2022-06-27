# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account
# activity. If the amount spent by a client on a particular day is greater than or equal to  the 
# client's median spending for a trailing number of days, they send the client a notification about 
# potential fraud. The bank doesn't send the client any notifications until they have at least that 
# trailing number of prior days' transaction data.

# Given the number of trailing days  and a client's total daily expenditures for a period of  days, 
# determine the number of times the client will receive a notification over all  days.

def bankFraud(ar,d):
    count=0
    for i in range(len(ar)):
        if d+i >= len(ar):
            break
        tmp_ar = sorted(ar[i:d+i])
        if d % 2 == 0:
            median = (tmp_ar[d//2]+tmp_ar[(d//2)-1])//2
        else:
            median = tmp_ar[d//2]

        if (ar[i+d] >= (2 * median)):
            count+=1
    return count

ar=[30,40,90,1000,2000,60000]
d=2
res=bankFraud(ar,d)
print(res)