# Linha de comando simplificada:
# cache_simulator <nsets> <bsize> <assoc> <subst> <flag_saida> arquivo_de_entrada.bin


import sys
import math

def main():

    # possiveis erros de parametros
    if len(sys.argv) != 7:
        print("Parametros invalidos, formato correto: ") 
        print("python cache_simulator <nsets> <bsize> <assoc> <subst> <flag_saida> arquivo_de_entrada.bin")
        sys.exit(1)
    if sys.argv[4] != "L" and sys.argv[4] != "R" and sys.argv[4] != "F":
        print("Parametro subst invalido, deve ser L, R ou F (lru, random ou fifo)")
        sys.exit(1)
    if sys.argv[5] != "0" and sys.argv[5] != "1":
        print("Parametro flag_saida invalido, deve ser 0 ou 1")
        sys.exit(1)
    
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

    print("nsets: ", nsets)
    print("bsize: ", bsize)
    print("assoc: ", assoc)
    print("subst: ", subst)
    print("flag_saida: ", flag_saida)
    print("arquivo: ", arquivo)


    cache_val = [[0] * assoc for _ in range(nsets)]  # array com o bit de validade de cada bloco
    cache_tag = [[-1] * assoc for _ in range(nsets)]  # array com a tag de cada bloco

    n_bit_offset = int(math.log2(bsize))    
    n_bit_indice= int(math.log2(nsets))

    n_bits_tag = 32 - n_bit_offset - n_bit_indice

    print("n_bit_offset: ", n_bit_offset)
    print("n_bit_indice: ", n_bit_indice)
    print("n_bits_tag: ", n_bits_tag)

    print ("bits de validade: ", cache_val)
    print ("tags", cache_tag)


    # flag de saida 1: dados brutos
    #   ordem: Total de acessos, Taxa de hit, Taxa de miss, Taxa de miss compulsório, 
    #          Taxa de miss de capacidade, Taxa de miss de conflito
    
    # flag de saida 0: dados formatados com labels e valores

if __name__ == "__main__":
    main()
    sys.exit(0)

