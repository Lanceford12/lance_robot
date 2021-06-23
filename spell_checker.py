# Function to return the spelling suggestions
# from the given tokens
def check_spelling(tokens, english_words):
    suggestions = []
    for token in tokens:
        for word in english_words:
            distance = jaccard_distance(jaccardIndex=jaccard_index(set(token), set(word)))
            if distance <= 0.2:
                suggestions.append(word)

    return suggestions

# Function to return the 
# intersection set of s1 and s2 
def intersection(s1, s2) :
  
    # Find the intersection of the two sets 
    intersect = s1 & s2 ;
  
    return intersect; 
  
  
# Function to return the Jaccard index of two sets 
def jaccard_index(s1, s2) :
      
    # Sizes of both the sets 
    size_s1 = len(s1); 
    size_s2 = len(s2); 
  
    # Get the intersection set 
    intersect = intersection(s1, s2); 
  
    # Size of the intersection set 
    size_in = len(intersect); 
  
    # Calculate the Jaccard index 
    # using the formula 
    jaccard_in = size_in  / (size_s1 + size_s2 - size_in); 
  
    # Return the Jaccard index 
    return jaccard_in; 
  
  
# Function to return the Jaccard distance 
def jaccard_distance(jaccardIndex)  :
  
    # Calculate the Jaccard distance 
    # using the formula 
    jaccard_dist = 1 - jaccardIndex; 
  
    # Return the Jaccard distance 
    return jaccard_dist; 