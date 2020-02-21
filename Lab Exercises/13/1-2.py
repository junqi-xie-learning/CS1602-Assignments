inf = open("2_log.txt", "r")
outf = open("2_net_amount.txt", "w")

net_amount = 0
while True:
    s = inf.readline()
    if s == "":
        break

    token, amount = s.split()
    amount = int(amount)
    if token == 'D':
        net_amount += amount
    elif token == 'W':
        net_amount -= amount
outf.write(str(net_amount))

inf.close()
outf.close()