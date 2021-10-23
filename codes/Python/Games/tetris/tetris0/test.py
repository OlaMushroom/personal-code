import dis

def fac(n):return 1 if n<2 else n*fac(n-1)

print(fac(24))
print(dis.dis(fac))