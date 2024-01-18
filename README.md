# Python projekts - Netflix reģiona noteikšana
## Projekta uzdevums
Šī projekta uzdevums ir izveidot programmu, kas spēj noteikt, kurā Netflix reģionā ir pieejama noteiktā filma, lai lietotājs var izmantot kādu VPN programmatūru, lai varētu iestatīt savu reģionu uz reģionu, kurā filma ir pieejama un tad to noskatīties Netflix interneta lapā. Lai to varētu panākt, ir jāiegūst avots, no kura var uzzināt, kuros pasaules reģionos konkrētas Netflix filmas ir pieejamas. Viens veids varētu būt no mājaslapām, kurās ir pieejama datubāze ar lielu skaitu Netflix filmām un reģioniem, kurās tās ir pieejamas, bet lielākā daļa no mājaslapām nav uzticamas, jo ar laiku šī informācija noveco un tā nekad netiek atjaunota. Pašā Netflix mājaslapā arī nav iespējams atrast, kuros reģionos filmas ir pieejamas, jo Netflix ir saslēgts ar konkrēto atrašanās vietas reģionu, kuram ir konkrēts filmu klāsts. Tā vietā, ņemot vērā Netflix saslēgšanos ar reģionu, to var apiet, izmantojot Google Search interneta lapu, jo Google var atrast mājaslapas visos reģionos, un tas arī ir iespējams ar netflix filmu mājaslapām, kas tieši ir adresētas kādai noteiktai filmai, kādā noteiktā reģionā. Tad no Netflix filmas mājaslapas adreses var iegūt informāciju par reģionu, kas ir dots ISO 3166-1 alpha-2 formātā, piemēram, Latvijai šis kods būtu LV. Tāpēc ir jāizveido programma, kas spēj izmantot Google, lai atrastu noteiktās filmas Netflix mājaslapas adresi un tad nolasīt reģiona kodu adresē, un izveidotā sarakstā atrast kodam atbilstošo valsti.   
## Programmas instrukcija
Lai varētu pareizi palaist programmu, ir nepieciešams ielādēt visus failus uz datora un instalēt nepieciešamās bibliotēkas. Datorā ir jābūt instalētam Python un Google Chrome, lai programma strādātu.
Zemāk ir norādīti soļi, lai varētu pareizi uzstādīt programmu.

Programmas uzstādīšanas instrukcija:
1. Pārliecināties, vai datorā ir instalēts Python un Google Chrome. Ja nav, tad ir nepieciešams lejupielādēt un instalēt Python un Google Chrome no sekojošajām mājaslapām: https://www.python.org/downloads/ https://www.google.com/chrome/?brand=FHFK&gclsrc=ds
3. Lejupielādēt visus failus(kods.py, requirements.txt, CountryCodes.xlsx) un ievietot tos vienā mapē.
4. Atvērt mapi teksta apstrādes programmā (ieteicams izmantot: Visual Studio Code).
5. Python konsolē ierakstīt "pip install -r requirements.txt", kas automātiski instalēs visas nepieciešamās bibliotēkas, kas ir nepieciešamas, lai programma strādātu.

Programmas lietošanas instrukcija:
1. Palaist proframmas failu "kods.py".
2. Kad parādās konsolē uzraksts "Filmas nosaukums: ", tad ierakstīt vēlamās filmas nosaukumu tajā pašā konsolē un nospiest taustiņu "enter" uz klaviatūras.
3. Gaidīt, kamēr programma atver Google Chrome interneta pārlūku un to aizver.
4. Kad interneta pārlūks aizveras, tad konsolē vajadzētu parādīties reģiona nosaukumam, kurā ir pieejama ierakstītā filma.

## Programmas uzbūve
Progrmmā ir izmantotas 2 Python bibliotēkas - Selenium un Openpyxl. Selenium bibliotēka tiek izmantota, lai varētu izmantot Google Search funkcionalitāti caur Google Chrome interneta pārlūku. Kā arī ar to tiek atrasta un izvilkta filmas lapas adrese. Openpyxl tiek izmantots, lai varētu nolasīt informāciju no Excel faila, kurā ir teritoriju kodi un blakus tiem ir norādīti atbilstošo teritoriju nosaukumi. Tā var noteikt kurā valstī filma ir pieejama.

Programma soli pa solim darbojas šādi:
1. Importē bibliotēkas.
2. Izvada uz ekrāna "Ievadiet filmas nosaukumu: ".
3. Pēc nosaukuma ievades, atver Google Chrome pārlūku un tajā atver Google mājaslapu.
4. Gaida 0,5 sekundes un pēc tam atrod pogu "Reject all" Google sīkfailu logā un to noklikšķina.
5. Gaida 0,1 sekundi, lai pazūd sīkfailu logs un tad atrod meklēšanas teksta logu, kurā ieraksta lietotāja ievadīto filmas nosaukumu un klāt tam pieraksta " netflix" un nospiež enter pogu.
6. Gaida 1 sekundi un nolasa pirmā rezultāta interneta lapas adresi, pēc kā Google Chrome pārlūks tiek aizvērts.
7. Adresi saraksta veidā sadala locekļos un izvelk reģionu no adreses.
8. Pēc adreses nosaka, vai šī adrese ir Netflix lapas adrese un vai šajai adresei ir norādīts reģions.
9. Ja ir reģions norādīts, tad excel failā tiek atrasts atbilstošā reģiona nosaukums un tas tiek izvadīts uz ekrāna.

