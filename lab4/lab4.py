from utilities import *
def parse_story(file_name):
    '''
    (string)->list
    This function, collects input from a file, and separates the strings and put it in a list satisfying various conditions for punctuations
    >>>parse_story('This "world" is too good.')
    ['This', 'world', 'is', 'too', 'good', '.']
    '''
    with open(file_name) as text:
                        whole_text = text.readlines()
                        defined_length = len(whole_text)
                        new = []
                        for i in range(defined_length):
                                    new.append(whole_text[i].strip('\n').lower())
                                    clean_list = []
                        for i in range(defined_length):
                                    new_sight = new[i]
                                    for j in BAD_CHARS:
                                                new_sight = new_sight.replace(j, ' ')
                                    for j in VALID_PUNCTUATION:
                                                new_sight = new_sight.replace(j, ' '+j+ ' ')
                                    clean_list.append(new_sight)
                        words = []
                        for i in range(len(clean_list)):
                                    words.append(clean_list[i].strip())
                        final_list = []
                        for i in range(len(words)):
                                    if words[i] == '':
                                                continue
                                    else:
                                                final_list.extend(words[i].split())            
                        return final_list

def get_prob_from_count(x):
    '''
   Return a list of probabilitiesderived from counts. Counts is a list of counts  of occurrences of a token after the  previous n-gram.
   You should  not  round  the probabilities.
   Input format counts:  a list of positive integer counts
   Sample inputs
   >>> get_prob_from_count([10, 20, 40, 30])
   [0.1, 0.2, 0.4, 0.3]
    '''
  return ([i/sum(x) for i in x])
x_1 = parse_story('308.txt')

def build_n_grams(words, n):
    '''
        Return a dictionary of N-grams (where N=n) and the counts of the  words  that follow  the N-gram.
        The key  of  the  dictionary will be  the  N-gram in a tuple.
        The  corresponding  value will be a list containing two  lists.
        The first list contains the words and the second list contains the corresponding  counts.
        Input format 
        words:  a list of words  obtained  from parse_story n: the  size of the  N-gram
        Sample inputs
        >>> words = [‘the’, ‘child’, ‘will’, ‘go’, ‘out’, ‘to’, ‘play’, ‘,’, ‘and’, ‘the’, ‘child’, ‘can’, ‘not’, ‘be’, ‘sad’, ‘anymore’, ‘.’]
        >>> build_ngram_counts(words, 2)
        {(‘the’, ‘child’): [[‘will’, ‘can’], [1, 1]],(‘child’, ‘will’): [[‘go’], [1]], (‘will’, ‘go’): [[‘out’], [1]], (‘go’, out’): [[‘to’], [1]],(‘out’, ‘to’): [[‘play’], [1]], (‘to’, ‘play’): [[‘,’], [1]], (‘play’, ‘,’): [[‘and’], [1]], (‘,’, ‘and’): [[‘the’], [1]], (‘and’, ‘the’): [[‘child’], [1]], (‘child’, ‘can’): [[‘not’], [1]], (‘can’, ‘not’): [[‘be’], [1]], (‘not’, ‘be’): [[‘sad’], [1]], (‘be’, ‘sad’): [[‘anymore’],[1]],(‘sad’, ‘anymore’): [[‘.’], [1]]}Note:•Thekey-value  pairs do  not have  to appear  in  the  exact  orderabove because  Python dictionaries areunordered.•The wordsand countsdo  not  have to appear in the  exact order above(though  it may be helpful to store the counts  in sorted order),but the wordsand counts  indices mustmatch. e.g. the  value [[‘at’, ‘be’],  [4,  2]]  means  that “at” appears four times, and “be” appears twice.
        '''    
    p = {}
    for i in range(len(words)-n):
        if tuple(words[i:i+n]) not in p.keys():
            p[tuple(words[i:i+n])] = [[words[i+n]],[1]]
        else:
            if words[i+n] in p[tuple(words[i:i+n])][0]:
                p[tuple(words[i:i+n])][1][p[tuple(words[i:i+n])][0].index(words[i+n])] += 1
            else:
                p[tuple(words[i:i+n])][0].append(words[i+n])
                p[tuple(words[i:i+n])][1].append(1)
    return p
                                  

def prune_ngram_counts(counts, prune_len):
    '''
    Return a dictionary of N-grams and counts  of words with lower frequency (i.e. occurring less often) words  removed.
    You  will  prune  the  words  based  on  their  counts,  keeping  the prune_len highest frequency  words.
    In  case of  a tie(for example, if prune_len was 5 and the 5th and 6th most  frequent  words had the  same frequency), 
    then keep  all words  that are in the tie(e.g. keep both the 5th and 6th words).
    Input format counts:  a  dictionary  of  N-grams  and word counts formatted according  to the  output  of build_ngram_counts 
    prune_len:  the number of highest frequency  words to  keep (potentially more if ties occur)
    Sample inputs
    >>> ngram_counts= {(‘i’, ‘love’): [[‘js’, ‘py3’, ‘c’, ‘no’], [20, 20, 10, 2]],(‘u’, ‘r’): [[‘cool’, ‘nice’, ‘lit’, 'kind’], [8, 7, 5, 5]],('toronto’, ‘is’): [[‘six’, ‘drake’], [2, 3]]}
    >>> prune_ngram_counts(ngram_counts, 3)
    {(‘i’, ‘love’): [[‘js’, ‘py3’, ‘c’], [20, 20, 10]],(‘u’, ‘r’): [[‘cool’, ‘nice’, ‘lit’, 'kind’], [8, 7, 5, 5]],('toronto’, ‘is’): [[‘six’, ‘drake’],[2, 3]]}
        '''    
    n = prune_len
    for i in counts:
        z = []
        r = sorted(counts[i][1], reverse = True)
        if n >= len(r):
            z = r[:]
        elif r[n-1] != r[n]:
            z = r[:n]
        else:

            z = r[:n]
            while (n<len(r))and(r[n-1] == r[n]):
                z.append(r[n])
                n = n+1
        j = 0
        while j < len(counts[i][1]):
            if counts[i][1][j] not in z:
                counts[i][0].remove(counts[i][0][j])
                counts[i][1].remove(counts[i][1][j])
                j = j-1
            j = j+ 1
    return counts
def probify_ngram_counts(counts):
    '''
        Take a  dictionary  of N-grams  and  counts  and  convert the  counts  to  probabilities.
        The probability of  each word is defined  as the observed  count divided  by  the  total count of all words.
        Input format counts:  a dictionary of N-grams and word counts  formatted according to  the output  of prune_ngram_counts 
        Sample inputs
        >>> ngram_counts = {(‘i’, ‘love’): [[‘js’, ‘py3’, ‘c’], [20, 20, 10]],(‘u’, ‘r’): [[‘cool’, ‘nice’, ‘lit’, 'kind’], [8, 7, 5, 5]],('toronto’, ‘is’): [[‘six’, ‘drake’], [2, 3]]}
        >>> probify_ngram_counts(ngram_counts){(‘i’, ‘love’): [[‘js’, ‘py3’, ‘c’], [0.4, 0.4, 0.2]],(‘u’, ‘r’): [[‘cool’, ‘nice’, ‘lit’, 'kind’], [0.32, 0.28, 0.2, 0.2]],('toronto’, ‘is’): [[‘six’, ‘drake’], [0.4, 0.6]]}
        '''    
    for i in counts:
        counts[i][1] = get_prob_from_count(counts[i][1])
    return counts

def build_ngram_model(words, n):
    '''
        Create  and  return  a  dictionary  of  the  format  given  above  in probify_ngram_counts.
        This dictionary is your  final model that will be used  to auto-generate text.
        For  your  final model,  keep  the  15  most likely  words  that  follow  an  N-gram.
        Moreover,  for each N-gram, the corresponding next words should appear in descending order of probability.
        Input format words:  a list of words/punctuation  obtained  from parse_story 
        n: the  size of N in the N-grams.
        Sample inputs
        >>> words = [‘the’, ‘child’, ‘will’, ‘the’, ‘child’, ‘can’, ‘the’, ‘child’, ‘will’, ‘the’, ‘child’, ‘may’,‘go’, ‘home’, ‘.’]
        >>> build_ngram_model(words, 2){(‘the’, ‘child’): [[‘will’, ‘can’, ‘may’], [0.5, 0.25, 0.25]],(‘child’, ‘will’): [[‘the’], [1.0]],(‘will’, ‘the’): [[‘child’],[1.0]],(‘child’, ‘can’): [[‘the’], [1.0]],(‘can’, ‘the’): [[‘child’], [1.0]],(‘child’, ‘may’): [[‘go’], [1.0]],(‘may’, ‘go’): [[‘home’], [1.0]],(‘go’, ‘home’): [[‘.’], [1.0]]}
        '''    
    counts = probify_ngram_counts(prune_ngram_counts(build_n_grams(words, n), 15))
    for i in counts:
        '''
        counts[i][0].sort(key=lambda words: words[0], reverse = True)
        counts[i][1].sort(reverse = True)
        '''
        j = 0
        while j < len(counts[i][0])-1:
            z = max(counts[i][1][j:])
            n = counts[i][1][j]
            if n < z:
                counts[i][0][j], counts[i][0][counts[i][1][j+1:].index(z) + j+1] = counts[i][0][counts[i][1][j+1:].index(z) + j+1], counts[i][0][j]
                counts[i][1][j], counts[i][1][counts[i][1][j+1:].index(z) + j+1] = counts[i][1][counts[i][1][j+1:].index(z) + j+1], counts[i][1][j]
            j=j+1
    return counts
def gen_bot_list(ngram_model, seed, num_tokens= 0):    
            z = True
            '''
            Returns a randomly generated list of  tokens  (strings) that starts  with the  N tokens  in seed, selecting  all subsequent  tokens  using gen_next_token.
            The list  ends  when  any  of  the following happens:
            •List contains num_tokens tokens, including  repetitions.In  case  seed  is  longer than num_tokens, the  returned  list should  contain  the  first num_tokens tokens ofthe seed.
            •Any  of the  assumptions  of gen_next_token is violated.
            I.e. if either an N-gram is not in the model, or if an N-gram has no tokens  that follow it.
            Input format ngram_model: the  format  of  this  input  is  the  same  as  the  format  of  the  output of build_ngram_model.
            However,  your  code for  this  function should  be  able  to  handle cases where not all N-grams are present in the dictionary.
            seed: a tuple of strings representing the first N tokens  in the  list.num_tokens: a positive intrepresenting the largest number of tokens  to be put  in the  list
            Assume  that you  will never have a test case where N in the ngram_model and N in the seed are mismatched.
            For  example, if ngram_model contains  4-grams, seed will be  a 4-gram as well.
            Sample inputs and outputs
            >>> ngram_model = {('the', 'child'): [['will', 'can','may'], [0.5, 0.25, 0.25]], 
            \('child', 'will'): [['the'], [1.0]], \('will', 'the'): [['child'], [1.0]], \('child', 'can'): [['the'], [1.0]], \('can', 'the'): [['child'], [1.0]], \('child', 'may'): [['go'], [1.0]], \('may', 'go'): [['home'], [1.0]], \('go', 'home'): [['.'], [1.0]] \}
            >>> random.seed(10)
            >>> gen_bot_list(ngram_model, ('hello', 'world'))
            []
            >>> gen_bot_list(ngram_model, ('hello', 'world'), 5)
            ['hello', 'world']
            >>> gen_bot_list(ngram_model, ('the', 'child'), 5)
            ['the', 'child', 'can']
            Note  that the removal of the  crossed out ('child', 'can') 2-gram is the reason for the termination.
            >>> gen_bot_list(ngram_model, ('the', 'child'), 5)
            ['the', 'child', 'will', 'the', 'child']
                '''            
            r = 0
            answer = list(seed[:])
            if seed ==():
                        return []
            elif seed not in ngram_model.keys():
                        return list(seed)
            elif num_tokens==0:
                        return []
            elif len(seed) > num_tokens:
                        return list(seed[0:num_tokens])

            while r< num_tokens-len(seed) and z == True:
                        if check_open_ngram(seed,ngram_model):
                                    new_seed = gen_next_token(seed, ngram_model)
                                    p = list(seed[1:])
                                    p.append(new_seed)
                                    seed = tuple(p)
                                    answer.append(new_seed)
                        else:
                                    z = False
                        r+=1
            return answer
def gen_bot_text(token_list, bad_author):
    '''
     Consider lab4v2.pdf
        '''    
    answer = ''
    if bad_author == True:
        for i in range(len(token_list)):
            if i == 0:
                answer = token_list[i]
            else:
                answer = answer + ' ' + token_list[i]
    if bad_author == False:
        cap_low = [x.lower() for x in ALWAYS_CAPITALIZE]
        for i in range(len(token_list)):
            if i == 0:
                if token_list[i] == token_list[i][0].upper() + token_list[i][1:].lower():
                    answer = token_list[i]
                    continue
                else:
                    token_list[i] = token_list[i][0].upper() + token_list[i][1:].lower()
                    sentence = token_list[i]
            else:
                if token_list[i-1] in END_OF_SENTENCE_PUNCTUATION:
                    if token_list[i] in VALID_PUNCTUATION:
                        answer = answer + token_list[i]  
                    else:
                        token_list[i] = token_list[i][0].upper() + token_list[i][1:].lower()                    
                        answer = answer + ' ' + token_list[i]                                            
                else:
                    if token_list[i].lower() not in cap_low and token_list[i] not in VALID_PUNCTUATION:
                        answer = answer + ' ' + token_list[i]
                    elif token_list[i] not in VALID_PUNCTUATION and token_list[i].lower() in cap_low:
                        token_list[i] = token_list[i][0].upper() + token_list[i][1:].lower()                    
                        answer = answer + ' ' + token_list[i]
                    elif token_list[i] in VALID_PUNCTUATION:
                        answer = answer + token_list[i] 
                        
    return answer    
                
                                    
                                    
                        

ngram_counts= {('i', 'love'): [['js', 'py3', 'c', 'no'], [20, 10, 20, 20]],('u', 'r'): [['cool', 'nice', 'lit', 'kind', 'tyd'], [8, 7, 5, 5, 8]],('toronto', 'is'): [['six', 'drake', 'ler'], [2, 3, 5]]}
#print(build_ngram_model(x_1, 2)) 
print(gen_bot_list(build_ngram_model(x_1, 3), ('i', 'remember', 'going'), 7))

text = ' '.join(x_1)

def write_story(file_name, text, title, student_name, author, year):
    '''
       Consider lab4v2.pdf
        '''    
    f = open(file_name, 'w')
    for i in range(10):
        f.write('\n')
    f.write(title + ':' + ' '+ str(year)+ ', UNLEASHED'+'\n')
    f.write(student_name+', inspired by '+author+'\n')
    f.write('Copyright year published ('+str(year)+'), publisher: EngSci press'+'\n')
    for i in range(17):
        f.write('\n')
    start = 0
    finished = False
    line_count = 0
    new_page = 1
    terminate = False
    page_new_chapter = False
    chapter_number = 1
    while start+ 90 < len(text):
        f.write('CHAPTER '+str(chapter_number)+'\n\n')
        line_count += 2
        page_new_chapter = False
        while not (page_new_chapter) and start < len(text):
            line_count += 2
            while(line_count < 30):
                if start+90 < len(text):
                    if text[start+89] == ' ':
                        f.write(text[start:start+89]+'\n')
                        start = start+90
                        line_count +=1
                    elif text[start+90] == ' ':
                        f.write(text[start:start+90]+'\n')
                        start = start + 91
                        line_count += 1
                    else:
                        stop = start + text[start:start+89].rindex(' ')
                        f.write(text[start:stop]+'\n')
                        start = stop+1
                        line_count +=1
                else:
                    f.write(text[start:]+'\n')
                    start = len(text)
                    line_count += 1
                    finished = True
            if not finished:
                f.write('\n'+str(new_page)+'\n')
            else:
                f.write('\n'+str(new_page))
        
            if(new_page % 12 == 0):
                page_new_chapter = True
            new_page +=1
            line_count = 0
        line_count = 0
        chapter_number += 1
    f.close()
if __name__ == '__main__':
    write_story('new_text.txt', text, 'Three Men in a Boat', 'Jerome K. Jerome', 'Jerome K. Jerome', 1889)
    
    
