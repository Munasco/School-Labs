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
        (string)->list
        This function, collects input from a file, and separates the strings and put it in a list satisfying various conditions for punctuations
        >>>parse_story('This "world" is too good.')
        ['This', 'world', 'is', 'too', 'good', '.']
        '''    
    return ([i/sum(x) for i in x])
x_1 = parse_story('308.txt')

def build_n_grams(words, n):
    '''
        (string)->list
        This function, collects input from a file, and separates the strings and put it in a list satisfying various conditions for punctuations
        >>>parse_story('This "world" is too good.')
        ['This', 'world', 'is', 'too', 'good', '.']
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
        (string)->list
        This function, collects input from a file, and separates the strings and put it in a list satisfying various conditions for punctuations
        >>>parse_story('This "world" is too good.')
        ['This', 'world', 'is', 'too', 'good', '.']
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
        (string)->list
        This function, collects input from a file, and separates the strings and put it in a list satisfying various conditions for punctuations
        >>>parse_story('This "world" is too good.')
        ['This', 'world', 'is', 'too', 'good', '.']
        '''    
    for i in counts:
        counts[i][1] = get_prob_from_count(counts[i][1])
    return counts

def build_ngram_model(words, n):
    '''
        (string)->list
        This function, collects input from a file, and separates the strings and put it in a list satisfying various conditions for punctuations
        >>>parse_story('This "world" is too good.')
        ['This', 'world', 'is', 'too', 'good', '.']
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
                (string)->list
                This function, collects input from a file, and separates the strings and put it in a list satisfying various conditions for punctuations
                >>>parse_story('This "world" is too good.')
                ['This', 'world', 'is', 'too', 'good', '.']
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
        (string)->list
        This function, collects input from a file, and separates the strings and put it in a list satisfying various conditions for punctuations
        >>>parse_story('This "world" is too good.')
        ['This', 'world', 'is', 'too', 'good', '.']
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
        (string)->list
        This function, collects input from a file, and separates the strings and put it in a list satisfying various conditions for punctuations
        >>>parse_story('This "world" is too good.')
        ['This', 'world', 'is', 'too', 'good', '.']
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
    
    
