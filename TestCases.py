import sys
def ExecutionTimer_test_case():

    from Timers import ExecutionTimer

    with ExecutionTimer(SortingMethods_test_case) as f:
        f.run()



def SortingMethods_test_case():


    from Sorters import SortingMethods
    from random import randint


    test_list = [randint(0,100) for _ in range(80000)]

    print(test_list)
    test_list_tt = SortingMethods.bubble(test_list)
    print(test_list)

def list_examples():

    from random import randint

    list_ = [randint(0, 100) for _ in range(7)]
    print(list_)
    print(list_[int(len(list_)/2):])
    print(list_[:int(len(list_) / 2)])

    l1, l2 = list_[::int(len(list_)/2)]
    print(l1,l2)


if __name__ == '__main__':
    #ExecutionTimer_test_case()
    list_examples()






