## Objetivo

- Entender os conceitos básicos sobre uma plataforma de gerenciamento de hardware.
- Introduzir conceitos básicos sobre redes de computadores.


## Tarefa 1

### Banco de dados funcionando e seu Status está como "Ativo" para o Sistema Operacional
![Database ativo](./img/database_ativo.jpeg)


### Banco de dados acessivel na máquina na qual ele foi implantado.
![Database ativo](./img/aces_propria_maq.jpeg)

### Banco de dados acessivel a partir de uma conexão vinda da máquina MAIN.
![Database ativo](./img/aces_conexao_main.jpeg)

### Porta em que este serviço está funcionando.
![Database ativo](./img/porta_servico.jpeg)


 --- tarefa 1 100% completa e registrada no relatório (daqui pra cima ta feito)

Conforme ilustrado acima, a tela inicial do MAAS apresenta um dashboard com informações sobre o estado atual dos servidores gerenciados. O dashboard é composto por diversos painéis, cada um exibindo informações sobre um aspecto específico do ambiente gerenciado. Os painéis podem ser configurados e personalizados de acordo com as necessidades do usuário.

### Tarefa 2

### Dashboard cdo **MAAS** com as máquinas
![Database ativo](./img/dashboard_maas.png)

### Imagens sincro
![Database ativo](./img/imagens_sincro.png)

### Testes de hardware e commissioning com Status "OK"
#### Server 1
![Database ativo](./img/teste_server1.png)
#### Server 2
![Database ativo](./img/teste_server2.png)
#### Server 3
![Database ativo](./img/teste_server3.png)
#### Server 4
![Database ativo](./img/teste_server4.png)
#### Server 5
![Database ativo](./img/teste_server5.png)


### Tarefa 3
 
### Dashboard do MAAS com as 2 Maquinas e seus respectivos IPs
![Database ativo](./img/dashboard_maas_2maq.png)
Server1 ip:172.16.15.0 \
Server2 ip:172.16.0.130

### Aplicação Django conectada ao servidor
![Database ativo](./img/django_conectado.jpeg)

### Implementação manual da aplicação Django e banco de dados:
Aqui vai a explicação



Exemplo de diagrama

```mermaid
architecture-beta
    group api(cloud)[API]

    service db(database)[Database] in api
    service disk1(disk)[Storage] in api
    service disk2(disk)[Storage] in api
    service server(server)[Server] in api

    db:L -- R:server
    disk1:T -- B:server
    disk2:T -- B:db
```

[Mermaid](https://mermaid.js.org/syntax/architecture.html){:target="_blank"}

## Questionário, Projeto ou Plano

Esse seção deve ser preenchida apenas se houver demanda do roteiro.

## Discussões

Quais as dificuldades encontradas? O que foi mais fácil? O que foi mais difícil?

## Conclusão

O que foi possível concluir com a realização do roteiro?
