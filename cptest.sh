
#!/bin/bash

problem_name=$1
test_dir=test/${problem_name:0:3}/${problem_name:0:${#problem_name}-2}/${problem_name: -1}
base_url=${problem_name%_*}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${test_dir} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

oj test -c "python -u ${problem_name:0:3}/${problem_name:0:${#problem_name}-2}/${problem_name}.py" -d ${test_dir}

# 参考
# https://qiita.com/chokoryu/items/4b31ffb89dbc8cb86971