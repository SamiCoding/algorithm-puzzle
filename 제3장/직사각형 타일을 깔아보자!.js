// 세로 4 × 가로 7인 욕실에 14장의 타일을 까는 방법을 구해 보세요.

let height = 4
let width = 7
let str = ""
let tatami = new Array(height+2)

// 초깃값을 설정(외주에 '-1', 내부에 '0'을 설정)
for (let h=0; h<=height+1; h++) {
  tatami[h] = new Array(width+2)
  for (let w=0; w<=width+1; w++) {
    tatami[h][w] = 0
    if ((h == 0) || (w == 0) || (h == height+1) || (w == width+1)) {
      tatami[h][w] = -1
    }
  }
}

// 타일을 표시
function printTatami() {
  for (let i=1; i<=height; i++) {
    for (let j=1; j<=width; j++) {
      // 가로로 배열되어 있을 때는 '-'를 표시
      if ((tatami[i][j] == tatami[i][j+1]) || (tatami[i][j] == tatami[i][j-1])) {
        str += "-"
      }
      // 세로로 배열되어 있을 때는 '|'를 표시
      if ((tatami[i][j] == tatami[i+1][j]) || (tatami[i][j] == tatami[i-1][j])) {
        str += "|"
      }
    }
    str += "\n"
  }
  str += "\n"
}

// 재귀적으로 타일을 설정
function setTatami(h, w, id) {
  if (h == height+1) { // 맨 마지막 행은 타일을 표시
    printTatami()
  }
  else if (w == width+1) { // 오른쪽 끝인 경우는 다음 행으로 이동
    setTatami(h+1, 1, id)
  }
  else if (tatami[h][w] > 0) { // 이미 설정 완료된 경우는 오른쪽으로 이동
    setTatami(h, w+1, id)
  }
  else { // 왼쪽 위와 위가 같은 경우, 왼쪽 위와 왼쪽이 같은 경우는 설정 가능
    if ((tatami[h-1][w-1] == tatami[h-1][w]) || (tatami[h-1][w-1] == tatami[h][w-1])) {
      if (tatami[h][w+1] == 0) { // 가로로 설정 가능한 경우
        tatami[h][w] = tatami[h][w+1] = id
        setTatami(h, w+2, id+1)
        tatami[h][w] = tatami[h][w+1] = 0
      }
      if (tatami[h+1][w] == 0) { // 세로로 설정 가능한 경우
        tatami[h][w] = tatami[h+1][w] = id
        setTatami(h, w+1, id+1)
        tatami[h][w] = tatami[h+1][w] = 0
      }
    }
  }
}

setTatami(1, 1, 1)
console.log(str)