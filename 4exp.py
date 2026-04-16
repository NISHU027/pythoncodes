print("Simple Interest Calculator")

print("Enter principal amount:")
p = float(input().split()[-1])

print("Enter rate of interest:")
r = float(input().split()[-1])

print("Enter time period (in years):")
t = float(input().split()[-1])

si = (p * r * t) / 100

def fmt(x):
    if x.is_integer():
        return f"{x:.1f}"
    else:
        return f"{x:g}"

print(f"Simple Interest: {fmt(si)}")