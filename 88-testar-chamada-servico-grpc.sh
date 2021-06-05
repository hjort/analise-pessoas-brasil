# verificar se porta está aberta
echo
netstat -ante | grep :500
echo
lsof -i :50052
echo

# nomes de pessoa para testar chamada
NOMES="Maria Joao SOCORRO JOSE Leonor Djalma Esther JURACY Domingas ATILA Conceicao"

for nome in $NOMES
do
  #echo "=> $nome"
  python grpc/genero_nome_client.py --host localhost --port 50052 --nome $nome
done

