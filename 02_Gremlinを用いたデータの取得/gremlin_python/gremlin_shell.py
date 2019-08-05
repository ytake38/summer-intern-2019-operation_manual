import argparse

from gremlin_python.driver import client, serializer
import pprint


ENDPOINT = 'wss://summer-intern-2019.gremlin.cosmosdb.azure.com:443/'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gremlin Shell')
    parser.add_argument('-d', '--database', type=str,
                        default='intern-data', help='name of database')
    parser.add_argument('-g', '--graph', type=str,
                        default='chiwawa', help='name of graph')
    parser.add_argument('-k', '--key', type=str, required=True,
                        help='primary key to connect database')

    args = parser.parse_args()

    c = client.Client(ENDPOINT, 'g',
                      username="/dbs/{0}/colls/{1}".format(
                          args.database, args.graph),
                      password="{}".format(args.key),
                      message_serializer=serializer.GraphSONSerializersV2d0()
                      )

    print('Connected to {} database!'.format(args.graph))
    print(':quit to exit\n')

    while True:
        print('gremlin> ', end="")
        query = input()
        if query == ':quit':
            break
        elif query == '':
            continue

        # クエリを発行してcallbackを取得
        callback = c.submitAsync(query)
        # コールバックが複数回に分かれて返ってくるので一つのリストにする
        response = [res for result in callback.result() for res in result]
        pprint.pprint(response)
        print('\n')
