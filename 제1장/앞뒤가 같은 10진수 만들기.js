// 10진수, 2진수, 8진수 그 어느 것으로 표현하여도 대칭수가 되는 수 중, 10진수의 10 이상에서의 최솟값을 구해보세요.

// 문자열 형식을 역순으로 반환하는 메서드를 추가
String.prototype.reverse = function() {
  return this.split("").reverse().join("")
}

// 11부터 탐색 개시
let num = 11

while(true) {
  if (
    (num.toString() == num.toString().reverse()) &&
    (num.toString(8) == num.toString(8).reverse()) &&
    (num.toString(2) == num.toString(2).reverse())
    ) {
    console.log(num)
    break
  }
  
  // 홀수만 탐색하므로 2씩 늘림
  num += 2
}