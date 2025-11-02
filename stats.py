def count_text(text):
    splited_text =  text.split()
    
    count = len(splited_text)
           
    return count

def character_count(text):
    char_dict = {}
    modified_text = text.lower()
    
    for c in modified_text:
        if c.isalpha():
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] += 1
                     
    return char_dict


def sort_items(dictionary):
    new_list = []
 
    for item in dictionary:
        new_list.append({"char": item, "num": dictionary[item]})
    
    new_list.sort(reverse=True, key=lambda x: x['num'])
            
    return new_list #return a sorted list of dictionaries

    
            