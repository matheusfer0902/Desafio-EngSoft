# Sistema de Controle de Biblioteca - Genius Lab

## Apresentação
 
Olá! Eu sou Matheus Ferreira, estudante de Engenharia da Computação, e este é um projeto desenvolvido como parte do processo seletivo da engeselt software. Abaixo, você encontrará informações detalhadas sobre a aplicação, suas funcionalidades, e o objetivo da mesma.

---

## Descrição do Projeto

O Sistema de Controle de Biblioteca para a Genius Lab é uma aplicação que traz inovação e eficiência para o gerenciamento de bibliotecas educacionais. Com uma interface intuitiva e diversas funcionalidades, a plataforma simplifica processos comuns em bibliotecas, como o cadastro de livros, acompanhamento de empréstimos e controle do acervo.

A aplicação possui ferramentas específicas para administradores e usuários:
- **Administradores** podem adicionar novos livros.
- **Usuários** têm acesso facilitado às informações sobre os livros disponíveis e ao histórico de seus empréstimos.

Essa solução digital permite maior eficiência operacional, otimização de recursos e uma experiência mais organizada e prática para todos os envolvidos.

---

## Funcionalidades Principais

1. **Cadastro de Usuários** - Registro e gerenciamento de perfis.
2. **Cadastro e Gerenciamento de Livros** - Inclusão e atualização do acervo.
3. **Empréstimos** - Controle dos empréstimos com verificação de disponibilidade.
4. **Perfil do Usuário** - Área onde o usuário pode verificar seus dados e histórico de empréstimos.

---

## Demonstração do Projeto

### Screenshots

#### Tela Home

![tela home](https://github.com/user-attachments/assets/2cf070ac-d67e-4bed-b3b4-ab0f1801d636)

#### Detalhes do livro

![ver detalhes](https://github.com/user-attachments/assets/a35ea170-b0c3-40f2-8d89-18664d606020)

#### Login

![login](https://github.com/user-attachments/assets/b9163f12-752a-4a5a-9fd2-f9df016af1fc)

#### Cadastro de usuário

![cadastro usuario](https://github.com/user-attachments/assets/44e9d46c-6ee7-4ec4-9dc2-8e4c32f6ae3f)

#### Tela de emprestimo

![tela emprestimo](https://github.com/user-attachments/assets/1180e268-abb6-45a6-971d-18c23a8ceadb)

#### Meu perfil

![meu perfil](https://github.com/user-attachments/assets/7a8ea49f-bcb7-4efe-8344-8dee220cef8f)

#### Cadastro de livro (usuário ADM)

![cadastro livro](https://github.com/user-attachments/assets/18ffc45e-ed33-4cda-bde7-2df052b1fcb0)

#### Registrar no estoque(usuário ADM)

![registrar estoque](https://github.com/user-attachments/assets/0f6047eb-181c-46b5-8b34-82ba2b37979a)

---

## Pontos de melhora

1. O sistema de login do projeto não possui autenticação real, apenas segue um fluxo de usabilidade. Isso significa que, se qualquer usuário acessar uma URL existente na aplicação, ele conseguirá acessar a área correspondente.
2. A parte de empréstimo do projeto não é controlada por um usuário administrador (ADM). Assim, não há controle de status de empréstimo aberto ou fechado.
3. Não é possível apagar uma conta de usuário pela aplicação, apenas diretamente no banco de dados.
4. Não há valores associados na aplicação, então os empréstimos não têm custo

## Considerações Finais

Este projeto demonstra o uso prático de conceitos de desenvolvimento de software, incluindo manipulação de banco de dados, interfaces de usuário e estruturação de um sistema completo com diferentes níveis de permissão. 
