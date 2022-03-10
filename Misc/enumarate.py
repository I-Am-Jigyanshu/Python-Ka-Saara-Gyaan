l1 = ["Bhindi","Aloo","Chopsticks","Chowmein"]
i = 1
# for item in l1:
#     if i%2 != 0:
#         print(f"Please buy {item}")
#     i+=1


for index,item in enumerate(l1):
    if index%2==0: # even 0 se start
        print(f"Please buy {item}")


