import operator

import requests


def download_file(url: str):
    # TODO: Check status code to see if valid or raise error
    # TODO: Write test cases to check the same
    file_name = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return file_name


def get_user(line: str):
    return line.split('>:')[0].split('<')[1]


def get_top_users(url: str, n: int = 3):
    file_name = download_file(url)
    user_dict = {}
    with open(file_name, 'r') as fp:
        for line in fp:
            if line.startswith('<'):
                user = get_user(line)
                if user in user_dict:
                    user_dict[user] += 1
                else:
                    user_dict[user] = 1

    sorted_user_dict = sorted(user_dict.items(), key=operator.itemgetter(1), reverse=True)

    # TODO: Check if n is in range otherwise raise error also test case for it
    print(sorted_user_dict[:n])


if __name__ == "__main__":
    url = 'https://s3.ap-south-1.amazonaws.com/haptikinterview/chats.txt'
    get_top_users(url)
