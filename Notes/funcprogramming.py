sum()
max()
min()
map()
sorted()
numbers = map(int, input().split())
print(*filter(lambda x: x > 0, numbers))

print(
    *filter(
        lambda x: x > 0,
        map(
            int,
            input().split()
        )
    )
)

print(*enumerate('abcde'))
print(any((True, False, True)))
print(all((True, False, True)))
print(
    all(
        map(
            lambda x: x > 0,
            map(
                int,
                input().split()
            )
        )
    )
)

passengers = map(int, input().split())
sorted_pass = sorted(enumerate(passengers), key=lambda x: x[1])
taxi = map(int, input().split())
sorted_taxi = sorted(enumerate(taxi), key=lambda x: x[1], reverse=True)
answer = zip(sorted_pass, sorted_taxi)
sorted_ans = sorted(answer, key=lambda x: x[0][0])
print(*map(lambda x: x[1][0] + 1, sorted_ans))


print(
    *map(
        lambda x: x[1][0] + 1,
        sorted(
            zip(
                sorted(
                    enumerate(
                        map(
                            int,
                            input().split()
                        )
                    ),
                    key=lambda x: x[1]
                ),
                sorted(
                    enumerate(
                        map(
                            int,
                            input().split()
                        )
                    ),
                    key=lambda x: x[1],
                    reverse=True
                )
            ),
            key=lambda x: x[0][0]
        )
    )
)
