T= int(input())

for tc in range(1, T+1):
    number = int(input())

    #숫자의 개수를 셀 카운트 배열
    counts = [0] * 12    #여분으로 2칸 더 만듦

    for i in range(6):
        #number의 1의 자리에 있는 숫자를 하나 증가시킴
        #10으로 나눈 나머지
        counts[number % 10] +=1

        #다음에 일의자리를 위해 10으로 나눈 몫만 사용
        number = number//10

    #run 또는 triplet을 판단할 기준 숫자
    i = 0
    #run 또는 triplet을 발견한 횟수
    run_cnt = tri_cnt = 0
    # 숫자는 9번까지 있음, 10이 되면 종료
    while i < 10:
        #triplet 검사 먼저
        if counts[i] >= 3:
            #숫자i 카드 세장 사용해서 triplet
            counts[i] -=3
            #triplet 만든 횟수 1 증가
            tri_cnt += 1
            continue
        # run 검사
        if counts[i] >=1 and counts[i+1] >=1 and counts[i+2] >= 1:
            #숫자 i, i+1, i+2 세장 사용해서 run
            counts[i] -=1
            counts[i+1] -=1
            counts[i+2] -=1
            #run 만든 횟수 1 증가
            run_cnt +=1
            continue
        i +=1
    # 9번까지 다 봤으면 run 횟수, triple 횟수 합쳐서 2 되는지 확인
    # 2 되면 Baby Gin, 안되면 Lose
    if run_cnt + tri_cnt ==2:
        print(f"#{tc} Baby Gin")
    else:
        print(f"#{tc} Lose")