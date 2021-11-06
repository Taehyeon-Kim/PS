/**
n, k : 동전 종류(int) n개, 가치 k원
동전의 종류 n줄 입력
*/

import Foundation

// 입력
var input = readLine()!
.components(separatedBy: " ")
.compactMap({ Int($0) }) // [4, 4200]

var coins = [Int]()
for _ in 0 ..< input[0] {
  if let coin = Int(readLine()!) {
    coins.append(coin)
  }
}

// 내림차순 정렬
coins.sort(by: >)

// 계산
// 풀이 : 큰 동전부터 거슬러주는 방식
var count = 0
for coin in coins {
  count += input[1] / coin
  input[1] %= coin 
}

// 출력
print(count)