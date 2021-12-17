# Youbike2.0
## main
`youbike.py` 

1. Download all the data.
2. Store them according to the time of which is downloaded.
3. Parse them to each excel file.

`station_constructor.py`

Generate `concerned.txt` file. Which store the youbike2.0 station **code(sno)** and **name(sna)** that its chinese name contains **臺大** or **公館**.

## data
The general structure rule is: `yyyy-mm-dd\hh\hh-mm`

`json`

Store all the `.json` files that were downloaded directly from website.

`excel`

Store all the `.xlsx` files that have been modified from `json`. Only keep some crucial information of stations we concerend about.
