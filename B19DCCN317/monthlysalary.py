t = int(input())
if(t>10 or t<0): print("INVALID INPUT")
else:
    while t>0:
        tntt, lcb = map(int, input().split())
        if(lcb<1000):
            print("INVALID INPUT")
        else:
            tncn =0
            tnct=tntt - 0.08*lcb -0.015*lcb - 0.01*lcb -11000000
            if tnct <= 5000000:
                tncn = 0.05*tnct
            elif tnct > 5000000 and tnct <= 10000000:
                tncn = 0.1*tnct - 250000
            elif tnct > 10000000 and tnct <= 18000000:
                tncn = 0.15*tnct - 750000
            elif tnct > 18000000 and tnct <= 32000000:
                tncn = 0.2*tnct - 1650000
            elif tnct > 32000000 and tnct <= 52000000:
                tncn = 0.25*tnct - 3250000
            elif tnct > 52000000 and tnct <= 80000000:
                tncn = 0.3*tnct - 5850000
            else:
                tncn = 0.35*tnct - 9850000
            thucLinh = tntt - 0.08*lcb -0.015*lcb - 0.01*lcb -0.01*lcb - tncn
            print(round(thucLinh))
        t-=1
