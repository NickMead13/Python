
val = input("input data:\n")
total, interest, months = (val.split())
total = int(total)
interest = int(interest) / 12 / 100
months = int(months)

payment = (total * interest * ((1 + interest) ** months)) / \
    (((1 + interest) ** months) - 1)
print("\nanswer:")
print(payment)
