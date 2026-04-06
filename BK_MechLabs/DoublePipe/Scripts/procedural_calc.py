import math
import sys

class WaterProperties:
    temp_points = [10, 20, 30, 40, 50, 60, 70, 80]
    rho = [999.7, 998.2, 995.7, 992.2, 988.1, 983.2, 977.8, 971.8]
    cp = [4192, 4182, 4178, 4179, 4181, 4185, 4190, 4196]
    lam = [0.585, 0.598, 0.615, 0.631, 0.644, 0.654, 0.663, 0.670]
    mu = [0.001307, 0.001002, 0.000798, 0.000653, 0.000547, 0.000467, 0.000404, 0.000355]
    pr = [9.45, 7.01, 5.42, 4.32, 3.55, 2.98, 2.55, 2.21]

    @staticmethod
    def get(prop_list, t):
        if t <= 10: return prop_list[0]
        if t >= 80: return prop_list[-1]
        for i in range(len(WaterProperties.temp_points)-1):
            if WaterProperties.temp_points[i] <= t <= WaterProperties.temp_points[i+1]:
                t_low = WaterProperties.temp_points[i]
                t_high = WaterProperties.temp_points[i+1]
                ratio = (t - t_low) / (t_high - t_low)
                return prop_list[i] + ratio * (prop_list[i+1] - prop_list[i])
        return prop_list[0]

# Dimensions
D1_IN = 0.014; D1_OUT = 0.016; D2_IN = 0.026; L_B = 0.925; L_C = 1.000; LAMBDA_W = 385
A1 = math.pi * (D1_IN ** 2) / 4
A2 = math.pi * (D2_IN ** 2 - D1_OUT ** 2) / 4

raw_tube_b = {(4,4):[54,49,34,40],(6,4):[59,54,36,42],(8,4):[64,58,39,45],(10,4):[69,63,40,47],(12,4):[71,66,41,48],(4,6):[56,49,35,40],(6,6):[60,54,36,42],(8,6):[65,58,38,44],(10,6):[70,63,40,46],(12,6):[71,66,41,47],(4,8):[56,50,34,40],(6,8):[60,54,36,42],(8,8):[66,58,37,43],(10,8):[70,63,39,44],(12,8):[71,65,40,46],(4,10):[57,50,34,40],(6,10):[62,54,36,41],(8,10):[67,58,37,42],(10,10):[70,63,39,44],(12,10):[72,65,40,45],(4,12):[58,51,34,40],(6,12):[63,55,36,41],(8,12):[68,59,37,42],(10,12):[71,63,39,44],(12,12):[72,66,40,45]}
raw_tube_c = {(4,4):[61,50,32,36],(6,4):[67,56,35,39],(8,4):[69,59,37,41],(10,4):[69,61,39,43],(12,4):[71,63,40,44],(4,6):[63,52,32,35],(6,6):[67,56,34,38],(8,6):[69,59,36,40],(10,6):[70,61,38,42],(12,6):[71,63,40,43],(4,8):[65,53,32,35],(6,8):[67,56,34,37],(8,8):[70,59,36,40],(10,8):[71,61,38,41],(12,8):[71,62,39,42],(4,10):[66,53,32,35],(6,10):[68,56,34,37],(8,10):[69,59,36,39],(10,10):[71,61,38,41],(12,10):[72,62,39,41],(4,12):[66,53,33,35],(6,12):[69,56,34,37],(8,12):[70,59,36,39],(10,12):[71,61,37,40],(12,12):[72,62,38,41]}

def get_nu(re, pr, prw, flow_type):
    if flow_type == 'B_HOT':
        if re < 1000: return 0.5 * (re**0.5) * (pr**0.38) * (pr/prw)**0.25
        elif re < 200000: return 0.25 * (re**0.6) * (pr**0.38) * (pr/prw)**0.25
        else: return 0.023 * (re**0.8) * (pr**0.37) * (pr/prw)**0.25
    else:
        if re > 10000: return 0.021 * (re**0.8) * (pr**0.43) * (pr/prw)**0.25
        elif re > 2320: return (2.2 + (re-2320)*(33-2.2)/(10000-2320)) * (pr**0.43) * (pr/prw)**0.25
        else: return 0.15 * (re**0.33) * (pr**0.43) * (pr/prw)**0.25

def calculate_set(label, raw, length):
    res = []
    for gh in [4,6,8,10,12]:
        for gc in [4,6,8,10,12]:
            t1i,t1o,t2i,t2o = raw[(gh,gc)]
            t1a = (t1i+t1o)/2; t2a = (t2i+t2o)/2
            r1 = WaterProperties.get(WaterProperties.rho, t1a); r2 = WaterProperties.get(WaterProperties.rho, t2a)
            c1 = WaterProperties.get(WaterProperties.cp, t1a); c2 = WaterProperties.get(WaterProperties.cp, t2a)
            l1 = WaterProperties.get(WaterProperties.lam, t1a); l2 = WaterProperties.get(WaterProperties.lam, t2a)
            m1 = WaterProperties.get(WaterProperties.mu, t1a); m2 = WaterProperties.get(WaterProperties.mu, t2a)
            p1 = WaterProperties.get(WaterProperties.pr, t1a); p2 = WaterProperties.get(WaterProperties.pr, t2a)
            g1 = (gh*0.001/60)*r1; g2 = (gc*0.001/60)*r2
            w1 = g1/(r1*A1); w2 = g2/(r2*A2)
            re1 = (w1*D1_IN*r1)/m1; re2 = (w2*(D2_IN-D1_OUT)*r2)/m2
            q1 = g1*c1*(t1i-t1o); q2 = g2*c2*(t2o-t2i); qa = (q1+q2)/2
            dm = t1i-t2o; dn = t1o-t2i
            lmtd = (dm-dn)/math.log(dm/dn) if dm!=dn and dm>0 and dn>0 else (dm+dn)/2
            tw = (t1a+t2a)/2
            for _ in range(5):
                pw = WaterProperties.get(WaterProperties.pr, tw)
                n1 = get_nu(re1, p1, pw, f"{label}_HOT"); n2 = get_nu(re2, p2, pw, f"{label}_COLD")
                a1 = (n1*l1)/D1_IN; a2 = (n2*l2)/(D2_IN-D1_OUT)
                t1w = t1a - qa/(a1*math.pi*D1_IN*length); t2w = t2a + qa/(a2*math.pi*D1_OUT*length)
                tw = (t1w+t2w)/2
            ks = math.pi / (1/(a1*D1_IN) + math.log(D1_OUT/D1_IN)/(2*LAMBDA_W) + 1/(a2*D1_OUT))
            kexp = qa/(lmtd*length) if lmtd>0 else 0
            res.append({'id':len(res)+1,'gh':gh,'gc':gc,'t1i':t1i,'t1o':t1o,'t1a':t1a,'rho1':r1,'cp1':c1,'lam1':l1,'mu1':m1,'pr1':p1,'t2i':t2i,'t2o':t2o,'t2a':t2a,'rho2':r2,'cp2':c2,'lam2':l2,'mu2':m2,'pr2':p2,'q1':q1,'q2':q2,'qa':qa,'dq':q1-q2,'lmtd':lmtd,'w1':w1,'re1':re1,'w2':w2,'re2':re2,'n1':n1,'a1':a1,'n2':n2,'a2':a2,'ks':ks,'ke':kexp,'er':abs(ks-kexp)/kexp*100 if kexp>0 else 0})
    return res

rb = calculate_set('B', raw_tube_b, 0.925); rc = calculate_set('C', raw_tube_c, 1.0)

def write_table(f, data, title, keys, fmts):
    f.write(f"% --- {title} ---\n")
    for r in data:
        row = " & ".join([format(r[k], f) if f else str(r[k]) for k, f in zip(keys, fmts)])
        f.write(f"    {row} \\\\\n")

with open('result_tables.txt', 'w') as f:
    write_table(f, rb, "TABLE 4: HOT B", ['id', 'gh', 'gc', 't1i', 't1o', 't1a', 'rho1', 'cp1', 'lam1', 'mu1', 'pr1'], [None, '.0f', '.0f', '.0f', '.0f', '.2f', '.2f', '.0f', '.4f', '.2e', '.2f'])
    write_table(f, rb, "TABLE 5: COLD B", ['id', 'gh', 'gc', 't2i', 't2o', 't2a', 'rho2', 'cp2', 'lam2', 'mu2', 'pr2'], [None, '.0f', '.0f', '.0f', '.0f', '.2f', '.2f', '.0f', '.4f', '.2e', '.2f'])
    write_table(f, rc, "TABLE 6: HOT C", ['id', 'gh', 'gc', 't1i', 't1o', 't1a', 'rho1', 'cp1', 'lam1', 'mu1', 'pr1'], [None, '.0f', '.0f', '.0f', '.0f', '.2f', '.2f', '.0f', '.4f', '.2e', '.2f'])
    write_table(f, rc, "TABLE 7: COLD C", ['id', 'gh', 'gc', 't2i', 't2o', 't2a', 'rho2', 'cp2', 'lam2', 'mu2', 'pr2'], [None, '.0f', '.0f', '.0f', '.0f', '.2f', '.2f', '.0f', '.4f', '.2e', '.2f'])
    
    f.write("% --- TABLE 8: Q B ---\n")
    for r in rb: f.write(f"    {r['id']} & {r['t1i']-r['t1o']:.0f} & {r['q1']:.2f} & {r['t2o']-r['t2i']:.0f} & {r['q2']:.2f} & {r['dq']:.2f} \\\\\n")
    f.write("% --- TABLE 9: Q C ---\n")
    for r in rc: f.write(f"    {r['id']} & {r['t1i']-r['t1o']:.0f} & {r['q1']:.2f} & {r['t2o']-r['t2i']:.0f} & {r['q2']:.2f} & {r['dq']:.2f} \\\\\n")
    
    f.write("% --- TABLE 10: LMTD B ---\n")
    for r in rb: f.write(f"    {r['id']} & {r['t1i']-r['t2o']:.2f} & {r['t1o']-r['t2i']:.2f} & {r['lmtd']:.2f} \\\\\n")
    f.write("% --- TABLE 11: LMTD C ---\n")
    for r in rc: f.write(f"    {r['id']} & {r['t1i']-r['t2o']:.2f} & {r['t1o']-r['t2i']:.2f} & {r['lmtd']:.2f} \\\\\n")

    write_table(f, rb, "TABLE 15: FLOW B", ['id', 'w1', 're1', 'lam1', 'w2', 're2', 'lam2'], [None, '.4f', '.1f', '.4f', '.4f', '.1f', '.4f'])
    write_table(f, rc, "TABLE 16: FLOW C", ['id', 'w1', 're1', 'lam1', 'w2', 're2', 'lam2'], [None, '.4f', '.1f', '.4f', '.4f', '.1f', '.4f'])

    write_table(f, rb, "TABLE 19: ALPHA B", ['id', 'pr1', 'n1', 'a1', 'n2', 'a2'], [None, '.2f', '.2f', '.2f', '.2f', '.2f'])
    write_table(f, rc, "TABLE 20: ALPHA C", ['id', 'pr1', 'n1', 'a1', 'n2', 'a2'], [None, '.2f', '.2f', '.2f', '.2f', '.2f'])

    write_table(f, rb, "TABLE 21: K B", ['id', 'ks', 'ke', 'er'], [None, '.2f', '.2f', '.2f'])
    write_table(f, rc, "TABLE 22: K C", ['id', 'ks', 'ke', 'er'], [None, '.2f', '.2f', '.2f'])

    write_table(f, rb, "TABLE 30: DEPENDENCE B", ['id', 're2', 'a1', 'a2', 'ks'], [None, '.1f', '.1f', '.1f', '.1f'])
    write_table(f, rc, "TABLE 31: DEPENDENCE C", ['id', 're2', 'a1', 'a2', 'ks'], [None, '.1f', '.1f', '.1f', '.1f'])

    print("FINISHED", file=sys.stderr)
