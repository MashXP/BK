import math

# Dimensions
D1_IN = 0.014  
D1_OUT = 0.016 
L_C = 1.000    

def test():
    # Hot: 4, Cold: 4 for Tube C
    t1in, t1out, t2in, t2out = 61, 50, 32, 36
    t1avg = (t1in + t1out) / 2
    t2avg = (t2in + t2out) / 2
    print(f"T1avg: {t1avg}, T2avg: {t2avg}")
    
    # Simple LMTD
    dt_max = t1in - t2out # 61 - 36 = 25
    dt_min = t1out - t2in # 50 - 32 = 18
    lmtd = (dt_max - dt_min) / math.log(dt_max / dt_min)
    print(f"LMTD: {lmtd:.4f}")
    
    # Sample Q
    rho = 995.0
    cp = 4178.0
    g1 = (4 * 0.001 / 60) * rho
    q1 = g1 * cp * (t1in - t1out)
    print(f"Q1: {q1:.2f}")
    print("Test Done")

if __name__ == "__main__":
    test()
