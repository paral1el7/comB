cd git-practice-02
git branch -r
git checkout -b branch3 origin/branch3
git checkout -b branch2 origin/branch2
git merge branch3
git commit -m "merge"
git checkout main
git branch -D branch3


