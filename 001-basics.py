def print_hello():
  print('Hello World!')
  print('it works')
  arr =  [1,2,3,4,5]
  for i in arr:
    print(i + 10)

def print_itemsone(n):
    print('items before ')
    while n>=0:
      print(n)
      n-=1
# O(n)
def print_items(n):
   for i in range(n):
      print(i)

# O(n)
def print_items_two(n):
   for i in range(n):
      for j in range(n):
        print(i,j)
    
 
#print_items(10)

print_items_two(3)




