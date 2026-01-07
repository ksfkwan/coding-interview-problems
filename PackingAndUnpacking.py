def outer(**outer_kwds):
    print(f"inner_kwds - {id(outer_kwds)}")
    for k, v in outer_kwds.items():
        print(f"kwds - ({k}, {v}): ({id(k)}, {id(v)})")

    def inner(**inner_kwds):
        print(f"\ninner_kwds - {id(inner_kwds)}")
        for k, v in inner_kwds.items():
            print(f"inner_kwds - ({k}, {v}): ({id(k)}, {id(v)})")

    inner(**outer_kwds)

# Example objects
lst = [1.111, 2.222, 3.333]
txt = "Hello World"

outer(abcd=lst, efgh=txt)  # Python interns some strings
