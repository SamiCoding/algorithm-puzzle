// n = 8일 때 백과 흑을 교대로 나열할 수 있는 최소 횟수를 구해 보세요.

const N = 8 // 각 색의 수
let start = (1 << N) - 1 // 시작 상태(0이 N개, 1이 N개)
let mask = (1 << N*2) - 1 // 비트 마스크

// 목표 상태(0과 1을 번갈아 설정)
let goal1 = 0
for (let i=0; i<N; i++) {
  goal1 = (goal1 << 2) + 1
}
let goal2 = mask - goal1

// 1이 있는 비트의 수를 센다.
function bitcount(x) {
  x = (x & 0x55555555) + (x >> 1 & 0x55555555)
  x = (x & 0x33333333) + (x >> 2 & 0x33333333)
  x = (x & 0x0F0F0F0F) + (x >> 4 & 0x0F0F0F0F)
  x = (x & 0x00FF00FF) + (x >> 8 & 0x00FF00FF)
  x = (x & 0x0000FFFF) + (x >> 16 & 0x0000FFFF)
  return x
}

// 교환 횟수
let count = N*2
for (let i=0; i<(1<<N*2); i++) {
  let turn = i ^ (i << 1) ^ (i << 2)
  turn = (turn ^ (turn >> (N*2))) & mask

  // 골과 일치하면 교환하는 위치에 있는 수의 최소치를 판정
  if (((start ^ turn) == goal1) || ((start ^ turn) == goal2)) {
    if (count > bitcount(i)) {
      count = bitcount(i)
    }
  }
}
console.log(count)