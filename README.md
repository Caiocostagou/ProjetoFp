🏋‍♂ WOD Tracker - Sistema de Gerenciamento de Treinos de CrossFit
Este é um sistema em Python para gerenciar treinos de CrossFit, registrar metas e receber sugestões de exercícios aleatórios. Ele permite adicionar, visualizar, editar e excluir treinos nos formatos AMRAP, EMOM e For Time, além de manter um registro das metas e oferecer funcionalidades motivacionais.

📋 Funcionalidades
✅ CRUD de treinos (Create, Read, Update, Delete)

🏁 Suporte a diferentes tipos de treino:

AMRAP (As Many Reps As Possible)

EMOM (Every Minute on the Minute)

For Time

🎯 Gestão de metas: adicionar, visualizar, concluir e desconcluir metas.

🔄 Sugestões aleatórias de WODs baseadas nos treinos existentes.

🏃‍♂ Sorteio de cardio aleatório como motivação extra.

📅 Organização por data para facilitar a consulta dos treinos.

🗃 Estrutura dos Arquivos
AM.txt, EM.txt, FT.txt – armazenam os treinos dos respectivos formatos.

metas.txt – registra as metas do usuário, concluídas ou não.

Todos os arquivos são atualizados automaticamente pelo sistema.

🚀 Como Usar
Execute o código.

Informe a data atual no formato dd/mm/aaaa.

Escolha a ação desejada a partir do menu interativo:
Adicionar um treino (C)
Visualizar seus treinos atuais (R)
Editar seus treinos atuais (U)
Excluir algum de seus treinos (D)
Receber sugestão de WOD aleatório (S)
Adicionar, Visualizar ou Completar metas (M)
Cardio aleatório (A)
Sair (E)
🧠Lógica de Funcionamento
O programa armazena treinos em arquivos .txt com base na data inserida.

Ao visualizar treinos, é possível buscar por data específica ou ver todos.

Metas são armazenadas com um identificador numérico e podem ser concluídas/desconcluídas.

A função CRUD() serve como central para todas as operações do sistema.

⚠️ Requisitos
Python 3.x

Nenhuma biblioteca externa é necessária (usa apenas bibliotecas nativas).

📌 Observações
O sistema cria os arquivos necessários na primeira execução.

Treinos e metas são persistentes e salvos localmente.

Há validação de data e tratamento básico de erros de entrada.

👤 Autores:
.Nomes:Arthur Andrade,Caio Costa,Gabiel Ricardo,Vinicius Tenorio, Telmo Calheiros
.Propósito: Projeto pessoal para organizar e acompanhar treinos de CrossFit
