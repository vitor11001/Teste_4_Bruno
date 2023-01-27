from Get_conexao.main import Verif_conex
from Post_API.main import Consumo_API
import logs

def main():
    print('''
          1 - Get google
          2 - Post API
          ''')
    
    escolha  = str(input('Escolha entre as duas opções: '))
    
    if escolha == '1':
        Verif_conex().get_google()
    
    elif escolha == '2':
        Consumo_API().post_api()
        
    else:
        print('opção invalida!')

if __name__ == '__main__':
    main()