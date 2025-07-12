# Guia de Desenvolvimento para o Projeto `fast_zero`

Este guia oferece uma série de comandos essenciais para desenvolver, testar e manter seu projeto FastAPI, utilizando Poetry para gerenciamento de dependências, Ruff para linting e formatação, e Pytest para testes.

---

## 1. Configuração Inicial do Projeto

Se você está começando este projeto do zero ou o clonou de um repositório, siga estes passos para configurá-lo:

1.  **Crie o Projeto (se necessário):**
    ```bash
    poetry new --flat fast_zero
    cd fast_zero
    ```
    *Isso gera a estrutura básica do projeto.*

2.  **Ajuste a Versão do Python:**
    Edite o arquivo `pyproject.toml`. Na seção `[project]`, localize e/ou adicione a linha `requires-python` para especificar a compatibilidade com o Python 3.11 (e futuras versões 3.x):
    ```toml
    # pyproject.toml
    [project]
    # ...
    requires-python = ">=3.11,<4.0"
    # ...
    ```
    *Este ajuste é crucial para evitar conflitos de dependências, como o que ocorreu com `taskipy`.*

3.  **Instale as Dependências de Produção (FastAPI):**
    ```bash
    poetry add "fastapi[standard] (>=0.116.0,<0.117.0)"
    ```
    *Isso adiciona o FastAPI e suas dependências essenciais para a execução da sua aplicação.*

4.  **Instale as Dependências de Desenvolvimento:**
    ```bash
    poetry add --group dev pytest pytest-cov taskipy ruff
    ```
    *Estas são ferramentas importantes para testes, linting (análise de código) e formatação, úteis durante o desenvolvimento.*

5.  **Configure as Ferramentas no `pyproject.toml`:**
    Garanta que as seções `[tool.ruff]`, `[tool.ruff.lint]`, `[tool.pytest.ini_options]` e `[tool.taskipy.tasks]` estejam configuradas conforme o exemplo fornecido anteriormente. Isso personaliza o comportamento do linter, testes e das tarefas personalizadas.

---

## 2. Rodando a Aplicação (Desenvolvimento)

Para iniciar sua aplicação FastAPI e vê-la em ação:

* **Inicie o Servidor de Desenvolvimento:**
    ```bash
    poetry run task run
    ```
    *Este comando, configurado via `taskipy`, executa `fastapi dev fast_zero/app.py`. O servidor Uvicorn iniciará, monitorando suas alterações de código e recarregando automaticamente. A URL de acesso será exibida no terminal (geralmente `http://127.0.0.1:8000`).*
    ```bash
    uvicorn fast_zero.app:app --port 8000 --reload
    ```
    *Faz a mesma coisa que "run = 'fastapi dev fast_zero/app.py' "*
    
* **Para parar o servidor:** Pressione `Ctrl + C` no terminal onde o servidor está rodando.

---

## 3. Mantendo a Qualidade do Código

É fundamental manter seu código limpo, padronizado e sem erros de estilo. Utilizamos o Ruff para isso.

* **Verifique o Código (Linting):**
    ```bash
    poetry run task lint
    ```
    *Executa `ruff check`, que analisa seu código em busca de erros de estilo, bugs comuns e inconsistências. Ele apenas lista os problemas encontrados, sem corrigi-los.*

* **Corrija Automaticamente (Pré-Formatação):**
    ```bash
    poetry run task pre_format
    ```
    *Executa `ruff check --fix`. Este comando tenta corrigir automaticamente a maioria dos problemas de estilo e formatação que o Ruff pode resolver (como espaços extras, ordenação de imports, etc.).*

* **Formate o Código Completamente:**
    ```bash
    poetry run task format
    ```
    *Executa `ruff format`. Este comando aplica um conjunto mais robusto de regras de formatação para padronizar todo o seu código. É uma ótima prática rodá-lo regularmente para manter a consistência.*

---

## 4. Executando os Testes

Para garantir que sua aplicação funciona como esperado e que novas alterações não introduziram bugs:

* **Execute Todos os Testes:**
    ```bash
    poetry run task test
    ```
    *Este é o comando principal para seus testes. Ele primeiro executa o `lint` (graças à configuração `pre_test` no `pyproject.toml`) para garantir que o código esteja limpo, e só então roda o `pytest` com as opções de cobertura de código. A saída indicará se os testes passaram, falharam e qual a porcentagem de cobertura do código.*

---

## 5. Gerenciamento de Dependências

O Poetry facilita a adição e remoção de bibliotecas do seu projeto.

* **Adicionar uma Nova Dependência de Produção:**
    ```bash
    poetry add nome-da-biblioteca
    # Exemplo: poetry add requests
    ```

* **Adicionar uma Nova Dependência de Desenvolvimento:**
    ```bash
    poetry add --group dev nome-da-biblioteca
    # Exemplo: poetry add --group dev ipython
    ```

* **Remover uma Dependência:**
    ```bash
    poetry remove nome-da-biblioteca
    ```

* **Instalar Dependências de um Projeto (se você clonou):**
    ```bash
    poetry install
    ```
    *Este comando lê os arquivos `pyproject.toml` e `poetry.lock` e instala todas as dependências necessárias para o projeto, garantindo que você tenha o ambiente correto.*

---

Este guia cobre os comandos mais frequentes e essenciais para o seu desenvolvimento. Mantenha-o como referência para um fluxo de trabalho eficiente!# APIs
