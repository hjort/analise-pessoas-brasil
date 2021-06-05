# nomes de pessoas para testar chamadas
NOMES="Maria Joao SOCORRO JOSE Leonor Djalma Esther JURACY Domingas ATILA Conceicao"

for nome in $NOMES
do
  echo "=> $nome"
  curl 'http://localhost/prever' \
    -H 'Content-Type: application/json' \
    -d "{\"nome\":\"$nome\"}"
  echo
done
