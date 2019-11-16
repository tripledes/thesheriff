class UnirseABanda:
    def __init__(self, bandido_repository, banda_repository):
        self.bandido_repository = bandido_repository
        self.banda_repository = banda_repository

    def execute(self, id_banda, id_bandido):
        banda = self.banda_repository.of_id(id_banda)
        bandido = self.bandido_repository.of_id(id_bandido)
        bandido.unirse_a_banda(banda)
        self.bandido_repository.update(bandido)
