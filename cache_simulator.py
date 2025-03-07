
import sys
import math

# Linha de comando simplificada:
# cache_simulator <nsets> <bsize> <assoc> <subst> <flag_saida> arquivo_de_entrada.bin
def main():

    # Possiveis erros de parametros
    if len(sys.argv) != 7:
        print("Parametros invalidos, formato correto: ") 
        print("python cache_simulator <nsets> <bsize> <assoc> <subst> <flag_saida> arquivo_de_entrada.bin")
        sys.exit(1)
    if (sys.argv[4] != "L" and sys.argv[4] != "l") and (sys.argv[4] != "R" and sys.argv[4] != "r") and (sys.argv[4] != "F" and sys.argv[4] != "f"):
        print("Parametro subst invalido, deve ser L, R ou F (lru, random ou fifo)")
        sys.exit(1)
    if sys.argv[5] != "0" and sys.argv[5] != "1":
        print("Parametro flag_saida invalido, deve ser 0 ou 1")
        sys.exit(1)
    
    # Abre o arquivo de entrada
    try:
        arquivo = open(sys.argv[6], "rb")
    except:
        print("Erro ao abrir o arquivo de entrada")
        sys.exit(1)

    nsets = int(sys.argv[1])
    bsize = int(sys.argv[2])
    assoc = int(sys.argv[3])
    subst = sys.argv[4]
    flag_saida = int(sys.argv[5])
    arquivo = sys.argv[6]

    #print("nsets: ", nsets)
    #print("bsize: ", bsize)
    #print("assoc: ", assoc)
    #print("subst: ", subst)
    #print("flag_saida: ", flag_saida)
    #print("arquivo: ", arquivo)

    # Inicializa a cache
    cache_val = [[0] * assoc for _ in range(nsets)]  # array com o bit de validade de cada bloco
    cache_tag = [[-1] * assoc for _ in range(nsets)]  # array com a tag de cada bloco

    n_bit_offset = int(math.log2(bsize))    
    n_bit_indice= int(math.log2(nsets))

    n_bits_tag = 32 - n_bit_offset - n_bit_indice


    le_arquivo(arquivo, print(), n_bit_offset, n_bit_indice)
#    print("n_bit_offset: ", n_bit_offset)
#    print("n_bit_indice: ", n_bit_indice)
#    print("n_bits_tag: ", n_bits_tag)

#    pretty_print_cache(cache_val, cache_tag)
    

def pretty_print_cache(cache_val, cache_tag):
    print("Cache:")
    for i in range(len(cache_val)):
        print("========== Linha ", i, "==========")
        for j in range(len(cache_val[i])):
            print("Bloco ", j, end=" ")
            print("Validade: ", cache_val[i][j], end=" ")
            print("Tag: ", cache_tag[i][j])

    return

def le_arquivo(arquivo, callback, n_bits_offset, n_bits_indice):
    print("lendo arquivo")
    with open(arquivo, "rb") as arquivo_de_entrada:
        while True:
            endereco = arquivo_de_entrada.read(4)
            if not endereco:
                break
            endereco = int.from_bytes(endereco, byteorder="big")
            tag = endereco >> (n_bits_offset + n_bits_indice)  # Extrai a tag
            indice = (endereco >> n_bits_offset) & ((2**n_bits_indice) - 1)  # Extrai o indice

            print(f"Endereço: {endereco}, Tag: {tag}, Índice: {indice}")
    return


if __name__ == "__main__":
    main()
    sys.exit(0)

