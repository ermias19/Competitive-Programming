def jump_game_vi():
    nums = [1,2,3,4,5,6]

    k = 2
    result = 0
    queue = []
    for i in nums:
        queue.append(i)
        # print(queue)
        print(k)
        if i<0 and len(queue) == k+1 or queue[-1] == nums[-1]:
            # print('mnshe nwman')

            result = queue.pop(0)

            result += max(queue)

            while len(queue) != 1:

                queue.pop(0)
            queue[0] = result
        else:
            result=sum(queue)
            print(result,'rsult the the else statment ')
            print('menshe nw broo',queue)

    print(result)


jump_game_vi()
