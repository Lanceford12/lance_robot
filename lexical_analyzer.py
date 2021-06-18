import parser
import re
import nltk
from nltk import tokenize
import app_parser as app_parser

class lexical_analyzer:

    def lexical_analysis(String):
        tokens=  lexical_analyzer.tokenize(String) #Split the token
        lexical_analyzer.pos_tagger(tokens) #assign part of speech
        lexical_analyzer.normalize(tokens) #normalize to lower case
        tokenize_sentence= lexical_analyzer.tokenize_by_sentence(String) #tokenize by sentence
        pos_tagged_sentences=lexical_analyzer.pos_tag_sentences(tokenize_sentence) #match the tokens to the part of speech


        app_parser.parse(pos_tagged_sentences) #calling the parser
       

    def tokenize(String): # declaring the tokenize function
        
        pattern = re.compile(r"([-\s.,;@!?])+") #rules that will defined the grammar
        tokens=pattern.split(String) #this will split the token

        new_tokens =[token for token in tokens if token and token not in '- \t\n.,:!@?'] #this for loop remove spaces
        print("tokens",tokens) #tokenized sentences
        print("tokenized sentences", new_tokens) #removed the spaces
        return new_tokens

    def tokenize_by_sentence(String):
        tokenized_sentence= nltk.sent_tokenize(String) #tokenixe the sentences using nltk
        print("tokenized by sentences", tokenized_sentence) #print out
        return tokenized_sentence
       
    def pos_tagger(tokens): # part of speech tag
        pos_tagged_tokens = nltk.pos_tag(tokens)
        print("match it to the part of speech", pos_tagged_tokens)
        return pos_tagged_tokens

    def normalize(tokens):
        normalized_tokens=[]
        for token in tokens:
            normalized_token= token.lower()
            normalized_tokens.append(normalized_token)

        print("normalized:", normalized_tokens)
        
    def pos_tag_sentences(sentences):
        pos_tagged_sentences=[]

        for sentence in sentences:
            pos_tagged_sentence=lexical_analyzer.pos_tagger(lexical_analyzer.tokenize(sentence))
            pos_tagged_sentences.append(pos_tagged_sentence)
            print("Pos Tagged Tokenized sentences:", pos_tagged_sentences)
            return pos_tagged_sentences

test_string= "This is some test string. vendetta seh love"

lexical_analyzer.lexical_analysis(test_string)
       

