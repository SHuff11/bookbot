def word_count(text):
   words = text.split()
   return len(words)

def character_count(text):
    char_dict = {}
    text = text.lower()
    for x in text:
      if x in char_dict:
         char_dict[str(x)] += 1
      else:
         char_dict[str(x)] = 1
    return char_dict  

def sort_num(items):
   return items["num"]

def sort_dict(dictionary):
   sorted_chardict_list = []
   for k,v in dictionary.items():
      char_count_dict = {}
      char_count_dict["char"] = k
      char_count_dict["num"] = v
      sorted_chardict_list.append(char_count_dict)
      sorted_chardict_list.sort(reverse=True, key=sort_num)
   return sorted_chardict_list


   