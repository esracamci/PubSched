# PubSched
Runs pubmed7 once a week.
<a href="https://schedule.readthedocs.io/"> Modify the schedule</a>


# pubmed7
pubmed7 is bit of code that retrieves PubMed entries published within the last seven days.

Search parameters are defined by the value <a href="https://www.ncbi.nlm.nih.gov/books/NBK25499/">reldate</a> and the contents of terms.txt. 

## To run pubmed7 immediately

1. Download files.
2. Edit the Entrez.email field to comply with <a href="https://www.ncbi.nlm.nih.gov/books/NBK25497/">NCBI e-utility policies</a>.
``` 
Entrez.email = "your-email@address.com"
```
3. Edit terms.txt.
4. Open your terminal and point it to the directory containing the files and run:
```
python pubmed7.py
```
5. Output will be printed to the terminal.

>$ python pubmed7.py
>
>search term
>
>   Publication title.
>     ['Author A', 'Author B', 'Author C', 'Author D']
>     Journal Title. 2021 Mar 30:1-8. doi: nn.nnnn/nnnnnnnn.




## notes
1. Empty records appear with three question marks; future versions will bypass empty records.
2. Duplicate citations appear.
3. Future versions should eliminate the square brackets around the author name outputs.
