resposta = -1
while resposta != 0:
    print("------------------------------")
    print("|        PIM I - UNIP        |")
    print("------------------------------")
    print("1. Infraestrutura Computacional")
    print("2. T.I e Comunicações")
    print("3. Lógica Computacional com Python")
    print("4. Matemática e Estatística")
    print("0. Encerrar")

    resposta = int(input(">>>Digite sua opção: "))

    if resposta == 1:
        print("-------------------------------------------------------------")
        print(" Você está dentro da materia de Infraestrutura Computacional")
        print("-------------------------------------------------------------")
        print("Em qual assunto você quer entrar?")
        print("1. Hardware, Software, Firmware")
        print("2. Sistemas Operacionais")

        resinfra = int(input(">>>Digite sua opção: "))

        if resinfra == 1:
            print("------------------------------------------------------------------------")
            print(" Você está em Infraestrutura Computacional/Hardware, Software, Firmware")
            print("------------------------------------------------------------------------")
            print("Resumo e Exemplificação sobre Hardware, Software e Firmware:\n")
            print("1.Hardware\n\nDefinição: São os componentes físicos e tangíveis de um computador ou dispositivo eletrônico.\n\nExemplos:\n\nProcessador (CPU): Cérebro do computador (Ex: Intel Core i7, Ryzen 5).\nMemória RAM: Armazena dados temporários (Ex: DDR4 8GB).\nDisco Rígido (HDD/SSD): Armazenamento permanente (Ex: SSD 500GB).\nPlaca de Vídeo (GPU): Processamento gráfico (Ex: NVIDIA RTX 3060).\nTeclado, Mouse, Monitor: Periféricos de entrada/saída.\n\n-------------------------------------------------------------------------------------------\n\n2.Software\n\nDefinição: São programas, instruções e dados que fazem o hardware funcionar. Intangível (códigos).\n\nExemplos:\n\nSistema Operacional (SO): Windows, Linux, macOS.\nAplicativos: Navegadores (Chrome), editores de texto (Word), jogos (Fortnite).\nDrivers: Software que permite o hardware funcionar (Ex: driver da placa de vídeo).\nUtilitários: Antivírus (Avast), compactadores (WinRAR).\n\n-------------------------------------------------------------------------------------------\n\n3.Firmware\n\nDefinição: Software embutido no hardware, controlando funções básicas do dispositivo. Fica entre hardware e software.\n\nExemplos:\n\nBIOS/UEFI: Firmware da placa-mãe (inicializa o PC).\nFirmware de roteador: Controla conexões de rede (Ex: OpenWRT).\nFirmware de smartphone: Atualizações do sistema em chips internos.\nFirmware de smartwatch: Controla sensores e funções básicas.\n\n-------------------------------------------------------------------------------------------\n\nDiferença Chave:\n\nHardware: Peça física.\nSoftware: Programa instalável (pode ser alterado pelo usuário).\nFirmware: Código embutido no hardware (atualizado raramente).\n\n-------------------------------------------------------------------------------------------")
            resposta = int(input("Deseja sair? 1-Continuar / 0-Sair:"))
        else:
            print("------------------------------------------------------------------------")
            print(" Você está em Infraestrutura Computacional/Sistemas Operacionais")
            print("------------------------------------------------------------------------")
            print("Resumo e Exemplificação sobre Sistemas Operacionais")
            print("\nSistemas Operacionais:\n\nDefinição: Um Sistema Operacional (SO) é um software que gerencia os recursos de um computador, atuando como intermediário entre o hardware e os aplicativos.\nEle controla processos,\nmemória, armazenamento, dispositivos de entrada/saída e fornece uma interface para o usuário (gráfica ou textual).\n\nPrincipais Funções de um SO:\n\nGerenciamento de Processos - Controla a execução de programas, alocando tempo de CPU.\nExemplo: O Windows usa o Task Manager para encerrar processos travados.\n\nGerenciamento de Memória – Aloca espaço na RAM para programas em execução.\nExemplo: O Linux usa swap para liberar memória RAM quando necessário.\n\nControle de Arquivos – Organiza dados em discos (pastas, permissões).\nExemplo: O macOS usa o APFS (Apple File System) para armazenamento rápido.\n\nGerenciamento de Dispositivos – Comunica-se com hardware via drivers.\nExemplo: Plugar um pendrive no Ubuntu faz o SO detectá-lo automaticamente.\n\nInterface do Usuário – Pode ser gráfica (GUI) ou textual (CLI).\nExemplo: Windows (GUI) vs. Terminal do Linux (CLI).\n\nExemplos de Sistemas Operacionais:\n\n1. Windows (Microsoft)\nTipo: Proprietário, para desktops/servidores.\nVersões: Windows 10, 11, Server.\nCaracterísticas: Interface gráfica intuitiva, amplo suporte a softwares.\n\n2. macOS (Apple)\nTipo: Proprietário, exclusivo para Macs.\nVersões: macOS Sonoma, Ventura.\nCaracterísticas: Integração com dispositivos Apple, desempenho otimizado.\n\n3. Linux (Open Source)\nTipo: Livre, com várias distribuições (distros).\nExemplos: Ubuntu (fácil para iniciantes), Fedora (atualizado), Debian (estável).\nCaracterísticas: Seguro, personalizável, usado em servidores e IoT.\n\n4. Android (Google)\nTipo: Baseado em Linux, para dispositivos móveis.\nCaracterísticas: Aberto para fabricantes, com loja de apps (Play Store).\n\n5. iOS (Apple)\nTipo: Proprietário, para iPhones/iPads.\nCaracterísticas: Sistema fechado, otimizado para hardware Apple.\n\nSistemas operacionais são essenciais para o funcionamento de dispositivos, variando conforme o uso (desktop, móvel, servidor). Enquanto Windows e macOS dominam no mercado de PCs,\nLinux é preferido em servidores, e Android/iOS lideram nos smartphones.")
            print("--------------------------------------------------------------------------------------------------------")
            resposta = int(input("Deseja sair? 1-Continuar / 0-Sair:"))
        #Sistemas Operacionais, Hardware, Firmware, Software
    elif resposta == 2:
        print("----------------------------------------------------")
        print(" Você está dentro da materia de T.I e Comunicações")
        print("----------------------------------------------------")
        print("Em qual assunto você quer entrar?")
        print("1. Banco de Dados")
        print("2. Redes de Computadores")

        resti = int(input(">>>Digite sua opção: "))

        if resti == 1:
            print("-------------------------------------------------")
            print(" Você está em T.I e Comunicações/Banco e Dados")
            print("-------------------------------------------------")
            print("Resumo e Exemplificação sobre Banco de Dados:\n")
            print("Banco de Dados:\n\nDefinição de Banco de Dados: Sistema organizado para armazenar, recuperar, inserir e atualizar dados.\n\nTipos principais:\nBancos relacionais (RDB): MySQL, PostgreSQL, Oracle.\nNoSQL: MongoDB, Cassandra, Redis.\nEspecializados: Grafos, chave-valor, documentos, colunas.")
            print("--------------------------------------------------------------------------------------------------------")
            print("Bancos de Dados Relacionais (RDB)\n\nCaracterísticas:\nDados organizados em tabelas (linhas = entidades; colunas = atributos).\nEstrutura rígida: Definida por um esquema com restrições (chaves primárias, estrangeiras).\nLinguagem SQL: Usada para consultas (SELECT, INSERT, UPDATE, DELETE) e operações complexas (junções, agregações).\nSistemas (RDBMS): MySQL, PostgreSQL, Oracle, SQL Server.\n\nVantagens do MySQL:\nFácil uso, boa performance, escalabilidade, multiplataforma.\n\nDesvantagens:\nRecursos avançados limitados; não ideal para cargas extremamente pesadas.")
            print("--------------------------------------------------------------------------------------------------------")
            print("Bancos NoSQL\n\nDiferenças em relação aos RDB:\nEsquema flexível: Dados não estruturados/semiestruturados (JSON, grafos, etc.).\nEscalabilidade horizontal: Distribuição fácil em múltiplos servidores.\n\nModelos específicos:\n-----------------------------------------------------------------\nTipo NoSQL	 Exemplos	       Uso Típico\n-----------------------------------------------------------------\nDocumentos    MongoDB, CouchDB	      Dados flexíveis (JSON)\n-----------------------------------------------------------------\nColunas	      Cassandra, HBase	      Análise de grandes volumes\n-----------------------------------------------------------------\nGrafos        Neo4j, Amazon Neptune   Relacionamentos complexos\n-----------------------------------------------------------------\nChave-valor   Redis, DynamoDB         Cache e alta velocidade\n-----------------------------------------------------------------\n\nVantagens do NoSQL:\nFlexibilidade, desempenho em grandes volumes, escalabilidade horizontal.\n\nDesvantagens:\nConsistência eventual (dados não atualizados imediatamente).\nMenor suporte a consultas complexas (ex.: junções).\nCurva de aprendizado para desenvolvedores SQL.\n\nComparativo: Relacional vs. NoSQL\n--------------------------------------------------------------------------\nCritério	 Relacional (RDB)	     NoSQL\n--------------------------------------------------------------------------\nEstrutura	 Tabelas rígidas	     Esquema flexível\n--------------------------------------------------------------------------\nEscalabilidade	 Vertical (mais hardware)    Horizontal (mais servidores)\n--------------------------------------------------------------------------\nConsistência	 Imediata	             Eventual\n--------------------------------------------------------------------------\nMelhor para      Transações complexas        Big Data, alta velocidade\n--------------------------------------------------------------------------\n\nConclusão\n\nEscolha depende do projeto:\nRDB: Ideal para dados estruturados e transações críticas (ex.: sistemas financeiros).\nNoSQL: Melhor para escalabilidade, flexibilidade e dados variados (ex.: redes sociais, IoT).")
            print("--------------------------------------------------------------------------------------------------------")
            resposta = int(input("Deseja sair? 1-Continuar / 0-Sair:"))
        else:
            print("---------------------------------------------------------")
            print(" Você está em T.I e Comunicações/Rede de Computadores")
            print("---------------------------------------------------------")
            print("Resumo e Exemplificação sobre Rede de Computadores:\n")
            print("Redes de Computadores\n\nDefinição: Interconexão de dispositivos (computadores, servidores, roteadores, etc.) para compartilhar recursos e trocar informações.\nExemplo: Acessar um vídeo no YouTube envolve comunicação entre seu dispositivo e um servidor remoto.\nImportância: Fundamental para o funcionamento de aplicativos, comunicação e acesso à internet.\n\nComponentes e Funcionamento\n\n1. Elementos Básicos\n\nNós (Dispositivos):\nDTE (Equipamentos Terminais): Computadores, impressoras, servidores (originam ou consomem dados).\nDCE (Equipamentos de Comunicação): Roteadores, switches, modems (gerenciam a comunicação).\n\nLinks (Conexões):\nFísicos: Cabos (par trançado, fibra óptica, coaxial).\nSem fio: Wi-Fi, Bluetooth (ondas de rádio).\n\n2. Principais Funções\n\nCompartilhamento de recursos (arquivos, impressoras).\nAcesso à internet e serviços online (redes sociais, streaming).\nComunicação (e-mail, VoIP, videoconferência).\nAcesso remoto a sistemas e dados.")
            print("--------------------------------------------------------------------------------------------------------")
            print("\nProtocolos de Rede\n\nConjunto de regras que padronizam a comunicação entre dispositivos.\n\nPrincipais Protocolos\n---------------------------------------------------------------------------------------------------------\nProtocolo	Função	                                        Exemplo de Uso\n---------------------------------------------------------------------------------------------------------\nTCP/IP	        Base da internet (envio confiável de dados).	Navegação, emails.\n---------------------------------------------------------------------------------------------------------\nHTTP/HTTPS      Transferência de dados na web.	                Acesso a sites seguros (HTTPS).\n---------------------------------------------------------------------------------------------------------\nFTP	        Transferência de arquivos.	                Upload de arquivos para servidor.\n---------------------------------------------------------------------------------------------------------\nDNS	        Traduz nomes (ex: google.com) em IPs.	        Acesso a websites.\n---------------------------------------------------------------------------------------------------------\nSMTP	        Envio de e-mails.	                        Configuração de servidores de email.\n---------------------------------------------------------------------------------------------------------\nUDP	        Transmissão rápida (sem confirmação).	        Streaming de vídeo (YouTube).\n---------------------------------------------------------------------------------------------------------\n")
            print("Padronização\nOrganizações como IETF definem padrões (RFCs).\nModelo OSI: Referência teórica com 7 camadas (não abordado em detalhes aqui).")
            print("--------------------------------------------------------------------------------------------")
            print("\nExemplo Prático\n\nCenário Doméstico:\nDispositivos: Notebook (DTE), roteador (DCE), cabo Ethernet (link físico).\nAplicação: Assistir Netflix (HTTP/TCP/IP via Wi-Fi).")
            print("--------------------------------------------------------------------------------------------")
            print("\nConclusão\n\nRedes de computadores são a espinha dorsal da comunicação digital, permitindo desde simples compartilhamentos de arquivos até operações globais (internet).\nA escolha de protocolos e infraestrutura (física/sem fio) depende das necessidades específicas (ex.: TCP para confiabilidade, UDP para velocidade).\n\nPalavras-chave: Comunicação, protocolos, TCP/IP, nós, links.")
            print("--------------------------------------------------------------------------------------------")

            resposta = int(input("Deseja sair? 1-Continuar / 0-Sair:"))
        #Sistemas de Informação
    elif resposta == 3:
        print("-----------------------------------------------------------------")
        print(" Você está dentro da materia de Lógica Computacional com Python")
        print("-----------------------------------------------------------------")
        print("Em qual assunto você quer entrar?")
        print("1. Funções, Variáveis, Condições, Repetições")
        
        respy = int(input(">>>Digite sua opção: "))

        if respy == 1:
            print("----------------------------------------------------------------------------------------")
            print(" Você está em Lógica Computacional com Python/Funções, Variáveis, Condições, Repetições")
            print("----------------------------------------------------------------------------------------")
            print("Resumo e Exemplificação sobre Funções, Variáveis, Condições e Funções")
            print("\n1. Variáveis\n\nVariáveis são espaços na memória usados para armazenar valores\nque podem ser utilizados e modificados durante a execução do programa.\n\nExemplos:\n\nname: Daniel (guarda uma string) - str\nage: 19 (guarda um número inteiro) - int\nheight: 1.82 (guarda um número decimal) - float\n\n-------------------------------------------------\n2.Condições (if, elif, else)\n\nServem para tomar decisões no código.O programa executa um bloco de código\nse uma condição for verdadeira.\n\nExemplo:\n\nidade = 17\nif idade >= 18:\n\tprint(Você é maior de idade.)\nelse:\n\tprint(Você é menor de idade.)\n--------------------------------------------------\n3. Repetições (loops)\n\nUsamos laços de repetição para executar algo várias vezes. Os principais são for e while.\n\nExemplos:\nfor – repete por um número definido de vezes.\nwhile – repete enquanto uma condição for verdadeira.\n-------------------------------------------------\nfor i in range(5):  # Vai de 0 a 4\n\tprint(Repetição, i)\n-------------------------------------------------\ncontador = 0\n\nwhile contador < 3:\n\tprint(Contando:, contador)\n-------------------------------------------------\n4. Funções\n\nFunções são blocos de código que podem ser reutilizados.\nElas ajudam a organizar e evitar repetição de código\n\nExemplo:\n\ndef saudacao(nome):\n\tprint(Olá, nome)\n\nsaudacao(Daniel)  # Chamada da função\n-------------------------------------------------\ndef soma(a, b):\n\treturn a + b\n\nresultado = soma(3, 4)\nprint(Resultado:, resultado)\n-------------------------------------------------\n")

        resposta = int(input("Deseja sair? 1-Continuar / 0-Sair:"))
        #Funções, Variaveis, Condições, Laços de Repetição
    elif resposta == 4:
        print("-----------------------------------------------------------")
        print(" Você está dentro da materia de Matemática e Estatística")
        print("-----------------------------------------------------------")
        print("Em qual assunto você quer entrar?")
        print("1. Razão e Proporção")
        print("2. Porcentagem")
        resmat = int(input(">>>Digite sua resposta: "))
        if resmat == 1:
            print("----------------------------------------------------------")
            print(" Você está em Matemática e Estatística/Razão e Proporção")
            print("----------------------------------------------------------")
            n1 = int(input('Digite o primeiro numerador: '))
            n2 = int(input("Digite o primeiro denominador: "))
            n3 = int(input("Digite o segundo numerador: "))
            n4 = int(input("Digite o segundo denominador: "))

            print("A razão entre", n1, "e", n2, "é:", n1/n2)
            if n1*n4==n3*n2:
                print("As razões", n1,"/",n2,"e",n3,"/",n4,"são proporcionais")
            else:
                print("As razões", n1,"/",n2,"e",n3,"/",n4,"não são proporcionais")
            resposta = int(input("Deseja sair? 1-Continuar 0-Sair: "))
        else:
            print("----------------------------------------------------------")
            print(" Você está em Matemática e Estatística/Porcentagem")
            print("----------------------------------------------------------")
            print("Calcule a porcentagem de um número")
            n1 = int(input('Digite o primeiro número:'))
            n2 = int(input("Digite o segundo número: "))

            print(n1,"% de", n2, "é:", n2*n1/100)
            resposta = int(input("Deseja sair? 1-Continuar 0-Sair: "))
        #Porcentagem, Razão e Proporção, 
print("Fim do Sistema")
