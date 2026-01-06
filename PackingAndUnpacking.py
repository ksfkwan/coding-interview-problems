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
lst = [1, 2, 3]
txt = "hello"

outer(abcd=lst, efgh=txt)