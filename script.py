# Some starting numbers
# the number we're checking
search_num = 1
# the next triangular number in sequence
next_tri = 6
# the number we use to generate the next triangular number in the search space
next_tri_components = [3, 6]
#tri_list is [
#   number to add to get the next iteration,
#   starting triangle number,
#   current iteration count,
#   current number ]
search_space = [[2,3,0,3]]
# the dict of results
results = {}

while search_num <= 500:
#    print("search_num:", search_num)
    for tri_list in search_space:
#        print("tri_list:", tri_list)
        if search_num == tri_list[3]:
#            print("found a trap number:", search_num)
            tri_list[2] += 1 #increment the counter
            tri_list[3] += tri_list[0] #increment the current number by the "number to add to get the next number"
            if search_num in results:
                results[search_num]+=1
            else:
                results[search_num]=1
#            print("found", search_num, ":", results[search_num])
        if search_num > tri_list[3]:
#            print("search number exceeds current iteration:", tri_list)
            tri_list[2] += 1 #increment the counter
            tri_list[3] += tri_list[0] #increment the current number by the "number to add to get the next number"
        if search_num == next_tri:
#            print("search_num = next_tri", search_num, next_tri)
            search_space.append([next_tri_components[0], next_tri_components[1], 0, next_tri])
#            print("updated search_space:", search_space)
            next_tri_components = [next_tri_components[0]+1, next_tri]
#            print("updated next_tri_components:", next_tri_components)
            next_tri = next_tri_components[0] + next_tri
#            print("updated next_tri:", next_tri)
#    print("finished searching for:", search_num)
    search_num += 1

smallest = {}

# Note: this would work except that some numbers are the smallest of more than one trapezoidal category. For example, 45 is the smallest number that can be written as four consecutive integers and five consecutive integers.  Goign to need to rewrite this. 
trap_count = 1
for result, count in results.items():
#    print("result,count:", result, count)
    if count == trap_count:
        smallest.update({count : result})
        trap_count +=1
        continue
 
print(smallest)
