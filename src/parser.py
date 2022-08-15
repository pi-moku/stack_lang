def parser(tokens):
    #現在のtoken
    pc = 0
    #スタック
    stack = []
    #lexerで追加したpendpが来るまで pendpはプログラムの終わりを意味する
    while tokens[pc] != "pendp":
        #push : stackにpushする
        if tokens[pc] == 'push':
            #tokensを一つ進める
            pc += 1
            #( であることを確認して、文字列を取得
            if tokens[pc] == '(':
                pc += 1   # "hello "
                name = tokens[pc].strip('"')
                pc += 1  #)
                #）であることを確認して, push
                if tokens[pc] == ')':
                    stack.append(name)
                    pc += 1
                else:
                    print('push error code:1')
                    pc += 1
            else:
                #おそらく数字
                why = tokens[pc].strip('()')
                if why.isdecimal():
                    stack.append(int(why))
                    pc += 1
                else:
                    #数字でもない
                    print('push error code:2')
                    pc += 1
        elif tokens[pc] == 'pop':
            #stackに要素があることを確認してpopした結果を表示
            try:
                print(stack.pop())
            except:
                print('pop error :not stack')
            pc += 1
        elif tokens[pc] == 'getp':
            #入力を取得してstackにpush
            stack.append(input())
            pc += 1
        elif tokens[pc] == 'add':
            #stackから二回popして足した結果をstackにpush
            try:
                stack.append(int(stack.pop()) + int(stack.pop()))
            except:
                print('add error: type error')
            pc += 1
        elif tokens[pc] == 'sub':
            #引く
            try:
                stack.append(int(stack.pop()) - int(stack.pop()))
            except:
                print('sub error: type error')
            pc += 1
        elif tokens[pc] == 'mul':
            #mulは、'hello' * 6 でも行けるからtry~~~~~exceptはなし
            stack.append(stack.pop() * stack.pop())
            pc += 1
        elif tokens[pc] == 'div':
            #割るときはゼロによる除算もあるから注意
            try:
                stack.append(int(stack.pop()) / int(stack.pop()))
            except:
                print('div error: type error or zerodivisionerror')
            pc += 1
        elif tokens[pc] == 'if':
            pc += 1
            #1だったら
            if stack.pop():
                while tokens[pc] != 'end':
                    if tokens[pc] == 'push':
                        #tokensを一つ進める
                        pc += 1
                        #( であることを確認して、文字列を取得
                        if tokens[pc] == '(':
                            pc += 1   # "hello "
                            name = tokens[pc].strip('"')
                            pc += 1  #)
                            #）であることを確認して, push
                            if tokens[pc] == ')':
                                stack.append(name)
                                pc += 1
                            else:
                                print('push error code:1')
                                pc += 1
                        else:
                            #おそらく数字
                            why = tokens[pc].strip('()')
                            if why.isdecimal():
                                stack.append(int(why))
                                pc += 1
                            else:
                                #数字でもない
                                print('push error code:2')
                                pc += 1
                    elif tokens[pc] == 'pop':
                        #stackに要素があることを確認してpopした結果を表示
                        try:
                            print(stack.pop())
                        except:
                            print('pop error :not if stack')
                        pc += 1
                    else:
                        if tokens[pc] == 'end':
                            pass
                        else:
                            print('error if ')
                        pc += 1

        else:
            if tokens[pc] == 'end':
                pass
            else:
                print("syntaxerror")
            pc += 1
