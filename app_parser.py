import nltk

def parse(sentence_tokens_pos): #creating tree
      grammar= "NP:{<DT>?<JJ>*<NN>}" #extract all tags exactly
      Reg_parser= nltk.RegexpParser(grammar)
      for sentence in sentence_tokens_pos:
        Reg_parser.parse(sentence)
        Output= Reg_parser.parse(sentence)
        print("/n")
        print(Output)
        Output.draw()
   