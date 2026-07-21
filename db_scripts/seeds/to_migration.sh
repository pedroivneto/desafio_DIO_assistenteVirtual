#!/bin/bash

# Pegar o diretório atual onde o script está localizado
scriptDirectory="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Arquivo de saída com todos os SQLs
outputFile="${scriptDirectory}/migration.sql"

# Verificação de existência do arquivo; caso exista, deleta
if [ -f "$outputFile" ]; then
    rm "$outputFile"
fi

# Coleta o conteúdo dos arquivos .sql ordenados pelo nome (exceto o próprio migration.sql caso ele estivesse lá)
# Utiliza find e sort para ordenar corretamente
find "$scriptDirectory" -maxdepth 1 -type f -name "*.sql" ! -name "migration.sql" | sort | while read -r file; do
    # Concatena o conteúdo do arquivo SQL no arquivo de saída
    cat "$file" >> "$outputFile"
    
    # Adiciona a linha "GO" e uma nova linha ao final de cada arquivo
    echo "GO" >> "$outputFile"
done

echo "Todos os arquivos foram combinados em $outputFile"