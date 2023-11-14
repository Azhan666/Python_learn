#while循环:
i =0
while i <= 9:
    #print (i)
    p = 1
    while p<=i:
        #print(p.end=")
        print('%d * %d = %d' % (p,i,p*i), end='\t')
        p += 1
    print("")
    i += 1
