def subsequences(input_string,output_str=""):
    if len(input_string)==0 :
        print (f"{output_str}")
        return
    subsequences(input_string[1:],output_str+input_string[0]) #INCLUDED
    subsequences(input_string[1:],output_str)   #NOT INCLUDED

str = input("Enter string: ")
subsequences(str)

'''

                                                  START
                                    _____input_str: "ab", output_str: ""______
                                   /                                         \
                                  /                                           \
                PART 2: Keep 'a' /                                             \ PART 3: Skip 'a'
                                /                                               \
            input_str: "b", output_str: "a"                                         input_str: "b", output_str: ""
                       /         \                                                  /                        \
                      /           \                                                /                          \
       PART 2: Keep 'b'          PART 3: Skip 'b'                       PART 2: Keep 'b'                     PART 3: Skip 'b'
                    /               \                                  /               \
 input_str: "", output_str: "ab"   input_str: "", output_str: "a"   input_str: "", output_str: "b"         input_str: "", output_str: ""

          |                                 |                                 |                                 |
     [BASE CASE]                       [BASE CASE]                       [BASE CASE]                       [BASE CASE]
     Prints: "ab"                      Prints: "a"                       Prints: "b"                       Prints: ""
     and returns                       and returns                       and returns                       and returns

'''