# DriveAutoBackup - 1.0.0

## Esse programa tem como objetivo a automatização de Backup's no Google Drive. 
### Como funciona:
 Por meio da utilização da biblioteca **PyAutoGui** [(Doc)](https://pyautogui.readthedocs.io/en/latest/) e suas diversas funções de automação, este script transforma uma pasta local em um tipo de . Dessa forma, ao rodar o script, todos os arquivos dentro dessa pasta serão enviados para sua conta do [Google Drive](https://www.google.com/intl/pt-BR/drive/).
Clone ou baixe o repositório com o comando: `https://github.com/YohansN/DriveAutoBackup.git`

### Requisitos:
- Python 3
- pyautogui

### Antes de rodar:
Algumas configurações podem e devem ser feitas no código!
1. Você deverá estar logado na conta do Google Drive que será utilizada.
2. Devem ser criadas duas pastas em qualquer local do Pc. Essas pastas serão as responsáveis por guardar os arquivos antes e após o upload no Drive. 
3. O nome dessas pastas devem ser passadas dentro do código. Caso não queira ter esse trabalho crie-as com os seguintes nomes "DriveUp" e "DriveUped" para a pasta antes do upload e depois, respectivamente.
4. O navegador usado pode ser trocado no código. Por padrão vem configurado como o Chrome.
5. **Importânte**: Em determinado ponto do script o mouse é utilizado. Para que isso ocorra ele usa das coordenadas do mouse na tela. Essas coordenadas variam em função do tamanho e resolução do monitor, assim sendo necessário a troca caso seu monitor não seja 1920 x 1080. Dentro do código está marcado onde deverá ser mudado e como fazer isso.

### Extra:
Muitas funcionalidades podem e devem ser adicionadas para melhorar a utilização desse script. Portanto, se tiver alguma ideia e queira contribuir, fique a vontedade!