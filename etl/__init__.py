import os
import json

import petl as etl
import pandas as pd
import numpy as np

from .utils import TimestampConverter


BASE_DIR = './data/'
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 2)


def open_json_file(file_name):
    with open(file_name, 'r') as fd:
        json_str = fd.read()
    return json.loads(json_str)


def extractor(data_type) -> any:
    path = BASE_DIR + data_type + '/'
    files = os.listdir(path)
    temp = []
    for file_name in files:
        record = open_json_file(path + file_name)
        temp.append(record)
    return etl.sort(etl.fromdicts(temp), 'ts')


def unpacked_json(raw_data):
    create_operation = etl.unpackdict(
        etl.select(
            raw_data,
            'op',
            lambda r: r == 'c'
        ),
        'data'
    )
    update_operation = etl.unpackdict(
        etl.select(
            raw_data,
            'op',
            lambda r: r == 'u'
        ),
        'set'
    )
    all_operations = etl.cat(
        create_operation,
        update_operation
    )
    all_operations = etl.convert(
        etl.cutout(
            all_operations,
            'data',
            'set'
        ),
        'ts',
        lambda r: TimestampConverter(r).to_datetime_utc().isoformat(sep='T', timespec='auto')
    )
    return etl.sort(all_operations, 'ts')


def extract_global_id(val, row):
    return row.id.replace('globalid', '')


def recovered_ids(raw_data, column):
    return etl.convert(
        raw_data,
        column,
        extract_global_id,
        pass_row=True
    )


def print_all(record, column='ts'):
    print(
        etl.lookall(
            etl.sort(
                record,
                column
            )
        )
    )


def get_all_data():
    accounts = extractor('accounts')
    unpacked_accounts = unpacked_json(accounts)
    cards = extractor('cards')
    unpacked_cards = unpacked_json(cards)
    savings_accounts = extractor('savings_accounts')
    unpacked_savings_accounts = unpacked_json(savings_accounts)
    
    return (
        etl.todataframe(recovered_ids(unpacked_accounts, 'account_id')),
        etl.todataframe(recovered_ids(unpacked_cards, 'card_id')),
        etl.todataframe(recovered_ids(unpacked_savings_accounts, 'savings_account_id'))
    )


def integrate_all_tables(accounts, cards, savings_accounts):
    account_group_by_sa_id = accounts.groupby(
        ['account_id', 'savings_account_id']
    ).last().reset_index().loc[:, ['account_id', 'savings_account_id']]


    pandas_accounts = accounts.set_index('account_id')
    account_group_by_sa_id = account_group_by_sa_id.set_index('account_id')
    pandas_accounts.update(account_group_by_sa_id)


    pandas_accounts = pandas_accounts.set_index('card_id')
    pandas_cards = cards.set_index('card_id')

    result = pd.merge(
        pandas_accounts,
        pandas_cards,
        how='outer',
        left_on=['ts', 'op', 'id'],
        right_on=['ts', 'op', 'id']
    )

    final_result = pd.concat(
        [result.reset_index(), savings_accounts],
        join='outer',
        keys='savings_account_id'
    )

    return final_result.sort_values(by=['ts'])

