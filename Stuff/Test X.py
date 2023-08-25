def find_first_and_second_a(string):
  first_a_index = -1
  second_a_index = -1

  for i in range(len(string)):
    if string[i] == 'a':
      if first_a_index == -1:
        first_a_index = i
      else:
        second_a_index = i

  return first_a_index, second_a_index


string = "algoritma dan pemrograman"
first_a_index, second_a_index = find_first_and_second_a(string)

print("The first 'a' is at index", first_a_index)
print("The second 'a' is at index", second_a_index)