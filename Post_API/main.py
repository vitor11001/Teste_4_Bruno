from requests import post, get
from requests.exceptions import ConnectTimeout, ConnectionError
from json import loads

class Consumo_API():
    def __init__(self) -> None:
        #self.url_api = 'https://api.open-meteo.com/v1/forecast?latitude=--8.28&longitude=-35.98&current_weather=true'
        self.url_api = 'https://api.open-meteo.com/v1/forecast?latitude=-8.28&longitude=-35.98&current_weather=true'
    
    def post_api(self) -> None:
        try:
            #p_api = post(self.url_api)
            p_api = get(self.url_api)
            if p_api.status_code == 200:
                print('Bom dia, essas são as condiçoes climáticas em Caruaru: ')
                for key, value in loads(p_api.text).items():
                    print(f'{key}: {value}')
                    
        except ConnectTimeout:
            print(f'Timeout ao tentar acessar: {self.site}')
        
        except ConnectionError:
            print('Sem acesso a internet! Verifique a conexão com a internet!')
            
        except:
            print('Erro desconhecido!')
            
###############################################################################