#!/bin/zsh

if [ -e "test" ];then
  rm -rf ./test
fi

contest=$1
type=$2
param=$3
oj d https://atcoder.jp/contests/$contest/tasks/${contest}_${type}

#oj t -e 1e-6 -c "python3 ${type}.py" | grep "FAILURE"
oj t -c "python3 ${type}.py" | grep "FAILURE"

if [ $? = 0 ];then
  echo "テストエラー"
  return
else
  echo "テスト成功"
fi

if [ $param = "test" ];then
  return
fi

oj s https://atcoder.jp/contests/${contest/tasks/${contest}_${type} ${type}.py --guess-python-interpreter pypy