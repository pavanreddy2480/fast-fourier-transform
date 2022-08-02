from cmath import e, pi


def fft(p):
    n=len(p)
    if n==1:
        return p
    w=e^((2*pi*complex(0,1))/n)
    pe=p[: :2]  
    po=p[1::2]
    ye=fft(pe)
    yo=fft(po)
    y=[0]*n
    for i in range(n/2):
        y[i]=ye[i]+(w^i)*yo[i]
        y[i+(n/2)]=ye[i]-(w^i)*yo[i]
    return y   




def ifft(p):
    n=len(p)
    if n==1:
        return p
    w=(1/n)*e^(-(2*pi*complex(0,1))/n)
    pe=p[: :2]  
    po=p[1::2]
    ye=ifft(pe)
    yo=ifft(po)
    y=[0]*n
    for i in range(n/2):
        y[i]=ye[i]+(w^i)*yo[i]
        y[i+(n/2)]=ye[i]-(w^i)*yo[i]
    return y  