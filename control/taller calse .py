def validar_placa(placa):
    nueva=""
    for letra in placa:
        num=ord(letra)
        if num%2==0:
            num+=5
        else:
            num-=5
        nueva=nueva+chr(num)
    return nueva
print(validar_placa("123wer") 