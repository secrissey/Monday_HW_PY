# Step 1
def storeInfo():
    stuff = {} # Step 2
    
    # Step 3
    while True:
        # Step 4
        grocery = input("Enter an item to be stored: ")
        more = input("Is there anything more to be stored: ")
        clear_output()

        
        # Step 5
        if grocery.lower() == 'quit':
            # Step 5a
            for key,value in stuff.items():
                print(sorted(stuff.items()))
            break # Step 5b
        stuff[grocery] = more # Apart of step 4 & step 6
        remove = input("Is there anything to be removed: ")
        clear_output()
        del stuff['grocery']
storeInfo() # Step 7