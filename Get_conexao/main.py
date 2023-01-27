from requests import get
from requests.exceptions import ConnectTimeout, ConnectionError
from os.path import dirname, realpath
from datetime import datetime

class Verif_conex():
    def __init__(self) -> None:
        self.site = 'https://www.google.com.br/'
        self.dir_absoluto = dirname(realpath(__file__))
        self.msg_log = f'URI: {self.site} Datetime: {datetime.now()}'
    
    def get_google(self) -> None:
        try:
            g_site = get(self.site, timeout=5)
            if g_site.status_code == 200:
                print(f'{g_site} - Foi possível acessar o site: {self.site}')
                self.cria_edita_arquivo('last_successful_connection_attempt.txt', 'w')
            
            else:
                print(f'{g_site} - Não foi possível acessar o site: {self.site}')
            
        except ConnectTimeout:
            print(f'Timeout ao tentar acessar: {self.site}')
            self.cria_edita_arquivo('fail_connection_attempts.log', 'a')
        
        except ConnectionError:
            print('Sem acesso a internet! Verifique a conexão com a internet!')
            self.cria_edita_arquivo('fail_connection_attempts.log', 'a')
            
        except:
            print('Erro desconhecido!')
            self.cria_edita_arquivo('fail_connection_attempts.log', 'a')
            
    def cria_edita_arquivo(self, arq_name: str, abrir_arq_como: str) -> None:
        try:
            with open(str(self.dir_absoluto).replace('Get_conexao', 'logs/') + arq_name, abrir_arq_como) as arq:
                if abrir_arq_como == 'w':
                    arq.write(self.msg_log)
                elif abrir_arq_como == 'a':
                    arq.write('\n' + self.msg_log)
                
        except FileNotFoundError:
            print('Erro ao tentar abrir ou criar o arquivo! Verifique o diretório!')
            

###########################################################################################