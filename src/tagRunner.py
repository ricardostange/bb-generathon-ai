from usuario import User
from tags import TagMap
import re

class TagRunner:

    def __init__(self, user):
        self.user = user
        self.tagMap = TagMap(self.user)

    def mensagemNaoReconhecida(self, message):
        return  (False, message)

    
    def processMessage(self, message):
        arguments = self.getArguments(message)
        print(arguments)
        for tag in self.tagMap.tags:
            if tag in message:
                return self.tagMap.tags[tag](arguments[1:])
        return self.mensagemNaoReconhecida(message)
    
    def getArguments(self, message):
        pattern = r'<(.*?)>'  # Non-greedy match inside angle brackets
        matches = re.findall(pattern, message)
        return matches


if __name__ == "__main__":
    tagRunner = TagRunner(User("João", "123456", 1000, 5000))
    print(tagRunner.processMessage("Olá, gostaria de imprimir meu saldo <imprimir saldo> <teste> <haha>"))