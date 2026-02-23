# הגדרת משתנים
q = 0.02
gen = 500

# פתיחת קובץ 
f = open('results/CF_freq.txt', 'w')
f.write("Generation\tFreq_c\tFreq_CC\tFreq_Cc\tFreq_cc\n")

# הגדרת לולאת דורות
for i in range(1, gen + 1):
    # חישוב ההתפלגויות של שכיחות האלל q והתפלגות הגנוטיפים CC, Cc, cc.
    p = 1 - q
    CC = p**2
    Cc = 2*q*p
    cc = q**2
    q = q / (q + 1)

    # כתיבה בקובץ
    f.write(f"{i}\t{round(q,5)}\t{round(CC,5)}\t{round(Cc,5)}\t{round(cc,5)}\n")
# סגירת הקובץ
f.close()
