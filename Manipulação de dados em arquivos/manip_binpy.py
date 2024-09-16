#Situação-problema: Em uma pequena empresa de design gráfico, surgiu a necessidade de implementar um sistema capaz de manipular imagens para uso em diferentes campanhas publicitárias. O gerente do projeto solicitou uma ferramenta que permita aos designers visualizarem, manipularem e criarem cópias de imagens no formato binário para entender melhor a estrutura de dados de imagens e explorar efeitos criativos através da manipulação direta desses dados.


#Objetivos do programa: Objetivos do programa
# 
# Desenvolver um programa em Python que execute as seguintes operações: Carregar uma imagem simples do sistema de arquivos.
#Converter a imagem em uma representação binária usando a biblioteca PIL (Python Imaging Library)
#Exibir os dados binários da imagem. 
#Salvar esses dados em um arquivo binário.
#Fazer uma cópia desse arquivo binário.
#Manipular os dados do arquivo binário cópia (por exemplo, inverter os bytes, adicionar ruído etc.).
#Carregar a imagem modificada a partir do arquivo binário e exibi-la para ver o efeito das manipulações.


def main():

    img = Image.open("simple_icon.png")
    img.show()
 
    
    img_data = np.array(img)
    binary_data = img_data.tobytes()
 
    
    with open("original_img.bin", "wb") as file:
        file.write(binary_data)
 
    
    with open("original_img.bin", "rb") as original_file:
        data = original_file.read()
    
    with open("copy_img.bin", "wb") as copy_file:
        copy_file.write(data)
 
    
    with open("copy_img.bin", "rb") as file:
        data = bytearray(file.read())
    
    
    data = data[::-1]
 
    with open("copy_img.bin", "wb") as file:
        file.write(data)
 
    
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)
    modified_img = Image.fromarray(modified_data)
    modified_img.show()
 
if __name__ == "__main__":
    main()