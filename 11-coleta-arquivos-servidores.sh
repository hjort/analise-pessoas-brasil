mkdir origem
cd origem

unzip 202012_Servidores.zip

file *.csv
for a in *.csv; do iconv -f iso88591 -t utf8 $a -o $$; mv -f $$ $a; done
file *.csv
head *.csv

bzip2 -9 *.csv

cd -

