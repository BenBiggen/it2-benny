temperaturer = [4.5, -2.0, 1.5, -6.5, 0.0, 3.0, -1.5, 7.0, 5.5, -3.5]
antallmålinger = len(temperaturer)
dagerunder0 = 0

print(f"det var {antallmålinger} målinger, første var {temperaturer[0]} C og siste var {temperaturer[antallmålinger-1]} C") #Her har jeg bare målt lengden av liste for antall målinger og tatt indeks 0 og indeksen av lengden -1 for første og siste måling

gjennomsnitt = ((sum(temperaturer)/antallmålinger)//0.1)/10

print(f"gjennomsnittet på målingene er {gjennomsnitt}")

for i in range(antallmålinger):
    if temperaturer[i]<0:
        dagerunder0 += 1

print(f"temperaturen var under 0 grader {dagerunder0} dager")