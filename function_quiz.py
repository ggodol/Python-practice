"""
Quiz) 표준 체중 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""

def std_weight (height, gender):
    if gender=="남자":
        std_weight = round(height*height*22/10000,2) # 남자 표준 체중 계산
        print ("키 {0} 남자의 표준 체중은 {1}kg 입니다.".format(height,std_weight))
    elif gender=="여자":
        std_weight = round(height*height*21/10000,2) # 여자 표준 체중 계산
        print ("키 {0} 여자의 표준 체중은 {1}kg 입니다.".format(height,std_weight))
    else:
        print ("입력한 성별이 올바르지 않습니다. \"남자\",\"여자\" 중 하나를 입력하세요.")

std_weight(175,"남자")
std_weight(158,"여자")
std_weight(303,"괴물")