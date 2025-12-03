def check_references():
    # A mutable object (list)
    list_a = [1, 2, 3]
    list_b = list_a  # b references the same object as a

    print(f"ID of A: {id(list_a)}")
    print(f"ID of B: {id(list_b)}")
    
    # Modifying B affects A because they point to the same memory address
    list_b.append(4)
    print(f"List A after modifying B: {list_a}")

    # Reassigning B creates a new reference
    list_b = [10, 20]
    print(f"ID of B after reassignment: {id(list_b)}")
    print(f"List A remains: {list_a}")

check_references()
