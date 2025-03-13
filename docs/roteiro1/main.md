## Objetivo

- Entender os conceitos básicos sobre uma plataforma de gerenciamento de hardware.
- Introduzir conceitos básicos sobre redes de computadores.


## Tarefa 1

### Banco de dados funcionando e seu Status está como "Ativo" para o Sistema Operacional
![Database ativo](./database_ativo.jpeg)


### Banco de dados acessivel na máquina na qual ele foi implantado.
![Database ativo](./aces_propria_maq.jpeg)

### Banco de dados acessivel a partir de uma conexão vinda da máquina MAIN.
![Database ativo](./aces_conexao_main.jpeg)

### Porta em que este serviço está funcionando.
![Database ativo](./porta_servico.jpeg)


 --- tarefa 1 100% completa e registrada no relatório (daqui pra cima ta feito)

Conforme ilustrado acima, a tela inicial do MAAS apresenta um dashboard com informações sobre o estado atual dos servidores gerenciados. O dashboard é composto por diversos painéis, cada um exibindo informações sobre um aspecto específico do ambiente gerenciado. Os painéis podem ser configurados e personalizados de acordo com as necessidades do usuário.

### Tarefa 2

## App



### Tarefa 1

### Tarefa 2

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
