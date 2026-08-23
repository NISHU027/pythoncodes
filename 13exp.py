basic = float(input())

da = basic * 0.70
ta = basic * 0.30
hra = basic * 0.10
gross = basic + da + ta + hra
def fmt(x):
    if x.is_integer():
        return f"{x:.1f}"
    else:
        return f"{x:g}"

#print("Salary Details:")
print(f"Basic Salary:    {fmt(basic)}")
print(f"DA (70%):        {fmt(da)}")
print(f"TA (30%):        {fmt(ta)}")
print(f"HRA (10%):       {fmt(hra)}")
print(f"Gross Salary:    {fmt(gross)}")
input()
