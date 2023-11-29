
def ExecutionTimer_test_case():

    def test_func(a,b, **params):
        result = 1

        while result < 1000000000:
            result += a + b

        print(result, params)

    from Timers import ExecutionTimer

    arg1 = 2
    arg2 = 3
    arg3 = {
        '1': 1,
        '2': 2,
        '3': 3
    }

    with ExecutionTimer(test_func) as f:
        f.run(arg1, arg2, **arg3)

if __name__ == '__main__':
    ExecutionTimer_test_case()



