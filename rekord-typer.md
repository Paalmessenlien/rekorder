# Rekord-typer på rekord.bueskyting.no — teknisk dokumentasjon

Snapshot-dato: 2026-04-25.
Dokumentet kartlegger alle rekord-typer som publiseres på Norges Bueskytterforbunds rekordside, og kobler dem mot konkurransereferansen `Avstandstabell-mesterskap-skive-2024-11.pdf` (NBF, november 2024).

## 1. Innledning

En rekord på rekord.bueskyting.no identifiseres entydig av fem akser:

| Akse        | Beskrivelse                                  |
|-------------|----------------------------------------------|
| Divisjon    | Bueformat (Recurve, Compound, Barebow, …)    |
| Rundetype   | Konkurranseformat (1440-runde, 720, 18m …)   |
| Klasse      | Alder + kjønn, lag, eller spesialklasse      |
| Avstand     | Skyteavstand i meter                         |
| Skive       | Skiveformat / blink                          |

`Avstandstabell-mesterskap-skive-2024-11.pdf` er normgivende for hvilken avstand og skive som skal brukes i mesterskap "skive" (innendørs og utendørs). Dokumentet binder de to sammen.

## 2. Kilder

| Kilde            | Plassering / mønster                                                |
|------------------|---------------------------------------------------------------------|
| Indeks           | https://rekord.bueskyting.no/                                       |
| Rekord-side      | https://rekord.bueskyting.no/rekord.php?rundeid=`{id}`&divisjon=`{div}` |
| Avstandstabell   | `Avstandstabell-mesterskap-skive-2024-11.pdf` (NBF, 2024-11)        |

## 3. Divisjoner

Listet med navnet som brukes i URL-parameteren `divisjon=` og navnet som brukes i PDF-en.

| Site-label (`divisjon=`)     | PDF-label    | Norsk klartekst              |
|------------------------------|--------------|------------------------------|
| `Recurve`                    | Recurve      | Recurve                      |
| `Compound`                   | Compound     | Compound                     |
| `Barebow`                    | Barebow      | Barebue                      |
| `Langbue`                    | Langbue      | Langbue                      |
| `Tradisjonell`               | Tradisjonell | Tradisjonell                 |
| `Synshemmede`                | W1 (VI)      | Synshemmede / Visually Impaired |
| `PsykiskUtviklingshemmet`    | OC           | Psykisk utviklingshemmet / Open class |

## 4. Rundetyper

Alle 10 rundetyper på rekord.bueskyting.no, identifisert av URL-parameteren `rundeid=`.

| `rundeid` | Navn               | Inne/Ute | Antall piler | Format                                 |
|-----------|--------------------|----------|--------------|----------------------------------------|
| 3         | Skandiarunde       | Ute      | 90           | 3 avstander á 30 piler                 |
| 4         | Norgesrunde        | Ute      | 30           | 1 avstand á 30 piler                   |
| 5         | 1440-runde         | Ute      | 144          | 4 avstander á 36 piler                 |
| 6         | ½ 1440-runde       | Ute      | 72           | 4 avstander á 18 piler                 |
| 21        | Norsk kortrunde    | Ute      | 90           | 3 avstander á 30 piler                 |
| 26        | 720-runde          | Ute      | 72           | 1 avstand á 72 piler                   |
| 28        | 2 × 720-runde      | Ute      | 144          | 2 × 720 (samme avstand)                |
| 22        | 60 piler 18 m      | Inne     | 60           | 1 avstand                              |
| 23        | 60 piler 25 m      | Inne     | 60           | 1 avstand                              |
| 27        | 30 piler 18 m      | Inne     | 30           | 1 avstand                              |

Lenkemal: `https://rekord.bueskyting.no/rekord.php?rundeid={rundeid}&divisjon={divisjon}`. Alle 70 kombinasjoner (10 rundeid × 7 divisjoner) eksisterer.

## 5. Klasser

### 5.1 Standard klasse-sett (Recurve, Compound, Barebow, Langbue, Tradisjonell)

| Gruppe        | Klasser                                                                 |
|---------------|-------------------------------------------------------------------------|
| Individuelt   | Damer Senior, Herrer Senior, Damer 50, Herrer 50, Damer U21, Herrer U21, Damer U18, Herrer U18, Jenter U16, Gutter U16 |
| Mix2 (lag)    | Mix2 Senior, Mix2 50+, Mix2 U21, Mix2 U18, Mix2 U16                     |
| Lag           | Lag per individuell klasse (utendørs runder; også enkelte innendørs)    |

### 5.2 Spesialdivisjonene Synshemmede og Psykisk utviklingshemmet

| Gruppe       | Klasser              |
|--------------|----------------------|
| Individuelt  | Felles (kombinert)   |
| Lag          | Lag                  |

Disse divisjonene har én fellesklasse (ikke kjønns- eller alderdelt) og kun én utendørs/innendørs avstand.

### 5.3 Merknader

- Mix2 er parlag og finnes på samtlige rundetyper for de fem standarddivisjonene, men ikke for spesialdivisjonene.
- Lag-rekorder finnes på alle utendørs runder for standarddivisjonene; innendørs er Lag eksplisitt registrert på 18 m / 25 m for noen divisjoner og rundeid 22 / 23 / 27.
- BB, Trad og LB U18 kan sette rekord i egen aldersbestemte klasse, eventuelt i alderstrinnet over dersom skytter deltar der (jf. PDF-fotnote).

## 6. Sub-avstander per (rundetype × divisjon)

Multi-avstandsrundene har egne delavstander per klasse. Listene under er hentet fra primærkilden (rekord-sidene).

### 6.1 Skandiarunde (`rundeid=3`) — 90 piler ute

| Divisjon                | Voksen-klasser (Sen/50/U21/U18) | U16 (Jenter/Gutter) |
|-------------------------|---------------------------------|---------------------|
| Recurve                 | 60 m, 50 m, 40 m                | 40 m, 30 m, 20 m    |
| Compound                | 60 m, 50 m, 40 m                | 40 m, 30 m, 20 m    |
| Barebow (Sen/50/U21)    | 40 m, 30 m, 20 m                | 25 m, 20 m, 15 m    |
| Barebow U18             | 30 m, 25 m, 20 m                | —                   |
| Langbue                 | 30 m, 25 m, 20 m                | 25 m, 20 m, 15 m    |
| Tradisjonell            | 30 m, 25 m, 20 m                | 25 m, 20 m, 15 m    |
| Synshemmede             | 20 m (Felles)                   | —                   |
| Psykisk utviklingshemmet| 20 m (Felles)                   | —                   |

### 6.2 Norgesrunde (`rundeid=4`) — 30 piler ute, én avstand

| Divisjon                | Voksen | U16  |
|-------------------------|--------|------|
| Recurve                 | 50 m   | 30 m |
| Compound                | 50 m   | 30 m |
| Barebow                 | 30 m   | 20 m |
| Langbue                 | 25 m   | 25 m |
| Tradisjonell            | 25 m   | 25 m |
| Synshemmede             | 20 m   | —    |
| Psykisk utviklingshemmet| 20 m   | —    |

### 6.3 1440-runde (`rundeid=5`) — 144 piler ute

| Divisjon × klassegruppe                        | Sub-avstander                |
|------------------------------------------------|------------------------------|
| Recurve Herrer Senior, Herrer U21              | 90, 70, 50, 30 m             |
| Recurve Damer Senior, Damer U21                | 90, 70, 60, 50, 30 m¹        |
| Recurve Herrer 50, Herrer U18                  | 70, 60, 50, 30 m             |
| Recurve Damer 50, Damer U18                    | 60, 50, 40, 30 m             |
| Recurve Jenter/Gutter U16                      | 50, 40, 30, 20 m             |
| Compound Herrer Senior, Herrer U21             | 90, 70, 50, 30 m             |
| Compound Damer Senior, Damer U21               | 70, 60, 50, 30 m             |
| Compound Herrer 50, Herrer U18                 | 70, 60, 50, 30 m             |
| Compound Damer 50, Damer U18                   | 60, 50, 40, 30 m             |
| Compound Jenter/Gutter U16                     | 50, 40, 30, 20 m             |
| Barebow voksen (Sen/50/U21/U18)                | 50, 40, 30, 20 m             |
| Barebow Damer U18                              | 40, 30, 25, 20 m             |
| Barebow Jenter/Gutter U16                      | 30, 25, 20, 15 m             |
| Langbue voksen (Sen/50/U21/U18)                | 40, 30, 25, 20 m             |
| Langbue U16                                    | 30, 25, 20, 15 m             |
| Tradisjonell voksen (Sen/50/U21/U18)           | 40, 30, 25, 20 m             |
| Tradisjonell U16                               | 30, 25, 20, 15 m             |
| Synshemmede Felles                             | 20 m                         |
| Psykisk utviklingshemmet Felles                | 20 m                         |

¹ Recurve Damer Senior/U21 publiseres med både `Total` og separat `Total 90 m` (delskår fra 90 m alene).

### 6.4 ½ 1440-runde (`rundeid=6`) — 72 piler ute
Samme delavstander som 1440-runde, men 18 piler per avstand i stedet for 36.

### 6.5 Norsk kortrunde (`rundeid=21`) — 90 piler ute

| Divisjon                | Voksen-klasser     | U16              |
|-------------------------|--------------------|------------------|
| Recurve                 | 50, 35, 25 m       | 35, 25, 20 m     |
| Compound                | 50, 35, 25 m       | 35, 25, 20 m     |
| Barebow                 | 35, 25, 20 m       | 25, 20, 15 m     |
| Langbue                 | 30, 25, 20 m       | 25, 20, 15 m     |
| Tradisjonell            | 30, 25, 20 m       | 25, 20, 15 m     |
| Synshemmede             | 20 m (Felles)      | —                |
| Psykisk utviklingshemmet| 20 m (Felles)      | —                |

### 6.6 720-runde (`rundeid=26`) og 2 × 720-runde (`rundeid=28`)

| Divisjon                | Senior/U21 | 50+ / U18 | U16  |
|-------------------------|------------|-----------|------|
| Recurve                 | 70 m       | 60 m      | 40 m |
| Compound                | 50 m       | 50 m      | 30 m |
| Barebow                 | 50 m       | 50 / 40 m¹| 25 m |
| Langbue                 | 30 m       | 30 m      | 25 m |
| Tradisjonell            | 30 m       | 30 m      | 25 m |
| Synshemmede             | 20 m       | —         | —    |
| Psykisk utviklingshemmet| 20 m       | —         | —    |

¹ Barebow U18 skyter 40 m, mens Barebow 50+ skyter 50 m.

### 6.7 Innendørs (`rundeid=22, 23, 27`)

Alle divisjoner har samme avstand for alle klasser i en gitt innendørsrunde.

| `rundeid` | Navn           | Avstand alle div./klasser           |
|-----------|----------------|-------------------------------------|
| 22        | 60 piler 18 m  | 18 m                                |
| 23        | 60 piler 25 m  | 25 m                                |
| 27        | 30 piler 18 m  | 18 m                                |

For PsykiskUtviklingshemmet/OC innendørs er PDF-avstanden 12 m, men site bruker 18 m i `rundeid=22/27` (se § 8 og § 9).

## 7. Avstandstabellen som strukturerte data

Reproduksjon av PDF-en `Avstandstabell-mesterskap-skive-2024-11.pdf`. Hver rad gir avstand og skive for innendørs- og utendørs (skive) mesterskap.

| Divisjon     | Klasse (Betegnelse) | Inne avstand | Inne skive            | Ute avstand | Ute skive          |
|--------------|---------------------|--------------|-----------------------|-------------|--------------------|
| Recurve      | Damer/Herrer Senior | 18 m         | 40 cm (trippel/1–10)  | 70 m        | 122 cm (1–10)      |
| Recurve      | Damer/Herrer 50+    | 18 m         | 40 cm (trippel/1–10)  | 60 m        | 122 cm (1–10)      |
| Recurve      | Damer/Herrer U21    | 18 m         | 40 cm (trippel/1–10)  | 70 m        | 122 cm (1–10)      |
| Recurve      | Damer/Herrer U18    | 18 m         | 40 cm (trippel/1–10)  | 60 m        | 122 cm (1–10)      |
| Recurve      | Jenter/Gutter U16   | 18 m         | 60 cm (1–10)          | 40 m        | 122 cm (1–10)      |
| Compound     | Damer/Herrer Senior | 18 m         | 40 cm (trippel)       | 50 m        | 80 cm (5–10)       |
| Compound     | Damer/Herrer 50+    | 18 m         | 40 cm (trippel)       | 50 m        | 80 cm (5–10)       |
| Compound     | Damer/Herrer U21    | 18 m         | 40 cm (trippel)       | 50 m        | 80 cm (5–10)       |
| Compound     | Damer/Herrer U18    | 18 m         | 40 cm (trippel)       | 50 m        | 80 cm (5–10)       |
| Compound     | Jenter/Gutter U16   | 18 m         | 60 cm (trippel)       | 30 m        | 80 cm (5–10)       |
| Barebow      | Damer/Herrer Senior | 18 m         | 40 cm (trippel/1–10)  | 50 m        | 122 cm (1–10)      |
| Barebow      | Damer/Herrer 50+    | 18 m         | 40 cm (1–10)          | 50 m        | 122 cm (1–10)      |
| Barebow      | Damer/Herrer U21    | 18 m         | 40 cm (1–10)          | 50 m        | 122 cm (1–10)      |
| Barebow      | Damer/Herrer U18    | 18 m         | 40 cm (1–10)          | 40 m        | 122 cm (1–10)      |
| Barebow      | Jenter/Gutter U16   | 18 m         | 60 cm (1–10)          | 25 m        | 122 cm (1–10)      |
| Langbue      | Damer/Herrer Senior | 18 m         | 40 cm (1–10)          | 30 m        | 122 cm (1–10)      |
| Langbue      | Damer/Herrer 50+    | 18 m         | 40 cm (1–10)          | 30 m        | 122 cm (1–10)      |
| Langbue      | Damer/Herrer U21    | 18 m         | 60 cm (1–10)          | 30 m        | 122 cm (1–10)      |
| Langbue      | Damer/Herrer U18    | 18 m         | 60 cm (1–10)          | 30 m        | 122 cm (1–10)      |
| Langbue      | Jenter/Gutter U16   | 18 m         | 60 cm (1–10)          | 25 m        | 122 cm (1–10)      |
| Tradisjonell | Damer/Herrer Senior | 18 m         | 40 cm (1–10)          | 30 m        | 122 cm (1–10)      |
| Tradisjonell | Damer/Herrer 50+    | 18 m         | 40 cm (1–10)          | 30 m        | 122 cm (1–10)      |
| Tradisjonell | Damer/Herrer U21    | 18 m         | 60 cm (1–10)          | 30 m        | 122 cm (1–10)      |
| Tradisjonell | Damer/Herrer U18    | 18 m         | 60 cm (1–10)          | 30 m        | 122 cm (1–10)      |
| Tradisjonell | Jenter/Gutter U16   | 18 m         | 60 cm (1–10)          | 25 m        | 122 cm (1–10)      |
| W1 (VI)      | Synshemmede         | 18 m         | 60 cm (1–10)          | 30 m        | 80 cm (1–10)       |
| OC           | Open class          | 12 m         | 60 cm (1–10)          | 20 m        | 122 cm (1–10)      |

### 7.1 PDF-fotnoter (innendørs)

1. Alle, foruten Tradisjonell, Langbue, W1 og OC, skyter trippel-skiver i match- og finalerunder.
2. Recurve Senior, 50+, U21 og U18 kan velge mellom full- eller trippelskive innledningsvis.
3. Barebow Senior kan velge mellom full- eller trippelskive innledningsvis.
4. BB, Trad og LB U18 kan sette rekord i egen aldersbestemt klasse, eventuelt i alderstrinnet over dersom skytter deltar i denne klassen.

## 8. Mapping site ↔ PDF

PDF-en dekker primært `Innendørs` og `Skive/utendørs` som er enkeltavstand-mesterskap. Multi-avstands-rundene på site har egne avstandsbord (se § 6) og er ikke i PDF-en.

| Site rundeid | Site-runde         | PDF-kolonne                | Forhold                                                                                          |
|--------------|--------------------|----------------------------|--------------------------------------------------------------------------------------------------|
| 22           | 60 piler 18 m      | Innendørs (alle div.)      | Direkte: 18 m og skive følger PDF-rad for hver klasse                                            |
| 27           | 30 piler 18 m      | Innendørs (alle div.)      | Samme avstand/skive som rundeid 22, halvert antall piler                                         |
| 23           | 60 piler 25 m      | (ingen)                    | 25 m innendørs er ikke en NM-disiplin i PDF-en; rekorder fortsatt registrert                     |
| 26           | 720-runde          | Skive/utendørs (alle div.) | Direkte: avstand og skive følger PDF-rad                                                         |
| 28           | 2 × 720-runde      | Skive/utendørs (alle div.) | Samme PDF-rad som rundeid 26; doblet antall piler                                                |
| 5            | 1440-runde         | Skive/utendørs (lengste)   | PDF-avstanden er den lengste delavstanden (90 m for Recurve Sen, 50 m for Compound 50, osv.)     |
| 6            | ½ 1440-runde       | Skive/utendørs (lengste)   | Som 1440-runde, men 18 piler per avstand                                                         |
| 3            | Skandiarunde       | (ingen)                    | Egne avstander (§ 6.1) som ikke nødvendigvis matcher PDF                                         |
| 4            | Norgesrunde        | (ingen)                    | Enkelt-avstand, men typisk kortere enn PDF (f.eks. Recurve Sen 50 m vs PDF 70 m)                 |
| 21           | Norsk kortrunde    | (ingen)                    | Egne kortere avstander                                                                           |

### 8.1 Klassemapping site ↔ PDF

| Site-klasse                     | PDF-betegnelse                  |
|---------------------------------|---------------------------------|
| Damer Senior + Herrer Senior    | Damer/Herrer Senior             |
| Damer 50 + Herrer 50            | Damer/Herrer 50+                |
| Damer U21 + Herrer U21          | Damer/Herrer U21                |
| Damer U18 + Herrer U18          | Damer/Herrer U18                |
| Jenter U16 + Gutter U16         | Jenter/Gutter U16               |
| Mix2 (alle aldre)               | (ikke i PDF; lagskår)           |
| Lag (alle aldre)                | (ikke i PDF; aggregert lagskår) |
| Synshemmede › Felles            | W1 (VI) Synshemmede             |
| Psykisk utviklingshemmet › Felles | OC Open class                 |

## 9. Spesialtilfeller og konvensjoner

1. **Trippel- vs full-skive innendørs**
   - Recurve Senior, 50+, U21 og U18 kan velge full- eller trippel-40 cm innledningsvis; trippel-skiver brukes alltid i match- og finalerunder.
   - Barebow Senior kan velge full- eller trippelskive innledningsvis; Barebow 50+ / U21 / U18 skyter full 40 cm.
   - Compound bruker alltid trippel-40 cm innendørs (og trippel-60 cm for U16).
   - Langbue, Tradisjonell, Synshemmede og OC skyter alltid full-skive (1–10).

2. **U16 innendørs på 60 cm**: alle divisjoner skyter 60 cm-skive innendørs i U16; for Compound er den triplet, ellers 1–10.

3. **Compound-scoring**: `5–10` på 80 cm utendørs betyr at kun 5-ringen og inn teller (ikke 1–4).

4. **Synshemmede / W1**: PDF gir 18 m inne / 30 m ute med 60 cm / 80 cm-skive. Site bruker imidlertid 20 m i utendørs-rundene (§ 6) — det er rekordavstanden som er etablert, ikke nødvendigvis PDF-NM-avstanden.

5. **Psykisk utviklingshemmet / OC**: PDF gir 12 m inne / 20 m ute. Site bruker 18 m innendørs på `rundeid=22/27` og 20 m utendørs. Innendørs-avviket bør verifiseres mot gjeldende rekordregelverk.

6. **U18-klasseopprykk**: Barebow, Tradisjonell og Langbue U18-skyttere kan registrere rekord i U18 eller i klassen over dersom de deltar der.

7. **Mix2**: parlag-rekorder; rapporteres som sum av to skytteres skår, finnes for alle 5 standarddivisjoner og alle 10 rundetyper.

8. **Lag**: én lagrekord per klasse. Spesielt `rundeid=23` (60 piler 25 m) eksponerer Lag-rekorder per (kjønn × aldersklasse) for Recurve.

9. **`Total 90 m` for Recurve Damer Senior/U21 i 1440**: separat rekord for kun 90 m-delen av runden (delavstandsskår), i tillegg til ordinær Total.

## 10. Verifikasjon

- **Full sweep utført 2026-04-25**: alle 70 kombinasjoner av (`rundeid`, `divisjon`) ble hentet og bekreftet å eksistere på rekord.bueskyting.no. Klasse- og delavstandslistene i § 6 og § 5 er hentet direkte fra disse sidene.
- **PDF**: alle 27 rader fra `Avstandstabell-mesterskap-skive-2024-11.pdf` er gjengitt i § 7 inkludert fotnoter.
- **Mapping**: § 8 verifisert ved at PDF Innendørs-avstander (18 m for alle utenom OC) og PDF Skive/utendørs-avstander matcher henholdsvis `rundeid=22/27` og `rundeid=26/28` for hver klasse.
- **Avvik notert**: kun Synshemmede/OC-divisjonene har site-avstander som ikke samsvarer fullstendig med PDF-en (§ 9 punkt 4 og 5).

For å re-verifisere: åpne `https://rekord.bueskyting.no/rekord.php?rundeid=<id>&divisjon=<div>` for ønsket kombinasjon og sammenlign klasselista og avstandene mot tabellen.
