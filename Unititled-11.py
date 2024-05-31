class Material:
    def __init__(self, titulo, autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self):
        print("Título:", self.titulo)
        print("Autor/Editora:", self.autor_ou_editora)


class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Gênero:", self.genero)


class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Edição:", self.edicao)


# Exemplo de utilização
livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia")
revista = Revista("National Geographic", "Editora Abril", "Janeiro 2024")

print("Detalhes do Livro:")
livro.exibir_informacoes()
print("\nDetalhes da Revista:")
revista.exibir_informacoes()        