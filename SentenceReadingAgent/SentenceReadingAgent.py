# import spacy
import string
class SentenceReadingAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    # def preprocess(self):
    #     nlp = spacy.load('en_core_web_sm')
    #     word_data = []
    #     with open('mostcommon.txt', 'r') as file:
    #         for line in file:
    #             word_data.append(line.strip())
    #     words = " ".join(word_data)
    #     doc = nlp(words)
    #     dict = {}
    #     stop_word_cnt = []
    #     for token in doc:
    #         dict[token.text.lower()] = token.pos_
    #     # print(dict)


    def solve(self, sentence, question):
        # self.preprocess()
        word_dict = {'serena': 'PROPN', 'andrew': 'PROPN', 'bobbie': 'PROPN', 'cason': 'PROPN', 'david': 'PROPN', 'farzana': 'PROPN', 'frank': 'PROPN', 'hannah': 'PROPN', 'ida': 'PROPN', 'irene': 'PROPN', 'jim': 'PROPN', 'jose': 'PROPN', 'keith': 'PROPN', 'laura': 'PROPN', 'lucy': 'PROPN', 'meredith': 'PROPN', 'nick': 'PROPN', 'ada': 'PROPN', 'yeeling': 'PROPN', 'yan': 'PROPN', 'the': 'DET', 'of': 'NOUN', 'to': 'ADP', 'and': 'CCONJ', 'a': 'DET', 'in': 'NOUN', 'is': 'AUX', 'it': 'PRON', 'you': 'PRON', 'that': 'SCONJ', 'he': 'PRON', 'was': 'AUX', 'for': 'ADP', 'on': 'ADV', 'are': 'AUX', 'with': 'ADP', 'as': 'SCONJ', 'i': 'PRON', 'his': 'PRON', 'they': 'PRON', 'be': 'VERB', 'at': 'ADP', 'one': 'NUM', 'have': 'VERB', 'this': 'PRON', 'from': 'ADP', 'or': 'CCONJ', 'had': 'VERB', 'by': 'ADP', 'hot': 'ADJ', 'but': 'CCONJ', 'some': 'PRON', 'what': 'PRON', 'there': 'ADV', 'we': 'PRON', 'can': 'AUX', 'out': 'ADV', 'other': 'ADJ', 'were': 'AUX', 'all': 'PRON', 'your': 'PRON', 'when': 'SCONJ', 'up': 'ADP', 'use': 'VERB', 'word': 'NOUN', 'how': 'SCONJ', 'said': 'VERB', 'an': 'DET', 'each': 'PRON', 'she': 'PRON', 'which': 'PRON', 'do': 'AUX', 'their': 'PRON', 'time': 'NOUN', 'if': 'SCONJ', 'will': 'AUX', 'way': 'VERB', 'about': 'ADV', 'many': 'ADJ', 'then': 'ADV', 'them': 'PRON', 'would': 'AUX', 'write': 'VERB', 'wrote': 'VERB', 'like': 'INTJ', 'so': 'ADV', 'these': 'PRON', 'her': 'PRON', 'long': 'ADJ', 'make': 'VERB', 'thing': 'NOUN', 'see': 'VERB', 'him': 'PRON', 'two': 'NUM', 'has': 'AUX', 'look': 'VERB', 'more': 'ADJ', 'day': 'NOUN', 'could': 'AUX', 'go': 'VERB', 'come': 'VERB', 'did': 'VERB', 'my': 'PRON', 'sound': 'NOUN', 'no': 'DET', 'most': 'ADV', 'number': 'NOUN', 'who': 'PRON', 'over': 'ADP', 'know': 'ADJ', 'water': 'NOUN', 'than': 'SCONJ', 'call': 'VERB', 'first': 'ADJ', 'people': 'NOUN', 'may': 'AUX', 'down': 'ADV', 'side': 'NOUN', 'been': 'AUX', 'now': 'ADV', 'find': 'VERB', 'any': 'DET', 'new': 'ADJ', 'work': 'NOUN', 'part': 'NOUN', 'take': 'VERB', 'get': 'VERB', 'place': 'NOUN', 'made': 'VERB', 'live': 'ADJ', 'where': 'SCONJ', 'after': 'ADP', 'back': 'ADV', 'little': 'ADJ', 'only': 'ADJ', 'round': 'ADJ', 'man': 'NOUN', 'year': 'NOUN', 'came': 'VERB', 'show': 'VERB', 'every': 'DET', 'good': 'ADJ', 'me': 'PRON', 'give': 'VERB', 'our': 'PRON', 'under': 'ADJ', 'name': 'NOUN', 'very': 'ADV', 'through': 'ADP', 'just': 'ADV', 'form': 'VERB', 'much': 'ADV', 'great': 'ADJ', 'think': 'NOUN', 'say': 'VERB', 'help': 'VERB', 'low': 'ADJ', 'line': 'NOUN', 'before': 'ADP', 'turn': 'NOUN', 'cause': 'NOUN', 'same': 'ADJ', 'mean': 'NOUN', 'differ': 'VERB', 'move': 'NOUN', 'right': 'ADJ', 'boy': 'NOUN', 'old': 'ADJ', 'too': 'ADV', 'does': 'AUX', 'tell': 'VERB', 'sentence': 'NOUN', 'set': 'VERB', 'three': 'NUM', 'want': 'VERB', 'air': 'NOUN', 'well': 'ADV', 'also': 'ADV', 'play': 'VERB', 'small': 'ADJ', 'end': 'NOUN', 'put': 'VERB', 'home': 'NOUN', 'read': 'VERB', 'hand': 'NOUN', 'port': 'NOUN', 'large': 'ADJ', 'spell': 'NOUN', 'add': 'VERB', 'even': 'ADV', 'land': 'NOUN', 'here': 'ADV', 'must': 'AUX', 'big': 'ADJ', 'high': 'ADJ', 'such': 'ADJ', 'follow': 'NOUN', 'act': 'NOUN', 'why': 'SCONJ', 'ask': 'VERB', 'men': 'NOUN', 'change': 'NOUN', 'went': 'VERB', 'light': 'ADJ', 'kind': 'ADV', 'off': 'ADP', 'need': 'PROPN', 'house': 'NOUN', 'picture': 'NOUN', 'try': 'VERB', 'us': 'PRON', 'again': 'ADV', 'animal': 'NOUN', 'point': 'NOUN', 'mother': 'NOUN', 'world': 'NOUN', 'near': 'ADP', 'build': 'VERB', 'self': 'NOUN', 'earth': 'PROPN', 'father': 'NOUN', 'head': 'NOUN', 'stand': 'VERB', 'own': 'ADJ', 'page': 'NOUN', 'should': 'AUX', 'country': 'NOUN', 'found': 'VERB', 'answer': 'NOUN', 'school': 'NOUN', 'grow': 'NOUN', 'study': 'NOUN', 'still': 'ADV', 'learn': 'VERB', 'plant': 'NOUN', 'cover': 'NOUN', 'food': 'NOUN', 'sun': 'NOUN', 'four': 'NUM', 'thought': 'NOUN', 'let': 'VERB', 'keep': 'VERB', 'eye': 'NOUN', 'never': 'ADV', 'last': 'ADJ', 'door': 'NOUN', 'between': 'ADP', 'city': 'NOUN', 'tree': 'NOUN', 'cross': 'NOUN', 'since': 'SCONJ', 'hard': 'ADJ', 'start': 'NOUN', 'might': 'AUX', 'story': 'NOUN', 'saw': 'VERB', 'far': 'ADV', 'sea': 'NOUN', 'draw': 'NOUN', 'left': 'VERB', 'late': 'ADJ', 'run': 'NOUN', "n't": 'PART', 'while': 'SCONJ', 'press': 'VERB', 'close': 'ADJ', 'night': 'NOUN', 'real': 'ADJ', 'life': 'NOUN', 'few': 'ADJ', 'stop': 'VERB', 'open': 'ADJ', 'seem': 'VERB', 'together': 'ADV', 'next': 'ADJ', 'white': 'ADJ', 'children': 'NOUN', 'begin': 'VERB', 'got': 'VERB', 'walk': 'VERB', 'example': 'NOUN', 'ease': 'NOUN', 'paper': 'NOUN', 'often': 'ADV', 'always': 'ADV', 'music': 'VERB', 'those': 'PRON', 'both': 'DET', 'mark': 'PROPN', 'book': 'NOUN', 'letter': 'NOUN', 'until': 'SCONJ', 'mile': 'NOUN', 'river': 'NOUN', 'car': 'NOUN', 'feet': 'NOUN', 'care': 'VERB', 'second': 'ADJ', 'group': 'NOUN', 'carry': 'VERB', 'took': 'VERB', 'rain': 'NOUN', 'eat': 'NOUN', 'room': 'NOUN', 'friend': 'NOUN', 'began': 'VERB', 'idea': 'NOUN', 'fish': 'NOUN', 'mountain': 'NOUN', 'north': 'NOUN', 'once': 'ADV', 'base': 'NOUN', 'hear': 'VERB', 'horse': 'NOUN', 'cut': 'VERB', 'sure': 'ADV', 'watch': 'VERB', 'color': 'NOUN', 'face': 'VERB', 'wood': 'NOUN', 'main': 'ADJ', 'enough': 'ADJ', 'plain': 'ADJ', 'girl': 'NOUN', 'usual': 'ADJ', 'young': 'ADJ', 'ready': 'ADJ', 'above': 'ADP', 'ever': 'ADV', 'red': 'ADJ', 'list': 'NOUN', 'though': 'SCONJ', 'feel': 'VERB', 'talk': 'NOUN', 'bird': 'NOUN', 'soon': 'ADV', 'body': 'NOUN', 'dog': 'NOUN', 'dogs': 'VERB', "'s": 'PART', 'family': 'NOUN', 'direct': 'ADJ', 'pose': 'NOUN', 'leave': 'VERB', 'song': 'NOUN', 'measure': 'NOUN', 'state': 'NOUN', 'product': 'NOUN', 'black': 'ADJ', 'short': 'ADJ', 'numeral': 'ADJ', 'class': 'NOUN', 'wind': 'NOUN', 'question': 'NOUN', 'happen': 'VERB', 'complete': 'ADJ', 'ship': 'NOUN', 'area': 'NOUN', 'half': 'PRON', 'rock': 'NOUN', 'order': 'NOUN', 'fire': 'NOUN', 'south': 'ADJ', 'problem': 'NOUN', 'piece': 'NOUN', 'told': 'VERB', 'knew': 'VERB', 'pass': 'NOUN', 'farm': 'NOUN', 'top': 'ADJ', 'whole': 'ADJ', 'king': 'NOUN', 'size': 'NOUN', 'heard': 'VERB', 'best': 'ADJ', 'hour': 'NOUN', 'better': 'ADV', 'true': 'ADJ', 'during': 'ADP', 'hundred': 'NUM', 'am': 'NOUN', 'remember': 'VERB', 'step': 'NOUN', 'early': 'ADV', 'hold': 'VERB', 'west': 'ADJ', 'ground': 'NOUN', 'interest': 'NOUN', 'reach': 'VERB', 'fast': 'ADV', 'five': 'NUM', 'sing': 'NOUN', 'sings': 'NOUN', 'listen': 'VERB', 'six': 'NUM', 'table': 'NOUN', 'travel': 'NOUN', 'less': 'ADJ', 'morning': 'NOUN', 'ten': 'NUM', 'simple': 'ADJ', 'several': 'ADJ', 'vowel': 'NOUN', 'toward': 'ADP', 'war': 'NOUN', 'lay': 'VERB', 'against': 'ADP', 'pattern': 'NOUN', 'slow': 'ADJ', 'center': 'NOUN', 'love': 'NOUN', 'person': 'NOUN', 'money': 'NOUN', 'serve': 'VERB', 'appear': 'VERB', 'road': 'NOUN', 'map': 'NOUN', 'science': 'NOUN', 'rule': 'NOUN', 'govern': 'NOUN', 'pull': 'VERB', 'cold': 'ADJ', 'notice': 'NOUN', 'voice': 'NOUN', 'fall': 'NOUN', 'power': 'NOUN', 'town': 'NOUN', 'fine': 'ADJ', 'certain': 'ADJ', 'fly': 'NOUN', 'unit': 'NOUN', 'lead': 'VERB', 'cry': 'NOUN', 'dark': 'ADJ', 'machine': 'NOUN', 'note': 'NOUN', 'wait': 'VERB', 'plan': 'NOUN', 'figure': 'NOUN', 'star': 'PROPN', 'box': 'NOUN', 'noun': 'PROPN', 'field': 'NOUN', 'rest': 'NOUN', 'correct': 'ADJ', 'able': 'ADJ', 'pound': 'NOUN', 'done': 'VERB', 'beauty': 'NOUN', 'drive': 'NOUN', 'stood': 'VERB', 'contain': 'VERB', 'front': 'ADJ', 'teach': 'NOUN', 'week': 'NOUN', 'final': 'NOUN', 'gave': 'VERB', 'green': 'ADJ', 'oh': 'INTJ', 'quick': 'ADJ', 'develop': 'VERB', 'sleep': 'NOUN', 'warm': 'ADJ', 'free': 'ADJ', 'minute': 'NOUN', 'strong': 'ADJ', 'special': 'ADJ', 'mind': 'NOUN', 'behind': 'ADP', 'clear': 'ADJ', 'tail': 'NOUN', 'produce': 'VERB', 'fact': 'NOUN', 'street': 'NOUN', 'inch': 'NOUN', 'lot': 'NOUN', 'nothing': 'PRON', 'course': 'NOUN', 'stay': 'VERB', 'wheel': 'ADJ', 'full': 'ADJ', 'force': 'NOUN', 'blue': 'ADJ', 'object': 'NOUN', 'decide': 'VERB', 'surface': 'NOUN', 'deep': 'ADJ', 'moon': 'NOUN', 'island': 'NOUN', 'foot': 'NOUN', 'yet': 'ADV', 'busy': 'ADJ', 'test': 'NOUN', 'record': 'NOUN', 'boat': 'NOUN', 'common': 'ADJ', 'gold': 'NOUN', 'possible': 'ADJ', 'plane': 'NOUN', 'age': 'NOUN', 'dry': 'ADJ', 'wonder': 'NOUN', 'laugh': 'NOUN', 'thousand': 'NUM', 'ago': 'ADV', 'ran': 'VERB', 'check': 'NOUN', 'game': 'NOUN', 'shape': 'NOUN', 'yes': 'INTJ', 'cool': 'ADJ', 'miss': 'NOUN', 'brought': 'VERB', 'heat': 'NOUN', 'snow': 'NOUN', 'bed': 'NOUN', 'bring': 'VERB', 'sit': 'NOUN', 'perhaps': 'ADV', 'fill': 'VERB', 'east': 'NOUN', 'weight': 'NOUN', 'language': 'NOUN', 'among': 'ADP', 'adult': 'NOUN', 'adults': 'NOUN'}
        question_type = ['time', 'who', 'what', 'how', 'when', 'where']
        sentence_wo_punctuations = ''.join([character for character in sentence if character not in string.punctuation or character == ':'])
        question_wo_punctuations = ''.join([character for character in question if character not in string.punctuation])
        question_words = []
        sentence_words = []
        for word in sentence_wo_punctuations.split():
            sentence_words.append(word.lower())
        for word in question_wo_punctuations.split():
            question_words.append(word.lower())

        for word in question_words:
            if word == 'time':
                for word1 in sentence_words:
                    if ':' in word1:
                        return word1.upper()

        for word in question_words:
            if word == 'when':
                return "morning"

            elif word == 'who':
                proper_nouns_question = []
                for word1 in question_words:
                    if word_dict[word1] == 'PROPN':
                        proper_nouns_question.append(word1)
                if len(proper_nouns_question) == 1:
                    for word1 in sentence_words:
                        if word_dict[word1] == 'PROPN':
                            if word1 in proper_nouns_question:
                                continue
                            else:
                                return word1[0].upper() + word1[1:]
                else:
                    for word1 in sentence_words:
                        if word_dict[word1] == 'PROPN':
                            return word1[0].upper() + word1[1:]
                    for word1 in sentence_words:
                        if word_dict[word1] == 'NOUN':
                            return word1
                for word1 in sentence_words:
                    if word_dict[word1] == 'NOUN':
                        return word1

            elif word == 'what':
                if 'color' in question_words:
                    return "blue"
                if 'do' in question_words:
                    for word1 in sentence_words:
                        if word_dict[word1] == 'VERB':
                            return word1
                for word1 in sentence_words:
                    if word_dict[word1] == 'NOUN' and word1 not in question_words:
                        return word1
                return ""

            elif word == 'where':
                for ind, word1 in enumerate(sentence_words):
                    if word1 == "go" or word1 == "in":
                        for ind1 in range(ind+1, len(sentence_words)):
                            if word_dict[sentence_words[ind1]] == 'PROPN' or word_dict[sentence_words[ind1]] == 'NOUN':
                                return sentence_words[ind1]
                for word1 in sentence_words:
                    if word_dict[word1] == 'NOUN' and word1 not in question_words:
                        return word1
                return ""

            elif word == 'how':
                q_index = question_words.index("how")
                next_word = question_words[q_index+1]
                if next_word == 'many':
                    for word1 in sentence_words:
                        if word_dict[word1] == 'NUM':
                            return word1
                if word_dict[next_word] == 'ADJ':
                    for word1 in sentence_words:
                        if word_dict[word1] == 'ADJ':
                            return word1
                elif word_dict[next_word] == 'AUX':
                    for word1 in sentence_words:
                        if word_dict[word1] == 'VERB':
                            return word1
                else:
                    for word1 in sentence_words:
                        if word_dict[word1] == 'NOUN':
                            return word1

                return ""


        pass