import operator

def inputData(sum_Score, hakbon_Math, field_Math):

    input_Data = open('baseMath.txt', "r")
    lines = input_Data.readlines()
    print(lines)
    #input('')
    cnt = 0
    for line in lines:
        line = line.strip("\n")
        field = line.split(" ")[0]
        hakbon = int(line.split(" ")[1])
        hakbon_Math.insert(cnt, hakbon)
        field_Math[hakbon] = field
        score = int(line.split(" ")[2])
        sum_Score[0][hakbon] = score
        sum_Score[3][hakbon] = 0
        sum_Score[3][hakbon] = sum_Score[3][hakbon] + score
        print( f"{hakbon}의 점수 {sum_Score[0][hakbon]} 누적점수/ {sum_Score[3][hakbon]}" )
        cnt += 1
    input_Data.close()
    #input('')

    input_Data = open('baseMath_2.txt', "r")
    lines = input_Data.readlines()

    cnt = 0
    for line in lines:
        line = line.strip("\n")
        field = line.split(" ")[0]
        hakbon = int(line.split(" ")[1])
        #hakbon_Math[cnt] = hakbon
        score = int(line.split(" ")[2])
        sum_Score[1][hakbon] = score
        sum_Score[3][hakbon] = sum_Score[3][hakbon] + score
        print(f"{hakbon}의 점수 {sum_Score[1][hakbon]} 누적점수/ {sum_Score[3][hakbon]}")
        cnt += 1
        #print(line)
    input_Data.close()
    #input('')

    cnt = 0
    input_Data = open('baseMath_3.txt', "r")
    lines = input_Data.readlines()
    for line in lines:
        line = line.rstrip("\n")
        field = line.split("\t")[0]
        hakbon = int(line.split("\t")[1])
        #hakbon_Math[cnt] = hakbon
        score = int(line.split("\t")[2])
        sum_Score[2][hakbon] = score
        sum_Score[3][hakbon] = sum_Score[3][hakbon] + score
        print(f"{hakbon}의 점수 {sum_Score[2][hakbon]} 누적점수/ {sum_Score[3][hakbon]}")
        cnt += 1
    input_Data.close()
    return

def inputData2(sum_Score, hakbon_Math, field_Math):

    input_Data = open('Math.txt', "r")
    lines = input_Data.readlines()
    print(lines)
    #input('')
    cnt = 0
    for line in lines:
        line = line.strip("\n")
        field = line.split(" ")[0]
        hakbon = int(line.split(" ")[1])
        hakbon_Math.insert(cnt, hakbon)
        field_Math[hakbon] = field
        score = int(line.split(" ")[2])
        sum_Score[0][hakbon] = score
        sum_Score[3][hakbon] = 0
        sum_Score[3][hakbon] = sum_Score[3][hakbon] + score
        print( f"{hakbon}의 점수 {sum_Score[0][hakbon]} 누적점수/ {sum_Score[3][hakbon]}" )
        cnt += 1
    input_Data.close()
    #input('')

    input_Data = open('Math_2.txt', "r")
    lines = input_Data.readlines()

    cnt = 0
    for line in lines:
        line = line.strip("\n")
        field = line.split(" ")[0]
        hakbon = int(line.split(" ")[1])
        #hakbon_Math[cnt] = hakbon
        score = int(line.split(" ")[2])
        sum_Score[1][hakbon] = score
        sum_Score[3][hakbon] = sum_Score[3][hakbon] + score
        print(f"{hakbon}의 점수 {sum_Score[1][hakbon]} 누적점수/ {sum_Score[3][hakbon]}")
        cnt += 1
        #print(line)
    input_Data.close()
    #input('')

    cnt = 0
    input_Data = open('Math_3.txt', "r")
    lines = input_Data.readlines()
    for line in lines:
        line = line.rstrip(" ")
        field = line.split(" ")[0]
        hakbon = int(line.split(" ")[1])
        #hakbon_Math[cnt] = hakbon
        score = int(line.split(" ")[2])
        sum_Score[2][hakbon] = score
        sum_Score[3][hakbon] = sum_Score[3][hakbon] + score
        print(f"{hakbon}의 점수 {sum_Score[2][hakbon]} 누적점수/ {sum_Score[3][hakbon]}")
        cnt += 1
    input_Data.close()
    #input('')
    return
def sort_Data(Sum_Math, hakbon_Math):
    cnt = len(Sum_Math)
    for i in range(1, cnt-1, 1):
        min_i = i
        for j in range(i, cnt, 1):
            if Sum_Math[hakbon_Math[min_i]] < Sum_Math[hakbon_Math[j]]:
                min_i = j
        temp2 = hakbon_Math[min_i]
        hakbon_Math[min_i] = hakbon_Math[i]
        hakbon_Math[i] = temp2

def rank_Data(sum_Score, hakbon_Math, rating):
    r_no = 0
    r_tm = 0
    temp= 0
    flag = 0

    cnt = len(hakbon_Math)

    for index in range(1, cnt, 1):
        #print("index=", hakbon_Math[index-1])
        #input()
        if sum_Score[3][hakbon_Math[index-1]] is not sum_Score[3][hakbon_Math[index]]:
            r_no = r_no + ( r_tm + 1 )
            r_tm = 0
        else:
            r_tm += 1

        rating[hakbon_Math[index]] = r_no

        #print(f"rate[{sum_Score[3][hakbon_Math[index]]}] is rank {rating[hakbon_Math[index]]}")
    #input()
    return

def expected_Grade(num):
    if num <= 10 :
        return 'A+'
    elif num <= 25:
        return 'A0'
    elif num <= 35:
        return 'B+'
    elif num <= 55:
        return 'B0'
    elif num <= 70:
        return 'C+ or C0'
    elif num == 0:
        return 'F'
    else:
        return 'D+ or D0'

def view_Score(sum_Score, hakbon_Math, field_Math, rating, hakbon, cnt):

    output_data = open("output.txt", "w")

    #print(f"{field_Math[hakbon]}분반 {hakbon}번")

    output_data.write(str(field_Math[hakbon]))
    output_data.write("분반 ")
    output_data.write(str(hakbon))
    output_data.write("번\n")
    output_data.write(str(sum_Score[3][hakbon]))
    output_data.write("점\n")
    output_data.write("ratings: ")
    output_data.write(str(rating[hakbon]))
    output_data.write("/")
    output_data.write(str(cnt))
    output_data.write("\n")
    output_data.write("percentage : ")
    output_data.write(str(rating[hakbon]/cnt*100))
    output_data.write("%\n")
    output_data.write("expected grade : ")
    output_data.write(str(expected_Grade(rating[hakbon]/cnt*100)))

    print(f"{sum_Score[3][hakbon]}점")
    print(f"ratings : ( {rating[hakbon]}/{cnt} )")
    print(f"percentage : {rating[hakbon]/cnt*100}%")
    print(f"expected grade: {expected_Grade(rating[hakbon]/cnt*100)}")

def main():

    Score_Math = {}
    Sum_Math = {}
    sum_Score = [Score_Math, Score_Math, Score_Math, Sum_Math]
    field_Math = {}
    hakbon_Math = []
    rating = {}

    while(True):
        menu = int(input("(기초미적은 1, 일반미적은 2) 숫자 입력: "))
        hakbon = int(input("학번을 입력: "))

        if menu is 1:
            inputData(sum_Score, hakbon_Math, field_Math)
            break
        elif menu is 2:
            inputData2(sum_Score, hakbon_Math, field_Math)
            break
        else:
            print("잘못입력해서, 다시 입력")



    cnt = len(Sum_Math)
    sort_Data(Sum_Math, hakbon_Math)

    j = 0
    for i in Sum_Math:
        #print(Sum_Math[hakbon_Math[j]])
        j += 1

    rank_Data(sum_Score, hakbon_Math, rating)
    view_Score(sum_Score, hakbon_Math, field_Math, rating, hakbon, cnt)



main()
