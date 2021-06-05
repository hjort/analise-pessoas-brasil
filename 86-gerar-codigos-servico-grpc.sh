cd grpc/
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. genero_nome.proto
ls -1
cd -
