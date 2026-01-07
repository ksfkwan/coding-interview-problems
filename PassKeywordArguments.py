def outer(**outer_kwds):
    print(f"outer_kwds - {id(outer_kwds)}")
    for k, v in outer_kwds.items():
        print(f"outer_kwds - ({k}, {v}): ({id(k)}, {id(v)})")

    def inner(**inner_kwds):
        print(f"\ninner_kwds - {id(inner_kwds)}")
        for k, v in inner_kwds.items():
            print(f"inner_kwds - ({k}, {v}): ({id(k)}, {id(v)})")

    inner(**outer_kwds)

lst = [1.111, 2.222, 3.333]
txt = "Hello World"

outer(a=lst, b=txt)  # Python does intern some strings



outer_kwds = {'Her name is V': lst, 'My name is M': txt}
print(f"\nouter_kwds - {id(outer_kwds)}")
for k, v in outer_kwds.items():
    print(f"outer_kwds - ({k}, {v}): ({id(k)}, {id(v)})")

def inner(**inner_kwds):
    print(f"\ninner_kwds - {id(inner_kwds)}")
    for k, v in inner_kwds.items():
        print(f"inner_kwds - ({k}, {v}): ({id(k)}, {id(v)})")

inner(**outer_kwds)


# Python does the following conceptually behind the scenes:
inner_kwds = {}
for key, value in outer_kwds.items():
    inner_kwds[key] = value
