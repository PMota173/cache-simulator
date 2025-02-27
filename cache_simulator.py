# Linha de comando simplificada:
# cache_simulator <nsets> <bsize> <assoc> arquivo_de_entrada.bin

# Exemplo: python cache_simulator 64 32 1 bin1m.bin

import sys
import struct
import random

def generate_binary_file(filename, num_values):
    with open(filename, "wb") as f:
        for _ in range(num_values):
            value = random.randint(0, 2**32 - 1)  
            f.write(struct.pack("I", value))

def main():
    if len(sys.argv) != 5:
        print("Usage: python cache_simulator <nsets> <bsize> <assoc> <input_file>")
        sys.exit(1)

    nsets = int(sys.argv[1])
    bsize = int(sys.argv[2])
    assoc = int(sys.argv[3])
    input_file = sys.argv[4]

    print(f"nsets: {nsets}, bsize: {bsize}, assoc: {assoc}, input_file: {input_file}")

    generate_binary_file(input_file, 1000000)
    print(f"Arquivo {input_file} gerado com 1000000 valores aleatórios.")

if __name__ == "__main__":
    main()

