import argparse

from etl import get_all_data, integrate_all_tables, summary_all_tables


def task_1():
    accounts, cards, savings_accounts = get_all_data()
    print('=' * 50 + " Task 1 " + '=' * 50)
    print('=' * 50 + " Accounts " + '=' * 50)
    print(accounts)
    print('=' * 50 + " Cards " + '=' * 50)
    print(cards)
    print('=' * 50 + " Savings Accounts " + '=' * 50)
    print(savings_accounts)


def task_2():
    print('=' * 50 + " Task 2 " + '=' * 50)
    print('=' * 50 + " History " + '=' * 50)
    accounts, cards, savings_accounts = get_all_data()
    print(summary_all_tables(accounts, cards, savings_accounts))


def task_3():
    print('=' * 50 + " Task 3 " + '=' * 50)
    accounts, cards, savings_accounts = get_all_data()
    summaries = integrate_all_tables(accounts, cards, savings_accounts)
    print(
        summaries[
            (
                (summaries['credit_used'] > 0) | (summaries['balance'] > 0)
            )
        ]
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process the warehouse data')
    parser.add_argument('-m', '--mode', type=str, help='execution mode')

    args = parser.parse_args()
    if args.mode == 'task-1':
        task_1()
    elif args.mode == 'task-2':
        task_2()
    elif args.mode == 'task-3':
        task_3()
    else:
        task_1()
        task_2()
        task_3()
