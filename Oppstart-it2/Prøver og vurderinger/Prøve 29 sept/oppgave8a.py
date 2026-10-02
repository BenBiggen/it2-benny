def konverter_tid(sekunder):
    timer = sekunder // 3600
    resttimer = sekunder % 3600
    minutter = resttimer // 60
    restminutter = resttimer % 60

    return(f"{timer} t, {minutter}, m, {restminutter} s")

print(konverter_tid(4000)) #Her har jeg brukt // og % som i ene del oppgaven på oppgave 1 for å regne ut timer, minutter og sekunder
