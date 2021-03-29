#PubSched
Runs pubmed7 once a week.

# pubmed7
A bit of code that searches PubMed for entries published in a given amount of time by a custom author list. Can be run on its own.

Search parameters are defined by the value <a href="https://www.ncbi.nlm.nih.gov/books/NBK25499/">reldate</a> and the author list names.txt .

## To run pubmed7 immediately

1. Download files.
2. Edit the Entrez.email field to comply with <a href="https://www.ncbi.nlm.nih.gov/books/NBK25497/">NCBI e-utility policies</a>.
``` 
Entrez.email = "your-email@address.com"
```
3. Edit names.txt to contain the names of your labmates, collaborators, or other scientists.
4. Open your terminal and point it to the directory containing the files, and run:
```
python pubmed7.py
```
5. If a publication has appeared on PubMed under that author's name in the last 7 days, it will be printed.

## sample output for March 28, 2021:

>$ python pubmed7.py
>
>Doudna, Jennifer A
>
>   Cancer-specific loss of TERT activation sensitizes glioblastoma to DNA damage.
>     'Amen AM', 'Fellmann C', 'Soczek KM', 'Ren SM', 'Lew RJ', 'Knott GJ', 'Park JE', 'McKinney AM', 'Mancini A', 'Doudna JA', 'Costello JF'
>     Proc Natl Acad Sci U S A. 2021 Mar 30;118(13). pii: 2008772118. doi: 10.1073/pnas.2008772118.
>
>Charpentier, Emmanuelle
>
>   ?
>     ?
>     ?
>
>Sahin, Ugur
>
>   Patient-reported outcomes from the phase II FAST trial of zolbetuximab plus EOX compared to EOX alone as first-line treatment of patients with metastatic CLDN18.2+ gastroesophageal adenocarcinoma.
>     'Lordick F', 'Al-Batran SE', 'Ganguli A', 'Morlock R', 'Sahin U', 'Tureci O'
>     Gastric Cancer. 2021 Mar 23. pii: 10.1007/s10120-020-01153-6. doi: 10.1007/s10120-020-01153-6.
>
>   Lipoprotein apheresis efficacy and challenges: single center experience.
>     'Ozdemir ZN', 'Sahin U', 'Yildirim Y', 'Kaya CT', 'Ilhan O'
>     Hematol Transfus Cell Ther. 2021 Mar 14. pii: S2531-1379(21)00034-1. doi: 10.1016/j.htct.2021.01.009.
>
>Tureci, Ozlem
>
>   Patient-reported outcomes from the phase II FAST trial of zolbetuximab plus EOX compared to EOX alone as first-line treatment of patients with metastatic CLDN18.2+ gastroesophageal adenocarcinoma.
>     'Lordick F', 'Al-Batran SE', 'Ganguli A', 'Morlock R', 'Sahin U', 'Tureci O'
>     Gastric Cancer. 2021 Mar 23. pii: 10.1007/s10120-020-01153-6. doi: 10.1007/s10120-020-01153-6.
>
     
## notes
1. Empty records appear with three question marks; future versions will bypass empty records.
2. Duplicate citations appear.
3. Future versions should eliminate the square brackets around the author name outputs.
