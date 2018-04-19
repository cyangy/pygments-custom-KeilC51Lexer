#from pygments.lexers.asm import CppLexer
from pygments.lexers.compiled import CLexer
from pygments.token import Name, Keyword

class C51Lexer(CLexer):
    name = 'C51'
    aliases = ['c51']

    EXTRA_KEYWORDS = ['_at_']
    EXTRA_TYPE = ['sbit', 'idata', 'xdata','code','bit','sfr']
    def get_tokens_unprocessed(self, text):
        for index, token, value in CLexer.get_tokens_unprocessed(self, text):
            if token is Name and value in self.EXTRA_TYPE:
                yield index, Keyword.Type, value
            elif token is Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword, value
            else:
                yield index, token, value