// 1,000 ~ 9,999 중에서 앞의 조건을 만족하는 수를 구해 보세요.

/*
앞의 조건 )
나열된 각 숫자 사이에 사칙연산의 연산자를 넣어 계산해 보기
완성된 식을 계산한 결과 '원래 수를 거꾸로 나열한 숫자'가 되는 것
*/

let op = ["+", "-", "*", "/", ""]
for (i=1000; i<10000; i++) {
  let c = String(i)
  for (j=0; j<op.length; j++) {
    for (k=0; k<op.length; k++) {
      for (l=0; l<op.length; l++) {
        val = c.charAt(3) + op[j] + c.charAt(2) + op[k] + c.charAt(1) + op[l] + c.charAt(0)
        if (val.length > 4) {
          // 반드시 연산자를 하나는 넣는다.
          if (i === eval(val)) {
            console.log(val + " = " + i)
          }
        }
      }
    }
  }
}