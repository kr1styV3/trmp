# site produced by : @**_kr1styv3_**
## site owned by : @*temporanea* & *kr1*


 -------------------------------------------------


### queste sono le istruzioni per aggiornare il sito 

> dal momento che hai la cartella sul sistema
> apri un terminale
> [!IMPORTANT]
> *ricordati di fare**_git pull_*

> devi entrare nella cartella degli script
> sul terminale
```
cd scripts
cd py
```

> prima di tutto devi inserire le immagini
> questo viene fatto tramite *upload_photos.py*
> questo lo devi fare tramite *python3*
> su terminale dentro _/trmp/scripts/py/_
```
python3 upload_photos.py
```
> questo ti aprira un promt 
> dove dovrai fare quel che ti dice
> [!IMPORTANT]
> nel caso qualcosa va storto nel mentre
*_devi eliminare!!_*
```
cd ../../img/
rm -r ex*
cd ../scripts/py/
* inteso numero ultima mostra
python3 upload_photos.py
```

> dopo tramite altri 2 script aggiorni il codice
> nella stessa cartella
```
in questo ordine 
python3 create_pages.py
python3 update_index.py
```
> dopo che sei **sicurissimo** che hai fatto tutto giusto
> puoi fare 
```
cd ../../
git add .
git commit -m "messaggio riguardante mostra"
git push
```

> poi dopo 2 minuti controlla
[tmp](https://temporanea.art)
> e vedrai il sitto aggiornato
