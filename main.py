class operation():
    def __init__(self,j=0,k=0,l=0,m=0,n=0):
        self.a=j
        self.b=k
        self.c=l
        self.d=m
        self.e=n
        self.li=[self.a,self.b,self.c,self.d,self.e]
        print('inialize the values ')
    def add(self):
        print('Addition= ',self.a+self.b+self.c+self.d+self.e )
    def sub(self):
        print('Substraction= ',self.a-self.b-self.c-self.d-self.e)
    def mul(self):
        print('Multiplication= ',self.a*self.b*self.c*self.d*self.e)
    def div(self):
        print('Divide= ',self.a/self.b/self.c/self.d/self.e)
    def modulus(self):
        print('Modulus= ',self.a%self.b%self.c%self.d%self.e)
    def mean(self):
        print('Mean= ',(self.a+self.b+self.c+self.d+self.e)/len(self.li))
    def median(self):
        self.li.sort()
        print('Median= ',self.li[2])
    def min(self):
        print('Minimum',min(self.li))
    def max(self):
        print('Maximum',max(self.li))
    def mode(self):
        d=dict()
        for i in self.li:
            d.setdefault(i,0)
            d[i]+=1
        jk=max(d.values())
        di={h:g for g,h in d.items()}
        print('Mode',di[jk])
    def per75(self):
        print('75%A= ', (75*self.a)/100)
        print('75%B= ', (75*self.b)/100)
        print('75%C= ', (75*self.c)/100)
        print('75%D= ', (75*self.d)/100)
        print('75%E= ', (75*self.e)/100)
    def total75per(self):
        print('Total 75 percent',75*(self.a+self.b+self.c+self.d+self.e)/100)
    def per25(self):
        print('25%A= ', (25*self.a)/100)
        print('25%B= ', (25*self.b)/100)
        print('25%C= ', (25*self.c)/100)
        print('25%D= ', (25*self.d)/100)
        print('25%E= ', (25*self.e)/100)
    def total25per(self):
        print('Total 25 percent',25*(self.a+self.b+self.c+self.d+self.e)/100)
    def per50(self):
        print('50%A= ', (50*self.a)/100)
        print('50%B= ', (50*self.b)/100)
        print('50%C= ', (50*self.c)/100)
        print('50%D= ', (50*self.d)/100)
        print('50%E= ', (50*self.e)/100)
    def total50per(self):
        print('Total 50 percent',50*(self.a+self.b+self.c+self.d+self.e)/100)
z=operation(10,12,21,53,54)
z.add()
t=operation(100,23,3,4,5)
t.sub()
u=operation(2,3,4,5,8)
u.mul()
r=operation(123450,2,4,3,6)
r.div()
po=operation(1234445,2,2,2,2)
po.modulus()
Q=operation(12,24,5,65,6)
Q.mean()
Me=operation(34,32,5,53,43)
Me.median()
ta=operation(12,433,5,3,3)
ta.min()
ta.max()
zx=operation(11,23,4,4,4)
zx.mode()
zx.per75()
zx.per25()
zx.per50()
zx.total75per()
zx.total25per()
zx.total50per()