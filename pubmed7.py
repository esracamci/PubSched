

##### iterate through terms.txt
terms = open("terms.txt").readlines()
for g in terms:


##### query pubmed for each term (author name), return PMIDs, print record
    from Bio import Entrez
    Entrez.email = "esracamci@gmail.com" # per NCBI, please edit to contain your email
    handle = Entrez.esearch(db="pubmed", term=g, reldate=7) # reldate=n, where n is days from today
    record = Entrez.read(handle)
    handle.close()
    idlist = record["IdList"]
    #print(record["IdList"])
    print(g)

    from Bio import Medline
    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
    records = Medline.parse(handle)
    records = list(records)

    for record in records:
         print("  ", record.get("TI", "?"))
         print("    ", record.get("AU", "?"))
         print("    ", record.get("SO", "?"))
         print("")
