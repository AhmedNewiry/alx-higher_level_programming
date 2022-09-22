#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    identifiers = dir(hidden_4)
    for id in identifiers:
        if id[:2] != "__":
            print("{}".format(id))
