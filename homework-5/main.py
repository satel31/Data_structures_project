from src.linked_list import LinkedList

if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})

    print(ll)
    assert str(ll) == " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
