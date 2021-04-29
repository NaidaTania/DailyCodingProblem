# Function to return max sum such that 
# no two elements are adjacent
def find_max_sum(arr):
    incl = 0 #sum with previous element
    excl = 0 #sum w/o previous element
     
    for i in arr:
          
        # Current max excluding i (No ternary in 
        # Python)
        new_excl = excl if excl>incl else incl #pick the one greater bet incl and excl
         
        # Current max including i
        incl = excl + i #update incl with new number
        excl = new_excl #max(incl, excl)
        print("incl:",incl,"excl:",excl)
      
    # return max of incl and excl
    return (excl if excl>incl else incl)
  
# Driver program to test above function
arr = [2, 10, 11, 8, 1]
print(find_max_sum(arr))
  
# This code is contributed by Kalai Selvan
'''
so basically this algo is legit comparing 2+11 vs 10, then 10+8 vs 2+11 and so on.
By making sure excl is always 1 step late, while incl is wherever excl is+next
'''