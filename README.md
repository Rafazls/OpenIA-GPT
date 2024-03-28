
## Configurando o Ambiente Virtual (venv)

1. Abra um terminal ou prompt de comando.

2. Navegue até o diretório raiz do projeto.

3. Execute o seguinte comando para criar um novo ambiente virtual (substitua `nome_venv` pelo nome que deseja para o seu ambiente virtual):

    ```bash
   $ python -m venv nome_venv
    ```

4. Após a execução do comando acima, um diretório com o nome especificado será criado no diretório raiz do projeto, contendo o ambiente virtual.

## Inicializando o Ambiente Virtual

Antes de executar o projeto ou instalar os pacotes necessários, é necessário ativar o ambiente virtual. Siga as instruções correspondentes ao seu sistema operacional:

### Windows

No prompt de comando, execute:

```bash
$ nome_venv\Scripts\activate
```

### Linux/macOS
No terminal, execute:
```bash
$ nome_venv/bin/activate
```
## Instalando Pacotes
```bash
$ pip install -r requirements.txt
```

## Desativando o Ambiente Virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual. Basta executar o seguinte comando no terminal ou prompt de comando:
```bash
$ deactivate
```