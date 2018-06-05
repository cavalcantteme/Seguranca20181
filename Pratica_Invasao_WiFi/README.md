<h1>Invadindo Redes Wi-Fi WPA2</h1>

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
<ul>
<li>Kali Linux</li>
<li>Adaptador Wi-Fi USB (Apenas em caso de máquina virtual)</li>
</ul>

<h1>Fundamentação Teórica</h1>
<strong>Kali Linux</strong><br />
<p>
O Kali Linux é um sistema operacional Linux baseado no Debian, que é desenvolvido pela pequena e consagrada equipe da Offensive Security. Ele contém mais de 300 ferramentas nativas para testes de invasão, penetração, força bruta, forense entre outras. Atualmente é um dos sistemas mais famosos no mundo na área de e segurança da informação. Muito utilizado por hackers, pentesters, analistas e auditores de segurança da informação.
O Kali Linux chegou para ficar no lugar do descontinuado BackTrack, sistema operacional Linux baseado no Ubuntu, lançado em 2006, com o mesmo objetivo de construção. Podemos considerar que o BackTrack apenas mudou de “nome” para Kali Linux, que é uma versão melhorada do antigo sistema favorito dos hackers e auditores de segurança.
Ele já vem pronto para o uso, com o Kali Linux é possível fazer Pentests (Teste de penetração), SQL Inject, Exploits, Sniffers, Scanner, Cracking e Ataques. Bem como invasão de redes sem fio, sites e banco de dados. Quebra de senhas e muito mais!
</p>
<ul>
<li>Mais de 300 ferramentas nativas para teste de invasão e auditoria de segurança;</li>
<li>Você pode instalar ele como OS principal, rodar direto de um pendrive ou instalar em uma máquina virtual;</li>
<li>É gratuito e sempre será;</li>
<li>Confiável, pois ele é desenvolvido por um pequeno grupo de pessoas;</li>
<li>É Linux, baseado no Debian, com alta estabilidade;</li>
<li>Repositórios Git livre;</li>
<li>Tem suporte a inúmeros dispositivos wireless;</li>
<li>Totalmente personalizável;</li>
<li>Arquiteturas x32 e x64.</li>
</ul>
<strong>Lammers</strong><br />
<p>
Lammer ou Lamer é um termo utilizado para as pessoas que não possuem nenhum ou pouco conhecimento sobre hack e utilizam ferramentas desenvolvidas por outros para realizarem seus ataques. Conhecido atualmente também por "Script Kiddie", Lammer foi um termo depreciativo utilizado com maior frequência no final da década de 80 e durante os anos 90, atribuído àqueles que realizam ações na área da segurança da informação, mas não possuem conhecimento hábil e necessário para desenvolverem suas próprias ferramentas e executarem trabalhos profissionais.
Ao contrário de hackers, os ataques de lammers quase sempre são amadores, justamente pelo baixo conhecimento que possuem sobre programação e tecnologia. Alguns desses são apenas curiosos aventureiros da internet e do mundo virtual, procurando por diversão, ou novas maneiras de se satisfazerem na internet.<br />
</p>
<strong>WPA2</stong><br />
<p>
O WPA2, criado em 2003, corresponde à versão final do 802.11i e foi lançado no ano seguinte. A tecnologia veio em substituição à WPA "Wi-fi Alliance", pois embora fosse bem segura em relação ao padrão anterior existente, o WEP, a "Wi-fi Alliance" precisou fazer um novo certificado para as redes sem fio, tornando-as mais confiáveis. O WPA2 é um protocolo de certificação que utiliza o AES (Advanced Encryption Standard), sistema de encriptação mais seguro e mais pesado do que o WPA original. O AES é um sistema de encriptografia bastante seguro, baseado na utilização das chaves com 128 a 256 bits. Até mesmo o governo dos Estados Unidos faz uso desse sistema que torna a tarefa de invasão dos sistemas, mesmo diante de uma falha no algoritmo, bem mais complicada.
</p>
<strong>WPA HANDSHAKE</strong><br />
<p>
O que você precisa é de você, o invasor, um cliente que se conectará à rede sem fio e o ponto de acesso sem fio. O que acontece é quando o cliente e o ponto de acesso se comunicam para autenticar o cliente, eles têm um handshake de 4 vias que podemos capturar. Este handshake tem o hash da senha. Agora não há nenhuma maneira direta de obter a senha do hash e, portanto, hashing é um método de proteção robusto. Mas há uma coisa que podemos fazer. Podemos pegar todas as senhas possíveis que existem e convertê-las em hash. Então, combinaremos o hash que criamos com o que está lá no aperto de mão. Agora, se os hashes coincidirem, sabemos qual senha de texto simples deu origem ao hash, portanto, sabemos a senha. Se o processo parece muito demorado para você, então é porque é. O WPA hacking (e o hash cracking em geral) é um processo bastante intensivo em termos de recursos e tempo.<br />
</p>
<h1>Ferramentas Utilizadas</h1>
<p>
<strong>AIRMON-NG CHECK KILL</strong><br />
Verifica quais processos precisam receberem o kill (matar) e dá um kill nos processos necessários.<br />
</p>
<p>
<strong>IWCONFIG</strong><br />
O iwconfig é similar ao comando ifconfig, mas é usado para redes wifi. Com este comando pode-se verificar diversas características das redes wireless.<br />
</p>
<p>
<strong>AIRMON-NG</strong><br />
Esta é a ferramenta para colocarmos nossa placa de rede wireless no estado monitor! Devemos fazer isso antes de começar a capturar pacotes da rede wireless. <br />
</p>
<p>
<strong>AIRODUMP-NG</strong><br />
Sua principal finalidade é capturar e coletar ivs (Initialization Vectors) dos pacotes WEP.<br />
</p>
<p>
<strong>AIRCRACK-NG</strong><br />
A partir dos dados coletados pelo airodump-ng usaremos esta ferramenta para sabermos qual chave esse pacote WEP que capturamos está usando.<br />
</p>
<p>
<strong>AIREPLAY-NG</strong><br />
A função principal é gerar tráfego para uso posterior no aircrack-ng para quebrar chaves WEP e WPA-PSK. Esta ferramenta nos dá cinco maneiras diferentes de atacar. O programa aireplay-ng classifica da seguinte maneira:<br />
</p>
<ul>
<li><strong>Desautenticação:</strong> Faz com que o usuário conectado ao AP (Access Point) desautentique e volte a conectar, fazendo assim que ele faça uma nova requisição ARP e enviar um novo handshake.</li>
<li><strong>Autenticação falsa:</strong> Este ataque funciona com êxito quando temos um cliente conectado ao AP, caso não tenha, faremos uma cliente para conectar a esse AP. Mas lembre-se, é melhor quando temos uma cliente conectado ao AP, pois assim geraremos tráfego ARP.</li>
<li><strong>Seleção interativa do pacote a enviar:</strong> Ele pode selecionar um pacote qualquer e enviá-lo.</li>
<li><strong>Reinjeção de requisição ARP:</strong> É o mais efetivo para gerar IVs. Este ataque requer um MAC de um cliente associado ou um MAC falso. Este ataque pode demorar bastante, até que apareça a requisição ARP, ele falhará rapidamente se não houver tráfego. </li>
<li><strong>Ataque de KoreK chopchop:</strong> Este ataque é ótimo quando bem sucedido, pois ele desencripta um pacote WEP sem conhecer a sua chave e também pode usar uma WEP dinâmica.</li>
</ul>

<h1>Pratica</h1>
<p>
Verificar o nome da sua interface Wi-FI:<br />
<p>
<pre><code>iwconfig
</code></pre>
</p>
<img src="https://github.com/cavalcantteme/Seguranca20181/blob/master/Pratica_Invasao_WiFi/iwconfig.png"/>
</p> 
<p>
Após verificar o nome da interface, deve-se verificar se o Kali está reconhecendo o driver da interface sem fio: 
<p>
<pre><code>airmon-ng
</code></pre>
</p>
<img src="https://github.com/cavalcantteme/Seguranca20181/blob/master/Pratica_Invasao_WiFi/airmon-ng.png"/>
</p>
<p>
Após isso deve-se verificar se tem algum processo que pode acabar atrapalhando o processo de captura de pacotes:
<p>
<pre><code>airmon-ng check kill
</code></pre>
</p>
<img src="https://github.com/cavalcantteme/Seguranca20181/blob/master/Pratica_Invasao_WiFi/airmon-ng_checkkill.png"/>
</p>
<p>
Vamos colocar nossa placa de rede em modo monitor:
<p>
<pre><code>airmon-ng start wlan0
iwconfig
</code></pre>
</p>
<img src="https://github.com/cavalcantteme/Seguranca20181/blob/master/Pratica_Invasao_WiFi/airmon-ng_startwlan.png"/>
</p>
<p>
Quando a placa estiver pronta para monitorar, podemos ver quais são as redes disponíveis para nossos possíveis ataques. É importante levar em conta o alcance da rede a ser invadida, pois caso esteja distante, o WPA HANDSHAKE não consiga ser capturado.
<p>
<pre><code>airodump-ng wlan0mon 
</code></pre>
</p>
<img src="https://github.com/cavalcantteme/Seguranca20181/blob/master/Pratica_Invasao_WiFi/airodump-ng_wlan0.png"/>
</p>
<p>
Após selecionar a rede alvo, utilizaremos algumas de suas informações. Você pode guardá-las em um bloco de notas. As informações são as seguintes:<br />
<strong>BSSID:</strong> <em>Basic Service Set Identifier</em> se refere ao endereço MAC de um adaptador sem fio ou de um ponto de acesso.Sua função é identificar exclusivamente um ponto de acesso que enviará sinais pra transmissão da rede sem fio.<br /> 
<strong>CH:</strong> Canal na qual a rede está operando.<br />
<strong>ESSID:</strong> nome que é visível na rede.<br />
</p>
<p>
Agora que temos a rede alvo, iremos monitorá-la usando algumas das informações adquiridas que guardamos em um bloco de notas anteriormente. É importante que pelo menos 300 pacotes de dados tenham passado pela rede para garantir que o WPA HANDSHAKE seja capturado.
<p>
<pre><code>airodump-ng -c <canal_da_rede_alvo> --bssid [bssid_da_rede_alvo] -w dados
</code></pre>
</p>
#Colocar imagem do que aparece quando se dá o comando acima. E explicar os parâmetros
</p>
<p>
Hora de capturar o tão esperado WPA HANDSHAKE. Para que seja capturado, é preciso que alguém se conecte à rede. Há duas opções: você espera a oportunidade que algum usuário se conecte ou você pode desautenticar quem já está conectado e capturar o WPA HANDSHAKE logo que o usuário se reconectar. Usaremos a segunda opção!
<p>
<pre><code>aireplay-ng -0 10 -a <BSSID> wlanmon
</code></pre>
</p>
#Mostrar a imagem
</p>
<p>
verificar o WPA HANDSHAKE capturado no arquivo criado anteriormente na execução do comando de captura. No caso deste tutorial, o arquivo criado recebeu o nome “dados”. Dê o seguinte comando no seu diretório atual:
</p>
<pre><code>ls
aircrack-ng dados-01.cap
</code></pre>
</p>
#IMAGEM DO QUE APARECERÁ COM O COMANDO.
</p>
<p>
Hora de quebrar no Brute Force:
<p>
<pre><code>crunch 10 10 <padrão> ...
</code></pre>
</p>
</p>

<h1>Referências</h1>

<a href="https://www.jusbrasil.com.br/topicos/10730704/inciso-x-do-artigo-5-da-constituicao-federal-de-1988">Jusbrasil</a><br />
<a href="https://hackersec.com/invadindo-wifi-kali-linux/">Invadir rede WiFi com Kali Linux</a><br />
<a href="https://www.youtube.com/watch?v=8mZYeAStFv4">Aircrack-ng + Crunch [Wifi Atack sem o uso de Wordlist]</a><br />
<a href="https://tecnicasdeinvasao.com/linux/kali-linux/voce-sabe-o-que-e-o-kali-linux/">Você sabe o que é o Kali Linux?</a><br />
<a href="https://canaltech.com.br/seguranca/O-que-e-WPA2/">O que é WPA2?></a><br />
<a href="https://canaltech.com.br/hacker/o-que-e-um-lammer/">O que é um Lammer?</a><br />
<a href="http://www.kalitutorials.net/2014/06/hack-wpa-2-psk-capturing-handshake.html">Hack WPA/WPA2 PSK Capturing the Handshake</a><br />
<a href="https://www.vivaolinux.com.br/topico/Linux-Basico/Aircrack-ng-MODO-MONITORAMENTO-DESLIGA-O-WIFI-1">AIRCRACK-NG</a><br />
<a href="https://www.vivaolinux.com.br/artigo/Comandos-para-redes-wifi">Comandos para redes wifi</a><br />
<a href="https://www.vivaolinux.com.br/artigo/Aircrackng-e-sua-familia-para-quebrar-WEP-e-WPA1?pagina=1">Aircrack-ng e sua família para quebrar WEP e WPA1</a><br />

<h1>Contributors</h1>
<a href="https://github.com/cavalcantteme/">Antonio Matheus Cavalcante da Silva</a><br />
<a href="https://github.com/calebetaap/">Calebe Tavares Arruda Alves Pinheiro</a><br />
