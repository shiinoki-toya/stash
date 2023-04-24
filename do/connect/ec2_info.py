import os

from io import StringIO  # py3

import boto3
import six

# 取得対象アカウント
# ACCOUNTS = ['アクセスキー', 'シークレットアクセスキー', 'リージョン']
ACCOUNTS = [
    ('AKIARB6K3S5EGAP7USI4', 'l2v/Sg85qpcjFnCTm5MrZtYHHELvRbs9Hf4C2X6v', 'ap-northeast-1'),
]
# pemファイルの格納先
ssh_dir = '/home/toya/'
user_name = 'admin'

def main():
    isinstance = get_instance()
    print(isinstance)

def get_instance():
    config_lists = []

    # インスタンス情報の取得
    for access_key_id, secret_access_key, region in ACCOUNTS:
        session = boto3.Session(aws_access_key_id=access_key_id,
                                aws_secret_access_key=secret_access_key,
                                region_name=region)
        client = session.client('ec2')

        # 起動中のインスタンス一覧を取得
        filters = [
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
        response = client.describe_instances(Filters=filters)

        # すべてのインスタンス一覧を取得
        # response = client.describe_instances()

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                config = {}
                tags = {tag['Key']: tag['Value'] for tag in instance['Tags']}
                alias_name = tags.get('Name')
                public_dns_name = instance['PublicDnsName']
                key_name = instance['KeyName']

                config['alias_name'] = alias_name
                config['public_dns_name'] = public_dns_name
                config['user_name'] = user_name
                config['key_name'] = ssh_dir + key_name + '.pem'
                config['key_name'] = f"{ssh_dir}{key_name}.pem"
                config_lists.append(config)

    return config_lists

if __name__ == '__main__':
    main()