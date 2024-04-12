// 남자 20명, 여자 10명이 도착하였을 때 어디에서 끊더라도 두 그룹 모두 남자와 여자의 수가 달라지게 되는 도착 순서가 몇 가지 있는지 구해 보세요.

let boy = 20
let girl = 10
boy += 1
girl += 1
let ary = new Array(girl)
for (let i=0; i<girl; i++) {
  ary[i] = new Array(boy)
  for (let j=0; j<boy; j++) {
    ary[i][j] = 0
  }
}
ary[0][0] = 1
for (let i=0; i<girl; i++) {
  for (let j=0; j<boy; j++) {
    if ((i!=j) && (boy-j != girl-i)) {
      if (j > 0) {
        ary[i][j] += ary[i][j-1]
      }
      if (i > 0) {
        ary[i][j] += ary[i-1][j]
      }
    }
  }
}
console.log(ary[girl-2][boy-1] + ary[girl-1][boy-2])