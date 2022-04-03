def add_follower(user_name):
    if user_name in followers_book:
        pass
    else:
        followers_book[user_name] = {"likes": 0, "comments": 0}


def like(user_name, count):
    if user_name not in followers_book:
        followers_book[user_name] = {"likes": count, "comments": 0}
    else:
        followers_book[user_name]["likes"] += count


def comment(user_name):
    if user_name not in followers_book:
        followers_book[user_name] = {"likes": 0, "comments": 1}
    else:
        followers_book[user_name]["comments"] += 1


def block(user_name):
    if user_name not in followers_book:
        print(f"{user_name} doesn't exist.")
    else:
        followers_book.pop(user_name)


followers_book = {}
command_line = input().split(": ")

while "Log out" not in command_line:
    if "New follower" in command_line:
        follower_name = command_line[1]
        add_follower(follower_name)
    elif "Like" in command_line:
        follower_name = command_line[1]
        likes_count = int(command_line[2])
        like(follower_name, likes_count)
    elif "Comment" in command_line:
        follower_name = command_line[1]
        comment(follower_name)
    elif "Blocked" in command_line:
        follower_name = command_line[1]
        block(follower_name)
    command_line = input().split(": ")

print(f"{len(followers_book)} followers")
for follower in followers_book:
    print(f'{follower}: {followers_book[follower]["likes"]+followers_book[follower]["comments"]}')
