<h1>Tutorial de invasão à redes Wi-Fi WPA2</h1>

<p>
<strong>Constituição Federal de 1988</strong> <br /> 
Nós, representantes do povo brasileiro, reunidos em Assembléia Nacional Constituinte para instituir um
Estado Democrático,<br /> destinado a assegurar o exercício dos direitos sociais e individuais, a liberdade,
a segurança, o bem-estar, o desenvolvimento, a igualdade e a justiça como valores supremos de uma sociedade
fraterna, pluralista e sem preconceitos, fundada na harmonia social e comprometida, na ordem interna e
internacional, com a solução pacífica das controvérsias, promulgamos, sob a proteção de Deus, a seguinte
<strong>CONSTITUIÇÃO DA REPÚBLICA FEDERATIVA DO BRASIL.<br /> Art. 5º</strong> Todos são iguais perante a lei,
sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes no País a
inviolabilidade do direito à vida, à liberdade, à igualdade, à segurança e à propriedade, nos termos 
seguintes: <strong>X - são invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas, assegurado o
direito a indenização pelo dano material ou moral decorrente de sua violação;</strong>
</p>

<h1>Pré-requisitos</h1>
Kali Linux<br />
Adaptador Wi-Fi USB (caso o Kali seja instalado em uma máquina virtual, pois não há como usar a própria placa de rede sem para realizar as invasões)


Fundamentação Teórica:
Kali Linux:
O Kali Linux é um sistema operacional Linux baseado no Debian, que é desenvolvido pela pequena e consagrada equipe da Offensive Security. Ele contém mais de 300 ferramentas nativas para testes de invasão, penetração, força bruta, forense entre outras. Atualmente é um dos sistemas mais famosos no mundo na área de e segurança da informação. Muito utilizado por hackers, pentesters, analistas e auditores de segurança da informação.
O Kali Linux chegou para ficar no lugar do descontinuado BackTrack, sistema operacional Linux baseado no Ubuntu, lançado em 2006, com o mesmo objetivo de construção. Podemos considerar que o BackTrack apenas mudou de “nome” para Kali Linux, que é uma versão melhorada do antigo sistema favorito dos hackers e auditores de segurança.
Ele já vem pronto para o uso, com o Kali Linux é possível fazer Pentests (Teste de penetração), SQL Inject, Exploits, Sniffers, Scanner, Cracking e Ataques. Bem como invasão de redes sem fio, sites e banco de dados. Quebra de senhas e muito mais!
– Mais de 300 ferramentas nativas para teste de invasão e auditoria de segurança;
– Você pode instalar ele como OS principal, rodar direto de um pendrive ou instalar em uma máquina virtual;
– É gratuito e sempre será;
– Confiável, pois ele é desenvolvido por um pequeno grupo de pessoas;
– É Linux, baseado no Debian, com alta estabilidade;
– Repositórios Git livre;
– Tem suporte a inúmeros dispositivos wireless;
– Totalmente personalizável;
– Arquiteturas x32 e x64.

Lammers:
Lammer ou Lamer é um termo utilizado para as pessoas que não possuem nenhum ou pouco conhecimento sobre hack e utilizam ferramentas desenvolvidas por outros para realizarem seus ataques. Conhecido atualmente também por "Script Kiddie", Lammer foi um termo depreciativo utilizado com maior frequência no final da década de 80 e durante os anos 90, atribuído àqueles que realizam ações na área da segurança da informação, mas não possuem conhecimento hábil e necessário para desenvolverem suas próprias ferramentas e executarem trabalhos profissionais.
Ao contrário de hackers, os ataques de lammers quase sempre são amadores, justamente pelo baixo conhecimento que possuem sobre programação e tecnologia. Alguns desses são apenas curiosos aventureiros da internet e do mundo virtual, procurando por diversão, ou novas maneiras de se satisfazerem na internet.
WPA HANDSHAKE:
O que você precisa é de você, o invasor, um cliente que se conectará à rede sem fio e o ponto de acesso sem fio. O que acontece é quando o cliente e o ponto de acesso se comunicam para autenticar o cliente, eles têm um handshake de 4 vias que podemos capturar. Este handshake tem o hash da senha. Agora não há nenhuma maneira direta de obter a senha do hash e, portanto, hashing é um método de proteção robusto. Mas há uma coisa que podemos fazer. Podemos pegar todas as senhas possíveis que existem e convertê-las em hash. Então, combinaremos o hash que criamos com o que está lá no aperto de mão. Agora, se os hashes coincidirem, sabemos qual senha de texto simples deu origem ao hash, portanto, sabemos a senha. Se o processo parece muito demorado para você, então é porque é. O WPA hacking (e o hash cracking em geral) é um processo bastante intensivo em termos de recursos e tempo.

Comandos Utilizados:
airmon-ng check kill: Verifica quais processos precisam receberem o kill (matar) e dá um kill nos processos necessários.
iwconfig: O iwconfig é similar ao comando ifconfig, mas é usado para redes wifi. Com este comando pode-se verificar diversas características das redes wireless.
airmon-ng: Esta é a ferramenta para colocarmos nossa placa de rede wireless no estado monitor! Devemos fazer isso antes de começar a capturar pacotes da rede wireless. 
airomdump-ng: Sua principal finalidade é capturar e coletar ivs (Initialization Vectors) dos pacotes WEP.
aircrack-ng: A partir dos dados coletados pelo airodump-ng usaremos esta ferramenta para sabermos qual chave esse pacote WEP que capturamos está usando.
aireplay-ng: A função principal é gerar tráfego para uso posterior no aircrack-ng para quebrar chaves WEP e WPA-PSK. Esta ferramenta nos dá cinco maneiras diferentes de atacar. O programa aireplay-ng classifica da seguinte maneira:
- Desautenticação: Faz com que o usuário conectado ao AP (Access Point) desautentique e volte a conectar, fazendo assim que ele faça uma nova requisição ARP e enviar um novo handshake.
- Autenticação falsa: Este ataque funciona com êxito quando temos um cliente conectado ao AP, caso não tenha, faremos uma cliente para conectar a esse AP. Mas lembre-se, é melhor quando temos uma cliente conectado ao AP, pois assim geraremos tráfego ARP.
- Seleção interativa do pacote a enviar: Ele pode selecionar um pacote qualquer e enviá-lo.
- Reinjeção de requisição ARP: É o mais efetivo para gerar IVs. Este ataque requer um MAC de um cliente associado ou um MAC falso. Este ataque pode demorar bastante, até que apareça a requisição ARP, ele falhará rapidamente se não houver tráfego. 
- Ataque de KoreK chopchop: Este ataque é ótimo quando bem sucedido, pois ele desencripta um pacote WEP sem conhecer a sua chave e também pode usar uma WEP dinâmica.

Tutorial:

Preparativo:
Deve-se verificar o nome da sua interface Wi-FI:
Comando: iwconfig
#Colocar imagem do que aparece quando se dá o comando acima. 

Após verificar o nome da interface, deve-se verificar se o Kali está reconhecendo o driver da interface sem fio: 
comando: airmon-ng
#Colocar imagem do que aparece quando se dá o comando acima.

Após isso deve-se se tem algum processo que pode acabar atrapalhando o processo de captura de pacotes:
comando: airmon-ng check kill
#Colocar imagem do que aparece quando se dá o comando acima.

Hora de começar:

Vamos colocar nossa placa de rede em modo monitor!
comando: airmon-ng start wlan0
comando: iwconfig
#Colocar imagem do que aparece quando se dá o comando acima.

Quando a placa estiver pronta para monitorar, podemos ver quais são as redes disponíveis para nossos possíveis ataques.
comando: airodump-ng wlan0mon 
#Colocar imagem do que aparece quando se dá o comando acima.
É importante levar em conta o alcance da rede a ser invadida, pois caso esteja distante, o WPA HANDSHAKE não consiga ser capturado.

Após selecionar a rede alvo, utilizaremos algumas de suas informações. Você pode guardá-las em um bloco de notas. As informações são as seguintes:
BSSID: dizer o que é. 
CH: canal na qual a rede está ...OPERANDO…?
ESSID: nome que é visível na rede.

Agora que temos a rede alvo, iremos monitorá-la usando algumas das informações adquiridas que guardamos em um bloco de notas anteriormente.
comando: airodump-ng -c <canal_da_rede_alvo> --bssid [bssid_da_rede_alvo] -w dados
#Colocar imagem do que aparece quando se dá o comando acima. E explicar os parâmetros
É importante que pelo menos 300 pacotes de dados tenham passado pela rede para garantir que o WPA HANDSHAKE seja capturado.

Hora de capturar o tão esperado WPA HANDSHAKE:
Para que seja capturado, é preciso que alguém se conecte à rede. Há duas opções: ou você espera a oportunidade que algum usuário se conecte ou você pode desautenticar quem já está conectado e capturar o WPA HANDSHAKE logo que o usuário se reconectar. Usaremos a segunda opção!
comando: aireplay-ng -0 10 -a <BSSID> wlanmon
#Mostrar a imagem
verificar o WPA HANDSHAKE capturado no arquivo criado anteriormente na execução do comando de captura. No caso deste tutorial, o arquivo criado recebeu o nome “dados”. Dê o seguinte comando no seu diretório atual:
comando: ls
comando: aircrack-ng dados-01.cap
#IMAGEM DO QUE APARECERÁ COM O COMANDO.

Hora de quebrar no Brute Force:
comando: crunch 10 10 <padrão> ...






Referências:
https://www.jusbrasil.com.br/topicos/10730704/inciso-x-do-artigo-5-da-constituicao-federal-de-1988
https://imasters.com.br/artigo/6572/gerencia-de-ti/acesso-nao-autorizado-a-redes-sem-fio-e-a-legislacao-brasileira/?trace=1519021197&source=single
https://hackersec.com/invadindo-wifi-kali-linux/
https://www.youtube.com/watch?v=8mZYeAStFv4
https://tecnicasdeinvasao.com/linux/kali-linux/voce-sabe-o-que-e-o-kali-linux/
https://canaltech.com.br/hacker/o-que-e-um-lammer/
http://www.kalitutorials.net/2014/06/hack-wpa-2-psk-capturing-handshake.html
https://www.vivaolinux.com.br/topico/Linux-Basico/Aircrack-ng-MODO-MONITORAMENTO-DESLIGA-O-WIFI-1
https://www.vivaolinux.com.br/artigo/Comandos-para-redes-wifi
https://www.vivaolinux.com.br/artigo/Aircrackng-e-sua-familia-para-quebrar-WEP-e-WPA1?pagina=1


